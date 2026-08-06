import base64
import json
import os
import urllib.request

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
BRANCH = "consolidation-control"
PUBLIC_REPO = "fabio-ara/ARA"
SCRIPT_PATH = ".github/process-cross-domain-benchmark.py"
WORKFLOW_PATH = ".github/workflows/process-cross-domain-benchmark.yml"


def api(method: str, path: str, payload=None):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        "https://api.github.com" + path,
        data=data,
        method=method,
        headers={
            "Authorization": "Bearer " + TOKEN,
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request) as response:
        body = response.read()
        return json.loads(body) if body else None


def get_text(repo: str, path: str, ref: str) -> str:
    obj = api("GET", f"/repos/{repo}/contents/{path}?ref={ref}")
    return base64.b64decode(obj["content"]).decode("utf-8")


inventory_text = get_text(REPO, "SOURCE_INVENTORY.jsonl", BRANCH)
records = [json.loads(line) for line in inventory_text.splitlines()]
assert len(records) == 558
assert [record["id"] for record in records] == [f"SRC-{i:06d}" for i in range(1, 559)]
assert len({record["locator"] for record in records}) == 558

before = {}
for record in records:
    before[record["status"]] = before.get(record["status"], 0) + 1
assert before == {"verified": 51, "processed": 13, "identified": 494}, before

updates = {
    "SRC-000033": "Issue de síntese integrada que exige peso analítico equivalente para a referência AraLearn e o espaço externo, amostragem de variação máxima e classificação sem conversão automática em engenharia. Consolidada em EXP-007 a EXP-010.",
    "SRC-000035": "Issue do benchmark transdomínio. Trata os recursos anteriores como sementes legadas situadas e exige separar representação, resposta, validação, retorno, extensão e execução antes de qualquer herança.",
    "SRC-000076": "Pull request que confirma benchmark de 21 sistemas e 16 fontes exploratórias. Precedentes técnicos, gramáticas de domínio e limitações foram preservados sem seleção de stack ou alegação de efetividade.",
    "SRC-000080": "Pull request da síntese integrada que recomenda extensibilidade governada em camadas e registra cobertura e lacunas. A recomendação permanece pendência, não decisão ou autorização de implementação.",
    "SRC-000223": "Mapa de quarenta possibilidades externas usado para identificar famílias e riscos. Classificações provisórias não foram copiadas em bloco nem convertidas em requisitos; capacidades específicas seguem para seus domínios.",
    "SRC-000228": "Registro de amostragem representativa e saturação relativa às decisões. Sustenta EXP-010 e mantém explícitas lacunas de usuários, instituições, acessibilidade e efetividade.",
    "SRC-000248": "Resumo estruturado do benchmark. Confirma 21 sistemas, separações de responsabilidade, hipótese de gênero e ausência de seleção tecnológica ou evidência de efetividade.",
    "SRC-000249": "Mapa de capacidades e precedentes usado para EXP-008 e EXP-009. Direções de primeiros princípios e protótipos permanecem alternativas de investigação.",
    "SRC-000250": "Cobertura de domínios que demonstra lacunas em matemática, programação, ciências, mapas, música, circuitos, línguas, humanidades e autoria. Lacunas não foram transformadas automaticamente em requisitos.",
    "SRC-000251": "Manifesto de 21 repositórios com revisões, caminhos, licenças e papel das fontes. Preservado como base de procedência para EXP-007, sem incorporar dependências.",
    "SRC-000252": "Benchmark detalhado de representação, resposta, validação, retorno, autoria, execução, acessibilidade e riscos. Usado como precedente técnico, não prova educacional nem escolha de produto.",
    "SRC-000447": "Síntese principal do benchmark transdomínio. Gramáticas de domínio, governança de capacidades e exclusão de código arbitrário foram registradas como pendências, não decisões arquiteturais.",
}

by_id = {record["id"]: record for record in records}
for source_id, notes in updates.items():
    record = by_id[source_id]
    assert record["domain"] == "experiências e sistemas analisados", source_id
    assert record["status"] == "identified", (source_id, record["status"])
    record["status"] = "processed"
    record["relevant"] = True
    record["destination"] = "BACKLOG.yaml"
    record["notes"] = notes

counts = {}
for record in records:
    counts[record["status"]] = counts.get(record["status"], 0) + 1
assert counts == {"verified": 51, "processed": 25, "identified": 482}, counts

