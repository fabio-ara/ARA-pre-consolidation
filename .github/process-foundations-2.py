import base64
import json
import os
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


inventory_path = Path("SOURCE_INVENTORY.jsonl")
records = [json.loads(line) for line in inventory_path.read_text(encoding="utf-8").splitlines()]
assert len(records) == 558
assert [record["id"] for record in records] == [f"SRC-{index:06d}" for index in range(1, 559)]
assert len({record["locator"] for record in records}) == 558

before = {}
for record in records:
    before[record["status"]] = before.get(record["status"], 0) + 1
assert before == {"verified": 35, "processed": 9, "identified": 514}, before

updates = {
    "SRC-000321": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Síntese decisória de pesquisa do pacote P2. Progressão, sequência, revisão, exemplos, scaffolding, segmentação e retomada foram preservados em PED-006 a PED-009; recomendações, perfis e parâmetros continuam não normativos.",
    ),
    "SRC-000322": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Corpus de evidências que sustenta decompor progressão, ritmo, revisão e apoio, bem como rejeitar limiar, algoritmo de espaçamento, intercalação ou fading universais.",
    ),
    "SRC-000323": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Registro estruturado de 36 dimensões candidatas. Foi consolidado seletivamente em PED-006 a PED-009, sem adotar contratos, valores, precedências ou mecanismos adaptativos.",
    ),
    "SRC-000324": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Comparação de perfis e sobreposições usada para registrar alternativas em PED-006 a PED-009. Nenhum perfil foi promovido a default ou decisão pública.",
    ),
    "SRC-000452": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Inventário curricular usado somente como orientação de temas, métodos e bibliografias. Sua natureza e limitações foram preservadas em PED-011; presença em unidade curricular não foi tratada como evidência de eficácia nem requisito.",
    ),
    "SRC-000457": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Síntese crítica principal do pacote P2, consolidada em PED-006 a PED-009. Shared control, spacing, exemplos e retomada permanecem recomendações ou famílias de pesquisa, não implementação autorizada.",
    ),
    "SRC-000458": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Síntese P3 usada, neste domínio, para preservar autonomia apoiada, adaptação explícita e assistência por inteligência artificial em PED-010. Detalhes de autoria, dados, arquitetura e UX seguem para seus domínios próprios.",
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
assert after == {"verified": 35, "processed": 16, "identified": 507}, after

remaining = [
    record["id"]
    for record in records
    if record["domain"] == "fundamentos educacionais" and record["status"] == "identified"
]
assert remaining == [], remaining

public = api(f"/repos/{PUBLIC_REPO}/contents/BACKLOG.yaml?ref=main")
backlog = base64.b64decode(public["content"]).decode("utf-8")
for item_id in ["PED-006", "PED-007", "PED-008", "PED-009", "PED-010", "PED-011"]:
    assert backlog.count(f"  - id: {item_id}\n") == 1, item_id
segment = backlog[backlog.index("  - id: PED-006"):backlog.index("  - id: AGENT-001")]
assert "decision_refs:" not in segment
for forbidden in ["ARA-pre-consolidation", "consolidation-control", "SRC-000", "research/data/", "research/pt-BR/"]:
    assert forbidden not in backlog, forbidden

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
  processed: 16
  discarded: 0
  blocked: 0
  verified: 35

domains:
  finalidade_e_escopo: verified
  fundamentos_educacionais: pending_audit
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
  Segundo lote de fundamentos educacionais concluído: sete fontes processadas.
  Progressão e domínio, sequência e ritmo, revisão e intercalação, exemplos e
  retomada, autonomia e adaptação, assistência por inteligência artificial e
  orientação curricular foram consolidados em seis pendências sem decisões.

next_step: >-
  Auditar o domínio fundamentos educacionais: conferir as 16 fontes processadas,
  a coerência de PED-001 a PED-011, a separação entre evidência, recomendação e
  decisão, a ausência de defaults universais ou referências privadas e a cobertura
  das limitações; depois marcar o domínio como verificado ou registrar correções.
""",
    encoding="utf-8",
)

print("foundations_processed_total: 16")
print("remaining_foundations: 0")
print("public_backlog_items_verified: 6")
