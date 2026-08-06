import base64
import json
import os
import urllib.request

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
BRANCH = "consolidation-control"
PUBLIC_REPO = "fabio-ara/ARA"
SCRIPT_PATH = ".github/process-model-domain-1.py"
WORKFLOW_PATH = ".github/workflows/process-foundations-1.yml"


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
assert [r["id"] for r in records] == [f"SRC-{i:06d}" for i in range(1, 559)]
assert len({r["locator"] for r in records}) == 558

counts_before = {}
for r in records:
    counts_before[r["status"]] = counts_before.get(r["status"], 0) + 1
assert counts_before == {"verified": 82, "identified": 476}, counts_before

updates = {
    "SRC-000021": ("processed", True, "BACKLOG.yaml", "Issue de produto que exige consolidar requisitos e modelo de domínio sem derivá-los automaticamente de protótipos ou sistemas comparados. As escolhas internas foram preservadas como candidatos MODEL-001 a MODEL-005, não como decisões vigentes."),
    "SRC-000090": ("processed", True, "BACKLOG.yaml", "Pull request historicamente aceito como handoff normativo no corpus. Suas escolhas de unidade reutilizável, ocorrência contextual, relações tipadas, separação de responsabilidades e estado contextual foram registradas como pendentes de aprovação do responsável pelo projeto."),
    "SRC-000125": ("processed", True, "BACKLOG.yaml", "Artefato de modelo de domínio que reúne identidade, revisão, composição, estado, configuração, pesquisa, organização e capacidades. Somente distinções próprias deste domínio foram consolidadas agora; conteúdos de versionamento, dados, acesso e infraestrutura seguem para seus domínios."),
    "SRC-000297": ("discarded", False, None, "Manifesto estrutural que apenas enumera arquivos e contagens do pacote Issue 6. O conteúdo intelectual está preservado nas fontes inventariadas individualmente; nenhum residual exclusivo."),
    "SRC-000298": ("processed", True, "BACKLOG.yaml", "Auditoria conceitual sem bloqueadores. O resultado confirma coerência interna do pacote, mas declara explicitamente que não valida factibilidade de implementação, usabilidade ou efetividade educacional; limitações preservadas no tratamento do lote."),
    "SRC-000299": ("processed", True, "BACKLOG.yaml", "Classificação de capacidades usada como evidência de escopo e alternativas. Classes, horizontes de release e proibições do corpus não foram promovidos a decisões; conteúdos correlatos permanecem em SCOPE-005, EXP-009, INF-001 e demais domínios."),
    "SRC-000300": ("processed", True, "BACKLOG.yaml", "Síntese explicitamente classificada no corpus como decisão normativa anterior. Na consolidação atual, as cinco escolhas próprias do modelo foram preservadas como MODEL-001 a MODEL-005 em pending_owner_approval, sem criar DEC-008 nem autorizar implementação."),
    "SRC-000301": ("processed", True, "BACKLOG.yaml", "Registro de 65 entidades usado seletivamente. Não foi copiado como ontologia pública; serviu para sustentar identidade de curso e microssequência, ocorrência contextual, separação entre recurso/prática/resposta/validação/retorno e organização por referências."),
    "SRC-000302": ("processed", True, "BACKLOG.yaml", "Registro de 24 invariantes. Invariantes próprios do modelo foram incorporados aos candidatos MODEL; regras de direitos, pesquisa, sincronização, licenças e infraestrutura foram deixadas para os domínios correspondentes."),
    "SRC-000303": ("processed", True, "BACKLOG.yaml", "Registro de 15 jornadas usado para conferir consequências dos candidatos em estudo pessoal, autoria, pesquisa, publicação, reutilização e uso offline. Jornadas não foram promovidas em bloco a requisitos."),
    "SRC-000304": ("processed", True, "BACKLOG.yaml", "Validação conceitual de 16 cenários usada como teste de coerência dos candidatos. Estado passed significa resolução interna do modelo, não resultado validado de implementação, usabilidade, acessibilidade com usuários ou aprendizagem."),
    "SRC-000305": ("processed", True, "BACKLOG.yaml", "Máquinas de estado candidatas para revisão, publicação, anotação, reparo, sincronização, pesquisa e capacidades. Não foram adotadas como contratos vigentes; estados específicos serão tratados nos domínios de versionamento, autoria, dados, sincronização e UX."),
}

