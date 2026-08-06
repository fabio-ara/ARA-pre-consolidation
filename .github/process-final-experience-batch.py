import base64
import json
import os
import urllib.request

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
BRANCH = "consolidation-control"
PUBLIC_REPO = "fabio-ara/ARA"
SCRIPT_PATH = ".github/process-final-experience-batch.py"
WORKFLOW_PATH = ".github/workflows/process-final-experience-batch.yml"


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
assert before == {"verified": 51, "processed": 25, "identified": 482}, before

updates = {
    "SRC-000029": "Issue que delimita a atualização sobre aprendizagem móvel de programação, exige separar tarefas, medidas, percepções e continuidade e proíbe inferência causal indevida. Consolidada por EXP-006, EXP-007, EXP-010 e pelas restrições pedagógicas vigentes.",
    "SRC-000064": "Pull request que documenta Anki, Duolingo e SoloLearn como antecedentes formativos e separa experiência pessoal, descrição oficial, estudo independente e evidência geral. Confirma EXP-006, EXP-007 e RES-002 sem conteúdo público adicional necessário.",
    "SRC-000065": "Pull request que amplia os antecedentes para outros aplicativos e plataformas e preserva anonimato, ambiguidade histórica e limites das descrições atuais. Deduplicado em EXP-006, EXP-007 e RES-002.",
    "SRC-000068": "Pull request que confirma atualização provisória sobre programação móvel, classificação de tarefas e matriz sistema-atividade-retorno. Resultados de experiência, engajamento e estudos transversais não foram tratados como aprendizagem causal.",
    "SRC-000316": "Corpus de oito revisões e estudos de 2023 a 2026. Preserva heterogeneidade, foco introdutório, ausência de transferência longitudinal e limites de validação; lacunas já estão cobertas por EXP-010 e pelas pendências pedagógicas e acadêmicas.",
    "SRC-000354": "Matriz comparativa de sistemas, atividades, execução, avaliação, retorno, tentativas, progressão, consequências e resultados medidos. Reforça que produtos não são pedagogias unitárias e foi deduplicada em EXP-007, PED-001 a PED-005 e RES-002.",
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
assert counts == {"verified": 51, "processed": 31, "identified": 476}, counts
assert not [
    record for record in records
    if record["domain"] == "experiências e sistemas analisados" and record["status"] == "identified"
]

backlog = get_text(PUBLIC_REPO, "BACKLOG.yaml", "main")
for item_id in [f"EXP-{number:03d}" for number in range(1, 11)]:
    assert backlog.count(f"  - id: {item_id}\n") == 1, item_id
for required in [
    "Usar experiências pessoais como evidência situada",
    "Tratar sistemas externos como precedentes, não requisitos",
    "Registrar cobertura representativa e lacunas de validação",
    "Registrar restrições de interpretação para respostas e resultados",
    "Organizar evidências por autoridade, procedência e estabilidade temporal",
]:
    assert required in backlog, required
for forbidden in [
    "ARA-pre-consolidation", "consolidation-control", "SOURCE_INVENTORY",
    "CONSOLIDATION_STATUS", "SRC-000", "research/data/", "research/pt-BR/",
]:
    assert forbidden not in backlog, forbidden

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
  identified: 476
  processed: 31
  discarded: 0
  blocked: 0
  verified: 51

domains:
  finalidade_e_escopo: verified
  fundamentos_educacionais: verified
  experiencias_e_sistemas_analisados: pending_audit
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
  Lote final de experiências e sistemas analisados concluído: seis fontes sobre
  antecedentes, sistemas relacionados e programação móvel processadas. As fontes
  foram deduplicadas contra EXP-006, EXP-007, EXP-010, fundamentos pedagógicos e
  procedência; nenhuma observação de produto foi tratada como evidência causal.

next_step: >-
  Auditar o domínio experiências e sistemas analisados: conferir as 31 fontes,
  a coerência de EXP-001 a EXP-010, a separação entre experiência situada,
  evidência implementada, descrição de produto, precedente técnico, estudo
  independente e alegação causal, a ausência de seleção tecnológica ou requisito
  automático e a ausência de referências privadas; marcar o domínio como verificado
  ou materializar as correções encontradas.
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
    "message": "chore: process final experience systems batch",
    "tree": new_tree,
    "parents": [head],
})["sha"]
api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {
    "sha": new_commit,
    "force": False,
})

print("final_experience_sources_processed: 6")
print("public_items_reused: 5")
print("domain_identified_remaining: 0")
print("commit:", new_commit)
