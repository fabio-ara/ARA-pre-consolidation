import json
from pathlib import Path

inventory_path = Path("SOURCE_INVENTORY.jsonl")
records = [json.loads(line) for line in inventory_path.read_text(encoding="utf-8").splitlines()]

assert len(records) == 558
assert [record["id"] for record in records] == [f"SRC-{index:06d}" for index in range(1, 559)]
assert len({record["locator"] for record in records}) == 558
assert sum(record["locator"].startswith("git:") for record in records) == 385
assert sum(record["locator"].startswith("github:issue/") for record in records) == 45
assert sum(record["locator"].startswith("github:pull/") for record in records) == 40
assert sum(record["locator"].startswith("github:conversation-comment/") for record in records) == 81
assert sum(record["locator"].startswith("github:pull-review/") for record in records) == 4
assert sum(record["type"] in {"comment_collection", "review_collection", "attachment_collection"} for record in records) == 3

updates = {
    "SRC-000001": ("discarded", False, None, "Versão em inglês duplicada pela versão pt-BR; nenhum conteúdo substantivo adicional."),
    "SRC-000002": ("processed", True, "README.md; BACKLOG.yaml; DECISOES.md", "Fonte principal em pt-BR para tese do produto, estágio de pré-desenvolvimento e gate de implementação."),
    "SRC-000003": ("discarded", False, None, "Versão pt-PT duplicada pela versão pt-BR; nenhum conteúdo substantivo adicional."),
    "SRC-000013": ("processed", True, "BACKLOG.yaml", "Índice não normativo usado para separar propostas, alternativas e itens candidatos de decisões confirmadas; nenhum pré-backlog foi promovido em bloco."),
    "SRC-000024": ("processed", True, "README.md; BACKLOG.yaml; DECISOES.md", "Confirma que o planejamento de implementação é fase futura e depende de autorização explícita."),
    "SRC-000025": ("processed", True, "README.md; BACKLOG.yaml; DECISOES.md", "Confirma tese de continuidade funcional, distinção de escopos e autoridade do gate de implementação."),
    "SRC-000081": ("processed", True, "README.md; BACKLOG.yaml; DECISOES.md", "Sustenta o enquadramento canônico; detalhes do processo e referências históricas não foram transferidos."),
    "SRC-000083": ("processed", True, "METODO_DE_TRABALHO.md", "Confirma navegação enxuta, fonte canônica única e eliminação de duplicação sem perda de rastreabilidade; já representado no método público."),
    "SRC-000093": ("processed", True, "BACKLOG.yaml; DECISOES.md", "Programa de implementação posteriormente superado. Somente a necessidade de gate explícito foi preservada; releases e itens executáveis não foram transferidos."),
    "SRC-000094": ("processed", True, "README.md; BACKLOG.yaml; DECISOES.md", "Correção explícita que restaura o estágio de pré-desenvolvimento e retira autoridade do programa prematuro."),
    "SRC-000095": ("processed", True, "BACKLOG.yaml", "Idealização não normativa. Limites e caráter candidato foram preservados; alternativas técnicas e pré-backlog permanecem para lotes futuros."),
    "SRC-000126": ("processed", True, "README.md; BACKLOG.yaml; DECISOES.md", "Baseline normativo que confirma resultados centrais, continuidade funcional, offline e controle humano; detalhes de domínio seguem para lote próprio."),
    "SRC-000129": ("processed", True, "README.md; BACKLOG.yaml; DECISOES.md", "Confirma pré-desenvolvimento, distinção de escopos e ausência de autorização de implementação; alternativas técnicas não foram promovidas."),
    "SRC-000134": ("processed", True, "README.md; BACKLOG.yaml; DECISOES.md", "Visão canônica usada para a definição pública do produto; apenas elementos estáveis de finalidade e escopo foram incorporados."),
}

by_id = {record["id"]: record for record in records}
for source_id, (status, relevant, destination, notes) in updates.items():
    record = by_id[source_id]
    assert record["status"] == "identified"
    record["status"] = status
    record["relevant"] = relevant
    record["destination"] = destination
    record["notes"] = notes

state_counts = {}
for record in records:
    state_counts[record["status"]] = state_counts.get(record["status"], 0) + 1
assert state_counts == {"processed": 12, "discarded": 2, "identified": 544}

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
  identified: 544
  processed: 12
  discarded: 2
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
  Cobertura integral verificada contra 385 blobs, 45 issues, 40 pull requests,
  86 comentários gerais e quatro revisões formais. Primeiro lote substantivo
  de finalidade e escopo concluído: 12 fontes processadas e duas duplicações
  linguísticas descartadas. Tese de produto, pré-desenvolvimento e gate de
  implementação materializados no repositório público.

next_step: >-
  Processar o segundo lote de finalidade e escopo: SRC-000007, SRC-000041 a
  SRC-000043, SRC-000119 a SRC-000121 e SRC-000451; separar licenciamento,
  política linguística, artefatos superados e síntese de enquadramento antes
  de tratar os pré-backlogs e manifestos candidatos.
""",
    encoding="utf-8",
)

print("coverage_verified: 385 blobs, 45 issues, 40 pull requests, 86 comments, 4 reviews")
print("control_updated: 12 processed, 2 discarded, 544 identified")