backlog = get_text(PUBLIC_REPO, "BACKLOG.yaml", "main")
for item_id in ["EXP-007", "EXP-008", "EXP-009", "EXP-010"]:
    assert backlog.count(f"  - id: {item_id}\n") == 1, item_id
segment = backlog[backlog.index("  - id: EXP-007"):]
assert "decision_refs:" not in segment
assert "status: approved" not in segment
for forbidden in [
    "ARA-pre-consolidation", "consolidation-control", "SOURCE_INVENTORY",
    "CONSOLIDATION_STATUS", "SRC-000", "research/data/", "research/pt-BR/",
]:
    assert forbidden not in backlog, forbidden

final_batch = [
    "SRC-000029", "SRC-000064", "SRC-000065",
    "SRC-000068", "SRC-000316", "SRC-000354",
]
for source_id in final_batch:
    record = by_id[source_id]
    assert record["domain"] == "experiências e sistemas analisados", source_id
    assert record["status"] == "identified", source_id

new_inventory = "\n".join(
    json.dumps(record, ensure_ascii=False, separators=(",", ":")) for record in records
) + "\n"
new_status = """corpus:
  branch: main
  commit: d5f83c1fdb2047de0080510540d2b911aec3cd8b
  cutoff: "2026-08-06T00:32:00-03:00"

phase: processing

counts:
  total: 558
  identified: 482
  processed: 25
  discarded: 0
  blocked: 0
  verified: 51

domains:
  finalidade_e_escopo: verified
  fundamentos_educacionais: verified
  experiencias_e_sistemas_analisados: processing
  modelo_de_conteudo_e_recursos: identified
  autoria_e_curadoria: identified
  interfaces_e_experiencia_de_uso: identified
  versionamento_e_proveniencia: identified
  colaboracao_e_acesso: identified
  parametrizacao_e_experimentacao: identified
  dados_e_pesquisa_educacional: identified
  infraestrutura_e_armazenamento: identified
  sincronizacao_e_funcionamento_offline: identified
  implantacao_e_interoperabilidade: identified
  avaliacao_e_validacao: identified
  relacao_com_a_pesquisa_academica: identified

blockers: []
pending_decisions: []

last_batch: >-
  Segundo lote de experiências e sistemas analisados concluído: 12 fontes do
  benchmark transdomínio e da síntese integrada processadas. Precedentes técnicos,
  gramáticas de domínio, governança de capacidades e lacunas de validação foram
  consolidados em quatro pendências, sem requisitos automáticos ou seleção de stack.

next_step: >-
  Processar o lote final de experiências e sistemas analisados: SRC-000029,
  SRC-000064, SRC-000065, SRC-000068, SRC-000316 e SRC-000354; consolidar
  antecedentes iniciais, sistemas relacionados, programação móvel e a matriz de
  atividades e retorno pedagógico, deduplicar com EXP-001 a EXP-010 e preparar a
  auditoria do domínio sem transformar observação de produto em evidência causal.
"""

head = api("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}")["object"]["sha"]
commit = api("GET", f"/repos/{REPO}/git/commits/{head}")
base_tree = commit["tree"]["sha"]

inventory_blob = api("POST", f"/repos/{REPO}/git/blobs", {
    "content": new_inventory,
    "encoding": "utf-8",
})["sha"]
status_blob = api("POST", f"/repos/{REPO}/git/blobs", {
    "content": new_status,
    "encoding": "utf-8",
})["sha"]
new_tree = api("POST", f"/repos/{REPO}/git/trees", {
    "base_tree": base_tree,
    "tree": [
        {"path": "SOURCE_INVENTORY.jsonl", "mode": "100644", "type": "blob", "sha": inventory_blob},
        {"path": "CONSOLIDATION_STATUS.yaml", "mode": "100644", "type": "blob", "sha": status_blob},
        {"path": SCRIPT_PATH, "mode": "100644", "type": "blob", "sha": None},
        {"path": WORKFLOW_PATH, "mode": "100644", "type": "blob", "sha": None},
    ],
})["sha"]
new_commit = api("POST", f"/repos/{REPO}/git/commits", {
    "message": "chore: process cross-domain benchmark batch",
    "tree": new_tree,
    "parents": [head],
})["sha"]
api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {
    "sha": new_commit,
    "force": False,
})

print("cross_domain_sources_processed: 12")
print("public_benchmark_items_verified: 4")
print("final_experience_batch_verified: 6")
print("commit:", new_commit)
