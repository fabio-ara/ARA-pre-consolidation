import base64
import json
import os
import urllib.request

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
BRANCH = "consolidation-control"
PUBLIC_REPO = "fabio-ara/ARA"
SCRIPT_PATH = ".github/process-aralearn-reference.py"
WORKFLOW_PATH = ".github/workflows/process-aralearn-reference.yml"


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
assert counts_before == {"verified": 82, "processed": 11, "discarded": 1, "identified": 464}, counts_before

updates = {
    "SRC-000238": ("processed", True, "BACKLOG.yaml", "Matriz de acessibilidade e segurança para quatro famílias de componentes. Sustenta PED-004, EXP-009 e INF-001 ao exigir alternativas por operação, limites conhecidos e fronteiras explícitas; afirmações permanecem requisitos candidatos aguardando protótipos de interação e avaliação com usuários."),
    "SRC-000239": ("processed", True, "BACKLOG.yaml", "Registro de dez emendas aceitas no protótipo v0.2. Na consolidação atual, são recomendações técnicas: autoridade separada de localização, estado derivado descartável, disponibilidade explícita, evidência protegida e limites de recursos, sem promoção a decisão do produto."),
    "SRC-000240": ("processed", True, "BACKLOG.yaml", "Comparação entre matemática semântica, construção relacional, programação executável e argumento com fontes. Demonstra que um envelope compartilhado pode coexistir com gramáticas e critérios irredutíveis; conteúdo deduplicado em MODEL-003 e EXP-008."),
    "SRC-000241": ("discarded", False, None, "Manifesto estrutural com caminhos, tamanhos e hashes do primeiro protótipo. Os artefatos substantivos estão inventariados individualmente; nenhum conteúdo intelectual exclusivo a preservar."),
    "SRC-000242": ("processed", True, "BACKLOG.yaml", "Resumo do primeiro protótipo: quatro famílias, envelope comum e 19 verificações estruturais sem falhas. Regras de autoridade e próximos trabalhos foram preservados como evidência de protótipo em MODEL-003, EXP-008, EXP-009, PED-004 e INF-001, sem seleção tecnológica."),
    "SRC-000243": ("discarded", False, None, "Manifesto estrutural da versão 0.2 com caminhos, tamanhos e hashes. Os artefatos substantivos estão inventariados individualmente; nenhum conteúdo intelectual exclusivo a preservar."),
    "SRC-000244": ("processed", True, "BACKLOG.yaml", "Resumo da revisão v0.2: dez emendas, verificações estruturais e testes de fronteira sem falhas, mas execução real das bibliotecas externas ainda pendente. A distinção entre validação pública no cliente e validação protegida em ambiente confiável permanece recomendação, não arquitetura aprovada."),
    "SRC-000245": ("processed", True, "BACKLOG.yaml", "Relatório de validação v0.2: 15 verificações de esquema, seis testes de contrato e quatro testes de fronteira passaram; bibliotecas externas não foram executadas. Conformidade não demonstra efetividade educacional, segurança de produção nem acessibilidade, conforme EXP-010."),
    "SRC-000246": ("processed", True, "BACKLOG.yaml", "Relatório do primeiro protótipo com 19 verificações estruturais sem falhas. Declara explicitamente ausência de renderizadores, validadores e runtime de produção e necessidade de validação de acessibilidade e semântica cruzada; tratado como evidência limitada, não resultado de produto."),
    "SRC-000364": ("processed", True, "BACKLOG.yaml", "Documento do protótipo por primeiros princípios. Define finalidade experimental, envelope estreito e quatro famílias contrastantes, além de limites normativos do experimento; confirma MODEL-003, EXP-008 e EXP-009 sem importar esquemas anteriores nem selecionar stack."),
    "SRC-000365": ("processed", True, "BACKLOG.yaml", "Quatro instâncias completas de componentes mostram representação, atividade, resposta, validação, retorno, execução, segurança, acessibilidade e funcionamento offline combinados de maneiras diferentes. São artefatos de prova de conceito, não contratos vigentes nem evidência educacional."),
    "SRC-000366": ("processed", True, "BACKLOG.yaml", "Quatro manifestos experimentais registram autoridade de protótipo, capacidades, runtime, segurança, acessibilidade, funcionamento offline, localização e proveniência. Usados como evidência para EXP-009; valores e pacotes exemplificativos não foram promovidos a requisitos."),
    "SRC-000367": ("processed", True, "BACKLOG.yaml", "Quatro microssequências experimentais demonstram composição de teoria, prática guiada e prática independente em domínios distintos. A estrutura exemplifica composição e apoio instrucional, mas não estabelece sequência pedagógica universal; deduplicada em MODEL-001 e PED-009."),
    "SRC-000368": ("processed", True, "BACKLOG.yaml", "Cenários experimentais distinguem entrada inválida, satisfação parcial, erro de execução, correção e revisão humana, preservando autoridade por critério. Sustenta MODEL-003 e PED-001/PED-003 sem autorizar políticas universais de pontuação ou avaliação."),
    "SRC-000369": ("processed", True, "BACKLOG.yaml", "Esquema comum experimental para proveniência, acessibilidade, funcionamento offline, runtime, segurança, resultados de critérios e retorno pedagógico. Serve como evidência de que um envelope compartilhado é representável; não é contrato aprovado nem ontologia universal."),
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
assert counts_after == {"verified": 82, "processed": 24, "discarded": 3, "identified": 449}, counts_after

backlog = get_text(PUBLIC_REPO, "BACKLOG.yaml", "main")
for item_id in ["MODEL-003", "EXP-002", "EXP-008", "EXP-009", "EXP-010", "PED-004", "INF-001"]:
    assert backlog.count(f"  - id: {item_id}\n") == 1, item_id
assert "DEC-008" not in get_text(PUBLIC_REPO, "DECISOES.md", "main")
for forbidden in ["ARA-pre-consolidation", "consolidation-control", "SOURCE_INVENTORY", "SRC-000"]:
    assert forbidden not in backlog, forbidden

next_batch = [f"SRC-{i:06d}" for i in range(370, 377)]
for source_id in next_batch:
    r = by_id[source_id]
    assert r["domain"] == "modelo de conteúdo e recursos", (source_id, r["domain"])
    assert r["status"] == "identified", (source_id, r["status"])

new_inventory = "\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in records) + "\n"
new_status = '''corpus:
  branch: main
  commit: d5f83c1fdb2047de0080510540d2b911aec3cd8b
  cutoff: "2026-08-06T00:32:00-03:00"

phase: processing

counts:
  total: 558
  identified: 449
  processed: 24
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
  Segundo lote de modelo de conteúdo e recursos concluído: treze fontes de contratos
  e protótipos processadas e dois manifestos estruturais descartados. A conformidade
  de esquemas e fronteiras conceituais em quatro famílias foi preservada como evidência
  de protótipo, sem seleção de tecnologia, contrato aprovado, segurança de produção,
  acessibilidade validada com usuários ou alegação de efetividade educacional. O
  conteúdo foi deduplicado contra pendências públicas existentes, sem alteração do
  repositório público.

next_step: >-
  Processar o terceiro lote de modelo de conteúdo e recursos: SRC-000370 a
  SRC-000376; concluir os esquemas específicos e o validador do primeiro protótipo,
  separando contrato experimental, gramática de domínio e resultado de validação
  estrutural. Não iniciar ainda os artefatos da versão 0.2.
'''

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
    "message": "chore: process component contract prototype batch",
    "tree": new_tree,
    "parents": [head],
})["sha"]
api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {"sha": new_commit, "force": False})

print("processed:", 13)
print("discarded:", 2)
print("next_batch:", len(next_batch))
print("commit:", new_commit)
