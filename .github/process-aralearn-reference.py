import base64
import json
import os
import urllib.request

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
BRANCH = "consolidation-control"
PUBLIC_REPO = "fabio-ara/ARA"
SCRIPT_PATH = ".github/process-aralearn-reference.py"
WORKFLOW_PATH = ".github/workflows/process-aralearn-reference.yml"


def api(method: str, path: str, payload=None):
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
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
assert before == {"verified": 51, "identified": 507}, before

updates = {
    "SRC-000034": "Issue que exige auditoria canônica dos contratos de recursos, separação entre implementação, documentação e implicações para o ARA e registro explícito de conflitos. Consolidada em EXP-001, EXP-003 e EXP-004.",
    "SRC-000075": "Pull request que confirma o baseline implementado de 18 recursos, seus testes, exclusões e limitações. Classificações de preservar ou revisar foram tratadas como provisórias, não decisões públicas.",
    "SRC-000139": "Auditoria integral do AraLearn usada para identificar capacidades demonstradas, limites arquiteturais, invariantes candidatos e questões de compatibilidade. Nenhum serviço, esquema ou fluxo foi copiado como requisito.",
    "SRC-000231": "Matriz de preservação de capacidades consolidada seletivamente em EXP-002 e EXP-005. Estados como preservar, reformular ou adiar permanecem recomendações de análise.",
    "SRC-000232": "Matriz de cobertura disciplinar que demonstra variedade representacional e limitações por domínio. Usada em EXP-003 e EXP-004 sem alegação de suficiência universal.",
    "SRC-000233": "Matriz de reclassificação de conceitos legados usada para separar representação, resposta, validação, composição e retorno pedagógico. Suas decisões são provisórias de pesquisa e prototipagem.",
    "SRC-000234": "Manifesto de fontes da auditoria usado para sustentar a hierarquia de autoridade entre documentação, código executável, testes e exemplos registrada em EXP-001.",
    "SRC-000235": "Resumo estruturado do baseline de recursos, exclusões e evidências de validação. Preservado como referência verificável, não como taxonomia completa nem evidência de eficácia.",
    "SRC-000236": "Mapa dos alvos efetivamente praticáveis que confirma a predominância de lacunas literais e escolhas exatas e sustenta a pendência EXP-004.",
    "SRC-000237": "Inventário detalhado dos 18 recursos, limites semânticos e móveis e classificações provisórias. Usado para EXP-003 e EXP-004 sem copiar campos ou contratos.",
    "SRC-000444": "Registro de antecedentes pessoais e sistemas comparáveis. Experiência pessoal, descrição oficial, estudo independente, eficácia e requisito permaneceram categorias distintas em EXP-006.",
    "SRC-000446": "Síntese principal da auditoria canônica dos recursos. Confirma o baseline, a separação conceitual e lacunas de interação; decisões provisórias não foram promovidas.",
    "SRC-000463": "Registro provisório de reclassificação dos conceitos legados após protótipos. Preservado como alternativa analítica para EXP-003, sem autorizar migração, bibliotecas ou arquitetura.",
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
assert counts == {"verified": 51, "processed": 13, "identified": 494}, counts

backlog = get_text(PUBLIC_REPO, "BACKLOG.yaml", "main")
for item_id in ["EXP-001", "EXP-002", "EXP-003", "EXP-004", "EXP-005", "EXP-006"]:
    assert backlog.count(f"  - id: {item_id}\n") == 1, item_id
segment = backlog[backlog.index("  - id: EXP-001"):]
assert "decision_refs:" not in segment
assert "status: approved" not in segment
for forbidden in [
    "ARA-pre-consolidation",
    "consolidation-control",
    "SOURCE_INVENTORY",
    "CONSOLIDATION_STATUS",
    "SRC-000",
    "research/data/",
    "research/pt-BR/",
]:
    assert forbidden not in backlog, forbidden

next_batch = [
    "SRC-000033", "SRC-000035", "SRC-000076", "SRC-000080",
    "SRC-000223", "SRC-000228", "SRC-000248", "SRC-000249",
    "SRC-000250", "SRC-000251", "SRC-000252", "SRC-000447",
]
for source_id in next_batch:
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
  identified: 494
  processed: 13
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
  Primeiro lote de experiências e sistemas analisados concluído: 13 fontes da
  referência AraLearn processadas. Capacidades demonstradas, limites, hierarquia
  das evidências, reclassificações provisórias, compatibilidade e antecedentes
  pessoais foram consolidados em seis pendências, sem decisões ou migração.

next_step: >-
  Processar o segundo lote de experiências e sistemas analisados sobre benchmark
  transdomínio e espaço externo: SRC-000033, SRC-000035, SRC-000076,
  SRC-000080, SRC-000223, SRC-000228, SRC-000248 a SRC-000252 e
  SRC-000447; separar precedentes técnicos, evidência educacional, alternativas
  e lacunas sem transformar funcionalidades de terceiros em requisitos.
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
    "message": "chore: process AraLearn reference batch",
    "tree": new_tree,
    "parents": [head],
})["sha"]
api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {
    "sha": new_commit,
    "force": False,
})

print("aralearn_reference_processed: 13")
print("public_experience_items_verified: 6")
print("next_external_batch_verified: 12")
print("commit:", new_commit)
