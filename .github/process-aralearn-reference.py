import base64
import json
import os
import urllib.error
import urllib.request

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
BRANCH = "consolidation-control"
TEMP_BRANCH = "consolidation-control-temp-should-not-use"
SELF_PATH = ".github/process-aralearn-reference.py"


def api(method, path, payload=None):
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
    try:
        with urllib.request.urlopen(request) as response:
            body = response.read()
            return json.loads(body) if body else None
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {error.code} {method} {path}: {body}") from error

# Confirm the operational materialization before cleanup.
status_obj = api("GET", f"/repos/{REPO}/contents/CONSOLIDATION_STATUS.yaml?ref={BRANCH}")
status_text = base64.b64decode(status_obj["content"]).decode("utf-8")
for expected in [
    "identified: 464", "processed: 11", "discarded: 1", "verified: 82",
    "MODEL-001", "MODEL-005",
]:
    assert expected in status_text, expected

# Delete only the accidental temporary branch.
api("DELETE", f"/repos/{REPO}/git/refs/heads/{TEMP_BRANCH}")
try:
    api("GET", f"/repos/{REPO}/git/ref/heads/{TEMP_BRANCH}")
    raise AssertionError("temporary branch still exists")
except RuntimeError as error:
    assert "GitHub API 404" in str(error), str(error)

final_status = '''corpus:
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
  Primeiro lote de modelo de conteúdo e recursos materializado: onze fontes
  relevantes processadas e um manifesto estrutural descartado. Cinco escolhas
  históricas do modelo permanecem registradas como MODEL-001 a MODEL-005 em
  pending_owner_approval, sem DEC-008 e sem autorização de implementação.
  Auditorias e cenários do corpus foram tratados como coerência conceitual, não
  como validação de factibilidade, usabilidade, acessibilidade com usuários ou
  efetividade educacional.

next_step: >-
  Processar o segundo lote de modelo de conteúdo e recursos: SRC-000238 a
  SRC-000246 e SRC-000364 a SRC-000369; avaliar os primeiros contratos
  experimentais, acessibilidade, segurança, comparação de quatro famílias,
  manifestos, instâncias, microssequências e validações, mantendo-os como
  evidência de protótipo e não como contratos aprovados.
'''

head = api("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}")["object"]["sha"]
commit = api("GET", f"/repos/{REPO}/git/commits/{head}")
status_blob = api("POST", f"/repos/{REPO}/git/blobs", {"content": final_status, "encoding": "utf-8"})["sha"]
new_tree = api("POST", f"/repos/{REPO}/git/trees", {
    "base_tree": commit["tree"]["sha"],
    "tree": [
        {"path": "CONSOLIDATION_STATUS.yaml", "mode": "100644", "type": "blob", "sha": status_blob},
        {"path": SELF_PATH, "mode": "100644", "type": "blob", "sha": None},
    ],
})["sha"]
new_commit = api("POST", f"/repos/{REPO}/git/commits", {
    "message": "chore: clear model batch operational blocker",
    "tree": new_tree,
    "parents": [head],
})["sha"]
api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {"sha": new_commit, "force": False})
print("temporary_branch_removed:", TEMP_BRANCH)
print("cleanup_commit:", new_commit)
