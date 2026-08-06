import base64
import json
import os
import re
import urllib.request

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
BRANCH = "consolidation-control"
PUBLIC_REPO = "fabio-ara/ARA"
SCRIPT_PATH = ".github/process-cross-domain-benchmark.py"


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
assert before == {"verified": 51, "processed": 31, "identified": 476}, before

experience_ids = [
    "SRC-000029", "SRC-000033", "SRC-000034", "SRC-000035",
    "SRC-000064", "SRC-000065", "SRC-000068", "SRC-000075",
    "SRC-000076", "SRC-000080", "SRC-000139", "SRC-000223",
    "SRC-000228", "SRC-000231", "SRC-000232", "SRC-000233",
    "SRC-000234", "SRC-000235", "SRC-000236", "SRC-000237",
    "SRC-000248", "SRC-000249", "SRC-000250", "SRC-000251",
    "SRC-000252", "SRC-000316", "SRC-000354", "SRC-000444",
    "SRC-000446", "SRC-000447", "SRC-000463",
]
assert len(experience_ids) == 31
by_id = {record["id"]: record for record in records}
experience_records = [record for record in records if record["domain"] == "experiências e sistemas analisados"]
assert len(experience_records) == 31, len(experience_records)
assert [record["id"] for record in experience_records] == experience_ids
for source_id in experience_ids:
    record = by_id[source_id]
    assert record["status"] == "processed", (source_id, record["status"])
    assert record["relevant"] is True, source_id
    assert record["destination"] == "BACKLOG.yaml", source_id
    assert record["notes"].strip(), source_id

public_files = {
    "README.md": get_text(PUBLIC_REPO, "README.md", "main"),
    "BACKLOG.yaml": get_text(PUBLIC_REPO, "BACKLOG.yaml", "main"),
    "DECISOES.md": get_text(PUBLIC_REPO, "DECISOES.md", "main"),
    "METODO_DE_TRABALHO.md": get_text(PUBLIC_REPO, "METODO_DE_TRABALHO.md", "main"),
    "LICENSE": get_text(PUBLIC_REPO, "LICENSE", "main"),
}
backlog = public_files["BACKLOG.yaml"]
decisions = public_files["DECISOES.md"]
readme = public_files["README.md"]
method = public_files["METODO_DE_TRABALHO.md"]

# Public autonomy and absence of private consolidation references.
for name, text in public_files.items():
    for forbidden in [
        "ARA-pre-consolidation", "consolidation-control", "SOURCE_INVENTORY",
        "CONSOLIDATION_STATUS", "SRC-000", "github:issue/", "github:pull/",
        "d5f83c1fdb2047de0080510540d2b911aec3cd8b", "research/data/",
        "research/pt-BR/",
    ]:
        assert forbidden not in text, (name, forbidden)

issues = api("GET", f"/repos/{PUBLIC_REPO}/issues?state=all&per_page=100")
for issue in issues:
    text = (issue.get("title") or "") + "\n" + (issue.get("body") or "")
    for forbidden in [
        "ARA-pre-consolidation", "consolidation-control", "SOURCE_INVENTORY",
        "CONSOLIDATION_STATUS", "SRC-000", "d5f83c1fdb2047de0080510540d2b911aec3cd8b",
    ]:
        assert forbidden not in text, (issue["number"], forbidden)

# Canonical decision boundary.
for number in range(1, 8):
    assert decisions.count(f"## DEC-{number:03d} -") == 1, number
assert "DEC-008" not in decisions
assert "componentes internos e escolhas técnicas do sistema anterior não são herdados automaticamente" in decisions
assert "não existe programa de implementação ativo" in readme.lower()
for category in ["Ideia", "evidência", "hipótese", "alternativa", "recomendação", "decisão", "requisito", "validação"]:
    assert category.lower() in method.lower(), category

# EXP items remain research/candidate material, never silent decisions.
exp_positions = []
for number in range(1, 11):
    item_id = f"EXP-{number:03d}"
    needle = f"  - id: {item_id}\n"
    assert backlog.count(needle) == 1, item_id
    exp_positions.append((item_id, backlog.index(needle)))
