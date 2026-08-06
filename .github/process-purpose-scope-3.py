import json
from pathlib import Path

inventory_path = Path("SOURCE_INVENTORY.jsonl")
records = [json.loads(line) for line in inventory_path.read_text(encoding="utf-8").splitlines()]

assert len(records) == 558
assert [record["id"] for record in records] == [f"SRC-{index:06d}" for index in range(1, 559)]
assert len({record["locator"] for record in records}) == 558

updates = {
    "SRC-000138": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Idealização ampla e não normativa decomposta seletivamente. Pendências únicas de escopo foram registradas como SCOPE-004, SCOPE-005, SCOPE-006 e VAL-001; propostas específicas de outros domínios não foram duplicadas porque possuem fontes próprias no inventário.",
    ),
    "SRC-000144": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Pré-backlog humano usado para identificar questões únicas. Somente limites do produto, vocabulário, cenários, revisão de candidatos e corpus representativo foram preservados neste domínio; os demais temas seguem para fontes específicas, sem promoção em bloco.",
    ),
    "SRC-000212": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Recomendação não normativa de extensibilidade governada preservada como SCOPE-005; incertezas capazes de alterar o recorte foram registradas como RES-003. Alternativas continuam abertas.",
    ),
    "SRC-000213": (
        "discarded",
        False,
        None,
        "Registro de candidatos substituído pela versão corrigida SRC-000214; nenhum conteúdo útil residual exclusivo.",
    ),
    "SRC-000214": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Candidatos corrigidos de agentes, observações e análise assistida consolidados como AGENT-001, sem aprovação de objetos, ferramentas, métricas ou métodos específicos.",
    ),
    "SRC-000215": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Registro estruturado usado para deduplicar o pré-backlog amplo. Pendências únicas de finalidade e escopo foram preservadas; propostas dos demais domínios não foram copiadas antecipadamente.",
    ),
    "SRC-000216": (
        "discarded",
        False,
        None,
        "Manifesto intermediário substituído por versão posterior; regra de não executabilidade e evolução aditiva já preservada nas fontes vigentes.",
    ),
    "SRC-000217": (
        "discarded",
        False,
        None,
        "Manifesto intermediário substituído por versão posterior; nenhum conteúdo atual exclusivo após deduplicação.",
    ),
    "SRC-000218": (
        "discarded",
        False,
        None,
        "Manifesto intermediário substituído por versão posterior; nenhum conteúdo atual exclusivo após deduplicação.",
    ),
    "SRC-000219": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Manifesto mais recente confirma que os candidatos são não executáveis e dependem de evidência e decisão. Contagens e união de versões não foram promovidas; conteúdos de versionamento e acesso seguem para suas fontes específicas.",
    ),
    "SRC-000224": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Limitações e entradas de revisão preservadas como SCOPE-006, VAL-001 e RES-003. Resultados declarados como auditoria de rascunho não foram tratados como validação do produto.",
    ),
    "SRC-000225": (
        "discarded",
        False,
        None,
        "Manifesto estrutural duplicado pelos documentos, registros e auditoria inventariados individualmente; nenhum conteúdo intelectual residual exclusivo.",
    ),
    "SRC-000226": (
        "processed",
        True,
        "BACKLOG.yaml",
        "Categorias de procedência, autoridade, escopo e data de acesso preservadas como RES-002, incluindo revalidação obrigatória de informações temporais instáveis.",
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
assert counts == {"processed": 24, "discarded": 11, "identified": 523}, counts
assert not [
    record for record in records
    if record["domain"] == "finalidade e escopo" and record["status"] == "identified"
]

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
  identified: 523
  processed: 24
  discarded: 11
  blocked: 0
  verified: 0

domains:
  finalidade_e_escopo: pending_audit
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
  Primeiro lote de pré-backlogs e manifestos concluído: oito fontes processadas
  e cinco versões ou estruturas sem conteúdo residual descartadas. Sete
  pendências únicas foram registradas no backlog público, sem promover
  contagens, propostas agregadas ou alternativas a decisões.

next_step: >-
  Auditar o domínio finalidade e escopo: conferir as 35 fontes classificadas,
  a coerência entre README.md, BACKLOG.yaml, DECISOES.md, METODO_DE_TRABALHO.md
  e LICENSE, a ausência de referências privadas e o registro completo das
  pendências; depois marcar o domínio como verificado ou registrar correções.
""",
    encoding="utf-8",
)

print("control_updated: 24 processed, 11 discarded, 523 identified")
print("purpose_scope_remaining_identified: 0")
