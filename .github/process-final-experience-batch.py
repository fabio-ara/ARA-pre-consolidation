import base64
import json
import os
import urllib.request

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
BRANCH = "consolidation-control"


def api(method, path, payload=None):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
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
    with urllib.request.urlopen(req) as resp:
        body = resp.read()
        return json.loads(body) if body else None


def get_text(path):
    obj = api("GET", f"/repos/{REPO}/contents/{path}?ref={BRANCH}")
    return base64.b64decode(obj["content"]).decode("utf-8")

records = [json.loads(line) for line in get_text("SOURCE_INVENTORY.jsonl").splitlines()]
assert len(records) == 558
assert [r["id"] for r in records] == [f"SRC-{i:06d}" for i in range(1, 559)]
assert len({r["locator"] for r in records}) == 558

counts = {}
for r in records:
    counts[r["status"]] = counts.get(r["status"], 0) + 1
assert counts == {"verified": 82, "processed": 24, "discarded": 3, "identified": 449}, counts

updates = {
    "SRC-000370": "Esquema experimental de manifesto de componente. Torna explícitas autoridade, referências de esquema, capacidades, requisitos de execução, segurança, acessibilidade, funcionamento offline, localização e proveniência; demonstra representabilidade do contrato, não aprovação do contrato nem dos valores enumerados.",
    "SRC-000371": "Esquema experimental de programação executável. Separa espaço de código, atividade, resposta, cadeia de validade, testes públicos e protegidos e autoridade determinística; o esquema declara fronteiras de execução, mas não implementa nem valida isolamento ou segurança de produção.",
    "SRC-000372": "Esquema experimental de microssequência com papéis de teoria, prática guiada e prática independente, além de dependências e apoio instrucional. A exigência desses três papéis pertence ao protótipo e não foi promovida a sequência pedagógica universal; conteúdo já coberto por MODEL-001, PED-007 e PED-009.",
    "SRC-000373": "Esquema experimental de construção relacional. Mantém estado semântico de nós e relações separado de geometria derivada, registra operações e predicados determinísticos; verificações como unicidade semântica e existência de endpoints exigem validação além do JSON Schema.",
    "SRC-000374": "Esquema experimental de matemática semântica. Representa árvore de expressão, entrada original, validade e testes de propriedades com prévia de interpretação; a autoridade determinística é especificada como contrato candidato, não como validador matemático implementado ou validado.",
    "SRC-000375": "Esquema experimental de anotação e argumentação com fontes. Usa versões identificadas por digest, seletores, anotações, relações argumentativas, verificações determinísticas de integridade e revisão humana final; assistência probabilística é não final. Não valida qualidade de rubricas ou revisão humana.",
    "SRC-000376": "Script reprodutível que carrega os esquemas e valida quatro manifestos, quatro instâncias, quatro microssequências e sete resultados de validação. Comprova conformidade estrutural dos 19 documentos de exemplo, não execução dos runtimes, restrições semânticas cruzadas, acessibilidade, segurança ou efetividade educacional.",
}
by_id = {r["id"]: r for r in records}
for sid, notes in updates.items():
    r = by_id[sid]
    assert r["domain"] == "modelo de conteúdo e recursos"
    assert r["status"] == "identified"
    r.update(status="processed", relevant=True, destination="BACKLOG.yaml", notes=notes)

counts = {}
for r in records:
    counts[r["status"]] = counts.get(r["status"], 0) + 1
assert counts == {"verified": 82, "processed": 31, "discarded": 3, "identified": 442}, counts
for i in range(377, 387):
    r = by_id[f"SRC-{i:06d}"]
    assert r["domain"] == "modelo de conteúdo e recursos" and r["status"] == "identified"

new_inventory = "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in records) + "\n"
new_status = '''corpus:
  branch: main
  commit: d5f83c1fdb2047de0080510540d2b911aec3cd8b
  cutoff: "2026-08-06T00:32:00-03:00"

phase: processing

counts:
  total: 558
  identified: 442
  processed: 31
  discarded: 3
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
  Terceiro lote de modelo de conteúdo e recursos concluído: sete fontes do primeiro
  protótipo processadas. Manifesto, microssequência, gramáticas específicas e script
  de validação foram preservados como evidência de contrato experimental. A validação
  registrada comprova somente conformidade estrutural dos documentos de exemplo e
  não execução de runtime, segurança de produção, acessibilidade com usuários,
  validade de revisão humana ou efetividade educacional. Nenhuma decisão nova foi criada.

next_step: >-
  Processar o primeiro lote da versão 0.2 do protótipo de componentes: SRC-000377 a
  SRC-000386; examinar README, quatro instâncias, quatro manifestos e cenários de
  validação, comparando as mudanças com o protótipo 0.1 sem tratar migração, campos
  adicionais, bibliotecas externas ou políticas de execução como contratos aprovados.
'''

head = api("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}")["object"]["sha"]
commit = api("GET", f"/repos/{REPO}/git/commits/{head}")
base_tree = commit["tree"]["sha"]
inv_blob = api("POST", f"/repos/{REPO}/git/blobs", {"content": new_inventory, "encoding": "utf-8"})["sha"]
status_blob = api("POST", f"/repos/{REPO}/git/blobs", {"content": new_status, "encoding": "utf-8"})["sha"]
cleanup = [
    ".github/process-final-experience-batch.py",
    ".github/workflows/process-final-experience-batch.yml",
    ".github/process-cross-domain-benchmark.py",
    ".github/process-foundations-2.py",
    ".github/workflows/process-foundations-2.yml",
]
tree_items = [
    {"path": "SOURCE_INVENTORY.jsonl", "mode": "100644", "type": "blob", "sha": inv_blob},
    {"path": "CONSOLIDATION_STATUS.yaml", "mode": "100644", "type": "blob", "sha": status_blob},
]
for path in cleanup:
    tree_items.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
new_tree = api("POST", f"/repos/{REPO}/git/trees", {"base_tree": base_tree, "tree": tree_items})["sha"]
new_commit = api("POST", f"/repos/{REPO}/git/commits", {"message": "chore: process first prototype schemas batch", "tree": new_tree, "parents": [head]})["sha"]
api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {"sha": new_commit, "force": False})
print(new_commit)