for index, (item_id, start) in enumerate(exp_positions):
    end = exp_positions[index + 1][1] if index + 1 < len(exp_positions) else len(backlog)
    section = backlog[start:end]
    assert "decision_refs:" not in section, item_id
    status_match = re.search(r"^    status: ([a-z_]+)$", section, re.M)
    assert status_match, item_id
    assert status_match.group(1) in {"captured", "pending_research"}, (item_id, status_match.group(1))

required_phrases = [
    "Capacidades apenas documentadas, inferidas ou propostas não devem ser",
    "Esses elementos formam uma referência, não autorização",
    "baseline verificável, não como ontologia",
    "Não há decisão sobre compatibilidade, importação ou migração",
    "Relato pessoal, descrição oficial do produto, estudo independente",
    "não demonstram efetividade educacional nem obrigam sua adoção",
    "alternativa não recomendada pelas fontes atuais",
    "não valida interações avançadas, requisitos",
]
for phrase in required_phrases:
    assert phrase in backlog, phrase

exp_segment = backlog[exp_positions[0][1]:]
for technology in ["React", "Vue", "Supabase", "Firebase", "Cytoscape", "MathLive", "Recogito", "PostgreSQL"]:
    assert technology not in exp_segment, technology

# Experience source notes preserve the intended evidence categories and limitations.
notes = "\n".join(by_id[source_id]["notes"] for source_id in experience_ids).lower()
for concept in [
    "experiência pessoal", "descrição oficial", "estudo independente", "precedente técnico",
    "não prova educacional", "não foram tratados como aprendizagem causal", "provisóri",
    "sem seleção de stack", "não como taxonomia completa", "não como ontologia",
]:
    assert concept in notes, concept

# Verify the bounded first batch of the next domain.
next_batch = ["SRC-000021", "SRC-000090", "SRC-000125"] + [f"SRC-{i:06d}" for i in range(297, 306)]
assert len(next_batch) == 12
for source_id in next_batch:
    record = by_id[source_id]
    assert record["domain"] == "modelo de conteúdo e recursos", (source_id, record["domain"])
    assert record["status"] == "identified", (source_id, record["status"])

# Audit outcome: processed experience sources become verified.
for source_id in experience_ids:
    by_id[source_id]["status"] = "verified"

counts = {}
for record in records:
    counts[record["status"]] = counts.get(record["status"], 0) + 1
assert counts == {"verified": 82, "identified": 476}, counts
assert not [record for record in records if record["domain"] == "experiências e sistemas analisados" and record["status"] != "verified"]

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
  processed: 0
  discarded: 0
  blocked: 0
  verified: 82

domains:
  finalidade_e_escopo: verified
  fundamentos_educacionais: verified
  experiencias_e_sistemas_analisados: verified
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
  Auditoria do domínio experiências e sistemas analisados concluída: 31 fontes
  verificadas e EXP-001 a EXP-010 conferidos. Experiência situada, implementação,
  descrição de produto, precedente técnico, estudo independente e alegação causal
  permanecem categorias distintas; não há seleção tecnológica, requisito automático,
  promoção silenciosa a decisão ou referência privada nos registros públicos.

next_step: >-
  Processar o primeiro lote de modelo de conteúdo e recursos: SRC-000021,
  SRC-000090, SRC-000125 e SRC-000297 a SRC-000305; consolidar modelo de domínio,
  entidades, invariantes, jornadas, máquinas de estado, classificação de capacidades
  e síntese decisória, separando contratos e recomendações candidatos de decisões
  aprovadas e sem herdar automaticamente o modelo legado.
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
    ],
})["sha"]
new_commit = api("POST", f"/repos/{REPO}/git/commits", {
    "message": "chore: verify experience systems domain",
    "tree": new_tree,
    "parents": [head],
})["sha"]
api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {
    "sha": new_commit,
    "force": False,
})

print("experience_sources_verified: 31")
print("public_exp_items_verified: 10")
print("public_issues_checked:", len(issues))
print("next_model_batch_verified: 12")
print("commit:", new_commit)
