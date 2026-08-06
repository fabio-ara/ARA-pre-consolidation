import base64
import json
import os
import re
import urllib.request
from pathlib import Path

TOKEN = os.environ["GITHUB_TOKEN"]
PUBLIC_REPO = "fabio-ara/ARA"


def api(path: str):
    request = urllib.request.Request(
        "https://api.github.com" + path,
        headers={
            "Authorization": "Bearer " + TOKEN,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def public_file(path: str) -> str:
    obj = api(f"/repos/{PUBLIC_REPO}/contents/{path}?ref=main")
    return base64.b64decode(obj["content"]).decode("utf-8")


inventory_path = Path("SOURCE_INVENTORY.jsonl")
records = [json.loads(line) for line in inventory_path.read_text(encoding="utf-8").splitlines()]
assert len(records) == 558
assert [record["id"] for record in records] == [f"SRC-{i:06d}" for i in range(1, 559)]
assert len({record["locator"] for record in records}) == 558

before = {}
for record in records:
    before[record["status"]] = before.get(record["status"], 0) + 1
assert before == {"verified": 35, "processed": 16, "identified": 507}, before

foundations = [record for record in records if record["domain"] == "fundamentos educacionais"]
assert len(foundations) == 16
for record in foundations:
    assert record["status"] == "processed", record
    assert record["relevant"] is True, record
    assert record["destination"] == "BACKLOG.yaml", record
    assert record["notes"].strip(), record

root = api(f"/repos/{PUBLIC_REPO}/contents?ref=main")
root_names = sorted(entry["name"] for entry in root)
assert root_names == sorted(["README.md", "BACKLOG.yaml", "DECISOES.md", "METODO_DE_TRABALHO.md", "LICENSE"]), root_names

texts = {name: public_file(name) for name in root_names}
forbidden_private = [
    "ARA-pre-consolidation",
    "consolidation-control",
    "SOURCE_INVENTORY",
    "CONSOLIDATION_STATUS",
    "PROTOCOLO_CONSOLIDACAO_ARA",
    "SRC-000",
    "github:issue/",
    "github:pull/",
    "research/data/",
    "research/pt-BR/",
]
for path, text in texts.items():
    for term in forbidden_private:
        assert term not in text, (path, term)
    assert "—" not in text, path

issues = api(f"/repos/{PUBLIC_REPO}/issues?state=all&per_page=100")
for issue in issues:
    combined = "\n".join(filter(None, [issue.get("title"), issue.get("body")]))
    for term in forbidden_private:
        assert term not in combined, (issue.get("number"), term)

backlog = texts["BACKLOG.yaml"]
assert backlog.count("  - id: PED-") == 11
ped_segment = re.search(
    r"(?ms)^  - id: PED-001\n.*?(?=^  - id: AGENT-001\n)", backlog
).group(0)

expected_statuses = {
    "PED-001": "pending_research",
    "PED-002": "pending_research",
    "PED-003": "captured",
    "PED-004": "pending_research",
    "PED-005": "captured",
    "PED-006": "pending_research",
    "PED-007": "pending_research",
    "PED-008": "pending_research",
    "PED-009": "pending_research",
    "PED-010": "pending_research",
    "PED-011": "captured",
}
for item_id, status in expected_statuses.items():
    match = re.search(
        rf"(?ms)^  - id: {item_id}\n(.*?)(?=^  - id: |\Z)", ped_segment
    )
    assert match, item_id
    block = match.group(0)
    assert f"    status: {status}\n" in block, (item_id, status)
    assert "decision_refs:" not in block, item_id
    assert "    next_action:" in block, item_id

assert "status: approved" not in ped_segment
for term in [
    "analytics",
    "mobile-first",
    "offline",
    "default",
    "overrides",
    "scaffolding",
    "scaffolds",
    "expertise",
    "rollback",
    "snapshot",
    "fallback",
    "guardrails",
    "constructo",
    "feedback",
]:
    assert term not in ped_segment, term

required_limitations = [
    "sem produzir interpretações equivalentes",
    "não sustentam uma regra universal",
    "não demonstram automaticamente",
    "sem tratá-la como padrão universal",
    "Não existe limiar universal",
    "recomendação a investigar",
    "não sustentam algoritmo, intervalo ou mistura universais",
    "sem retirar informação essencial",
    "não se torna autoridade educacional",
    "não substituem revisões da literatura",
]
for phrase in required_limitations:
    assert phrase in ped_segment, phrase

assert "## DEC-008" not in texts["DECISOES.md"]
assert len(re.findall(r"(?m)^## DEC-\d{3} - ", texts["DECISOES.md"])) == 7
assert "PED-" not in texts["DECISOES.md"]

for record in foundations:
    record["status"] = "verified"

after = {}
for record in records:
    after[record["status"]] = after.get(record["status"], 0) + 1
assert after == {"verified": 51, "identified": 507}, after

inventory_path.write_text(
    "\n".join(json.dumps(record, ensure_ascii=False, separators=(",", ":")) for record in records) + "\n",
    encoding="utf-8",
)

Path("CONSOLIDATION_STATUS.yaml").write_text(
    """corpus:
  branch: main
  commit: d5f83c1fdb2047de0080510540d2b911aec3cd8b
  cutoff: "2026-08-06T00:32:00-03:00"

phase: processing

counts:
  total: 558
  identified: 507
  processed: 0
  discarded: 0
  blocked: 0
  verified: 51

domains:
  finalidade_e_escopo: verified
  fundamentos_educacionais: verified
  experiencias_e_sistemas_analisados: identified
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
  Auditoria do domínio fundamentos educacionais concluída sobre 16 fontes e
  onze pendências. Evidências, recomendações e decisões permanecem separadas;
  limitações e ausência de valores universais estão explícitas. A terminologia
  pública foi normalizada e não foram encontradas referências privadas.

next_step: >-
  Processar o primeiro lote de experiências e sistemas analisados sobre a
  referência AraLearn: SRC-000034, SRC-000075, SRC-000139, SRC-000231 a
  SRC-000237, SRC-000444, SRC-000446 e SRC-000463; separar capacidades
  demonstradas, limitações, conflitos e decisões provisórias sem copiar a
  implementação anterior nem promover classificações de auditoria a decisões.
""",
    encoding="utf-8",
)

print("foundations_verified: 16")
print("public_ped_items_verified: 11")
print("private_references_found: 0")