by_id = {r["id"]: r for r in records}
for source_id, (status, relevant, destination, notes) in updates.items():
    r = by_id[source_id]
    assert r["domain"] == "modelo de conteúdo e recursos", (source_id, r["domain"])
    assert r["status"] == "identified", (source_id, r["status"])
    r["status"] = status
    r["relevant"] = relevant
    r["destination"] = destination
    r["notes"] = notes

counts_after = {}
for r in records:
    counts_after[r["status"]] = counts_after.get(r["status"], 0) + 1
assert counts_after == {"verified": 82, "processed": 11, "discarded": 1, "identified": 464}, counts_after

backlog = get_text(PUBLIC_REPO, "BACKLOG.yaml", "main")
for n in range(1, 6):
    item_id = f"MODEL-{n:03d}"
    needle = f"  - id: {item_id}\n"
    assert backlog.count(needle) == 1, item_id
    start = backlog.index(needle)
    next_start = backlog.find("\n  - id: ", start + len(needle))
    section = backlog[start:] if next_start == -1 else backlog[start:next_start]
    assert "status: pending_owner_approval" in section, item_id
    assert "decision_refs:" not in section, item_id
assert "DEC-008" not in get_text(PUBLIC_REPO, "DECISOES.md", "main")
for forbidden in ["ARA-pre-consolidation", "consolidation-control", "SOURCE_INVENTORY", "SRC-000"]:
    assert forbidden not in backlog, forbidden

next_batch = ["SRC-000045", "SRC-000047", "SRC-000148"] + [f"SRC-{i:06d}" for i in range(238, 247)] + ["SRC-000448", "SRC-000449", "SRC-000462"]
assert len(next_batch) == 15
for source_id in next_batch:
    r = by_id[source_id]
    assert r["domain"] == "modelo de conteúdo e recursos", (source_id, r["domain"])
    assert r["status"] == "identified", (source_id, r["status"])

new_inventory = "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in records) + "\n"
new_status = """corpus:
  branch: main
  commit: d5f83c1fdb2047de0080510540d2b911aec3cd8b
  cutoff: "2026-08-06T00:32:00-03:00"

phase: processing

counts:
  total: 558
  identified: 464
  processed: 11
  discarded: 1
  blocked: 0
  verified: 82

domains:
  finalidade_e_escopo: verified
  fundamentos_educacionais: verified
  experiencias_e_sistemas_analisados: verified
  modelo_de_conteudo_e_recursos: processing
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
pending_decisions:
  - MODEL-001
  - MODEL-002
  - MODEL-003
  - MODEL-004
  - MODEL-005

last_batch: >-
  Primeiro lote de modelo de conteúdo e recursos concluído: onze fontes processadas
  e um manifesto estrutural descartado. Cinco escolhas que o corpus tratava como
  normativas foram preservadas como MODEL-001 a MODEL-005 em pending_owner_approval,
  sem criar nova decisão, contrato de implementação ou seleção tecnológica.

next_step: >-
  Processar o segundo lote de modelo de conteúdo e recursos: SRC-000045,
  SRC-000047, SRC-000148, SRC-000238 a SRC-000246, SRC-000448, SRC-000449 e
  SRC-000462; consolidar modularidade, contratos de componentes, acessibilidade,
  segurança, migração e validação dos protótipos, distinguindo evidência de
  protótipo, recomendação e requisito aprovado antes de tratar os arquivos
  executáveis dos protótipos em lote separado.
"""

head = api("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}")["object"]["sha"]
commit = api("GET", f"/repos/{REPO}/git/commits/{head}")
base_tree = commit["tree"]["sha"]

inventory_blob = api("POST", f"/repos/{REPO}/git/blobs", {"content": new_inventory, "encoding": "utf-8"})["sha"]
status_blob = api("POST", f"/repos/{REPO}/git/blobs", {"content": new_status, "encoding": "utf-8"})["sha"]
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
    "message": "chore: process first content model batch",
    "tree": new_tree,
    "parents": [head],
})["sha"]
api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {"sha": new_commit, "force": False})

print("model_sources_processed: 11")
print("model_sources_discarded: 1")
print("pending_owner_approval: 5")
print("next_batch: 15")
print("commit:", new_commit)
