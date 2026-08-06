import base64
import json
import os
import urllib.request
from pathlib import Path

REPO = os.environ["GITHUB_REPOSITORY"]
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


inventory_path = Path("SOURCE_INVENTORY.jsonl")
records = [json.loads(line) for line in inventory_path.read_text(encoding="utf-8").splitlines()]
assert len(records) == 558
assert [record["id"] for record in records] == [f"SRC-{index:06d}" for index in range(1, 559)]
assert len({record["locator"] for record in records}) == 558

before = {}
for record in records:
    before[record["status"]] = before.get(record["status"], 0) + 1
assert before == {"verified": 35, "identified": 523}, before

updates = {
    "SRC-000028": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Issue de pesquisa que delimita formatos de resposta e feedback, separa aprendizagem, validade, usabilidade e preferência e proíbe defaults universais; consolidada em PED-001 a PED-004.",
    ),
    "SRC-000067": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Pull request que confirma a conclusão da síntese focada e suas validações metodológicas; parâmetros permaneceram variáveis de pesquisa, não defaults.",
    ),
    "SRC-000317": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Síntese decisória de pesquisa usada como recomendação não normativa. Dimensões, riscos, incertezas e não autorizações foram preservados em PED-001 a PED-005, sem promover parâmetros aceitos anteriormente a decisões públicas.",
    ),
    "SRC-000318": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Corpus de evidências que sustenta a decomposição da prática, as restrições interpretativas, a acessibilidade estrutural e a ausência de vencedor universal para formato, timing, tentativas ou consequências.",
    ),
    "SRC-000319": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Registro estruturado de parâmetros candidatos. Foi consolidado em cinco pendências de pesquisa e governança; valores, precedências e handoffs permanecem candidatos, não contrato de produção.",
    ),
    "SRC-000320": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Comparação de perfis preservada em PED-005. O perfil de referência anterior não foi transformado em default universal e os perfis alternativos não foram aprovados.",
    ),
    "SRC-000351": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Corpus complementar sobre formatos de resposta e feedback. Resultados quantitativos foram usados somente para sustentar perguntas e restrições, sem transpor notas entre formatos nem generalizar evidência de domínios específicos.",
    ),
    "SRC-000456": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Síntese crítica principal do pacote P1. Recomendações sobre prática, tentativas, revelação, feedback, consequências, acessibilidade e instrumentação foram registradas como pendências, não decisões.",
    ),
    "SRC-000467": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Síntese focada inicial que separa demanda cognitiva, pontuação, conteúdo e timing do feedback. Suas taxonomias e limitações foram incorporadas seletivamente em PED-001 a PED-004.",
    ),
}

by_id = {record["id"]: record for record in records}
for source_id, (status, relevant, destination, notes) in updates.items():
    record = by_id[source_id]
    assert record["domain"] == "fundamentos educacionais", source_id
    assert record["status"] == "identified", (source_id, record["status"])
    record["status"] = status
    record["relevant"] = relevant
    record["destination"] = destination
    record["notes"] = notes

after = {}
for record in records:
    after[record["status"]] = after.get(record["status"], 0) + 1
assert after == {"verified": 35, "processed": 9, "identified": 514}, after

remaining_foundations = [
    record["id"]
    for record in records
    if record["domain"] == "fundamentos educacionais" and record["status"] == "identified"
]
assert remaining_foundations == [
    "SRC-000321",
    "SRC-000322",
    "SRC-000323",
    "SRC-000324",
    "SRC-000452",
    "SRC-000457",
    "SRC-000458",
], remaining_foundations

public = api(f"/repos/{PUBLIC_REPO}/contents/BACKLOG.yaml?ref=main")
backlog = base64.b64decode(public["content"]).decode("utf-8")
for item_id in ["PED-001", "PED-002", "PED-003", "PED-004", "PED-005"]:
    assert backlog.count(f"  - id: {item_id}\n") == 1, item_id
for forbidden in ["ARA-pre-consolidation", "consolidation-control", "SRC-000", "research/data/", "research/pt-BR/"]:
    assert forbidden not in backlog, forbidden
assert "decision_refs:" not in backlog[backlog.index("  - id: PED-001"):backlog.index("  - id: AGENT-001")]

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
  identified: 514
  processed: 9
  discarded: 0
  blocked: 0
  verified: 35

domains:
  finalidade_e_escopo: verified
  fundamentos_educacionais: processing
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
  Primeiro lote de fundamentos educacionais concluído: nove fontes processadas.
  Evidências, taxonomias, perfis e recomendações sobre prática, formatos de
  resposta, tentativas, revelação, feedback, consequências e acessibilidade
  foram consolidados em cinco pendências, sem criar decisões ou defaults.

next_step: >-
  Processar o segundo lote de fundamentos educacionais: SRC-000321 a
  SRC-000324, SRC-000452, SRC-000457 e SRC-000458; consolidar progressão,
  sequenciamento, espaçamento, revisão, exemplos e scaffolding, mantendo
  recomendações e perfis como candidatos até aprovação explícita.
""",
    encoding="utf-8",
)

print("foundations_processed: 9")
print("remaining_foundations: 7")
print("public_backlog_items_verified: 5")
