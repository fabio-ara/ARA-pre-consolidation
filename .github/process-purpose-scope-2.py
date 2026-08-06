import json
from pathlib import Path

inventory_path = Path("SOURCE_INVENTORY.jsonl")
records = [json.loads(line) for line in inventory_path.read_text(encoding="utf-8").splitlines()]

assert len(records) == 558
assert [record["id"] for record in records] == [f"SRC-{index:06d}" for index in range(1, 559)]
assert len({record["locator"] for record in records}) == 558

updates = {
    "SRC-000007": (
        "processed",
        True,
        "LICENSE; README.md",
        "Confirma AGPL-3.0-or-later. O repositório público já registra o identificador da licença e remete ao texto oficial; nenhuma nova decisão foi necessária.",
    ),
    "SRC-000041": (
        "discarded",
        False,
        None,
        "Placeholder acidental, encerrado como não planejado, sem requisito, decisão, pendência ou artefato substantivo.",
    ),
    "SRC-000042": (
        "discarded",
        False,
        None,
        "Placeholder acidental, encerrado como não planejado, sem requisito, decisão, pendência ou artefato substantivo.",
    ),
    "SRC-000043": (
        "processed",
        True,
        "BACKLOG.yaml; DECISOES.md",
        "Gate administrativo prematuro e explicitamente superado. Somente o gate conceitual vigente de DEC-007 e SCOPE-002 foi preservado; branch protection e programa de releases não orientam o estágio atual.",
    ),
    "SRC-000119": (
        "discarded",
        False,
        None,
        "Versão em inglês duplicada pela versão pt-BR. Não é fonte canônica conforme DEC-002.",
    ),
    "SRC-000120": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Política parcialmente relevante. A proposta de documentação canônica multilíngue e engenharia documental em inglês conflita com DEC-002 e não foi transferida. Questões futuras de interface, jurisdição e metadados foram preservadas como LANG-002, no estado captured.",
    ),
    "SRC-000121": (
        "discarded",
        False,
        None,
        "Versão pt-PT duplicada pela versão pt-BR e não canônica conforme DEC-002.",
    ),
    "SRC-000451": (
        "processed",
        True,
        "README.md; BACKLOG.yaml",
        "Síntese exploratória que sustenta não reduzir o ARA a uma plataforma de flashcards. O gênero proposto permanece hipótese descritiva e foi preservado como SCOPE-003, no estado captured, sem alegação de efetividade.",
    ),
}

by_id = {record["id"]: record for record in records}
for source_id, (status, relevant, destination, notes) in updates.items():
    record = by_id[source_id]
    assert record["status"] == "identified", (source_id, record["status"])
    record["status"] = status
    record["relevant"] = relevant
    record["destination"] = destination
    record["notes"] = notes

counts = {}
for record in records:
    counts[record["status"]] = counts.get(record["status"], 0) + 1
assert counts == {"processed": 16, "discarded": 6, "identified": 536}, counts

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
  identified: 536
  processed: 16
  discarded: 6
  blocked: 0
  verified: 0

domains:
  finalidade_e_escopo: processing
  fundamentos_educacionais: identified
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
  Segundo lote de finalidade e escopo concluído: licença confirmada, dois
  placeholders acidentais descartados, gate administrativo superado separado
  do gate conceitual vigente, política linguística reconciliada com DEC-002 e
  hipótese de gênero preservada sem promoção a decisão. Quatro fontes foram
  processadas e quatro descartadas.

next_step: >-
  Processar o primeiro lote de pré-backlogs e manifestos candidatos de
  finalidade e escopo: SRC-000138, SRC-000144, SRC-000212 a SRC-000219 e
  SRC-000224 a SRC-000226; preservar somente itens únicos e questões abertas,
  sem promover contagens ou propostas em bloco ao backlog canônico.
""",
    encoding="utf-8",
)

print("control_updated: 16 processed, 6 discarded, 536 identified")
