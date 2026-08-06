require "json"
require "yaml"
require "net/http"
require "uri"
require "base64"
require "set"

TOKEN = ENV.fetch("GITHUB_TOKEN")
PUBLIC_REPO = "fabio-ara/ARA"


def assert(condition, message)
  raise message unless condition
end


def api(path)
  uri = URI("https://api.github.com#{path}")
  request = Net::HTTP::Get.new(uri)
  request["Authorization"] = "Bearer #{TOKEN}"
  request["Accept"] = "application/vnd.github+json"
  request["X-GitHub-Api-Version"] = "2022-11-28"
  response = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|
    http.request(request)
  end
  raise "GitHub API #{response.code}: #{path}" unless response.is_a?(Net::HTTPSuccess)
  JSON.parse(response.body)
end


def public_file(path)
  encoded = URI.encode_www_form_component(path).gsub("%2F", "/")
  object = api("/repos/#{PUBLIC_REPO}/contents/#{encoded}?ref=main")
  Base64.decode64(object.fetch("content"))
end

inventory_path = "SOURCE_INVENTORY.jsonl"
records = File.readlines(inventory_path, chomp: true).map { |line| JSON.parse(line) }

assert(records.length == 558, "inventário deve ter 558 registros")
expected_ids = (1..558).map { |index| format("SRC-%06d", index) }
assert(records.map { |record| record.fetch("id") } == expected_ids, "IDs fora de sequência")
assert(records.map { |record| record.fetch("locator") }.uniq.length == 558, "localizadores duplicados")

purpose = records.select { |record| record.fetch("domain") == "finalidade e escopo" }
assert(purpose.length == 35, "domínio finalidade e escopo deve ter 35 fontes")
status_counts = purpose.tally { |record| record.fetch("status") }
assert(status_counts == {"processed" => 24, "discarded" => 11}, "estados prévios inesperados: #{status_counts}")

purpose.each do |record|
  assert(!record.fetch("notes").to_s.strip.empty?, "fonte sem justificativa: #{record.fetch("id")}")
  if record.fetch("relevant") == true
    assert(!record.fetch("destination").to_s.strip.empty?, "fonte relevante sem destino: #{record.fetch("id")}")
  else
    assert(record.fetch("relevant") == false, "relevância não resolvida: #{record.fetch("id")}")
    assert(record["destination"].nil?, "fonte descartada com destino: #{record.fetch("id")}")
  end
end

root = api("/repos/#{PUBLIC_REPO}/contents?ref=main")
root_names = root.map { |entry| entry.fetch("name") }.sort
expected_root = ["BACKLOG.yaml", "DECISOES.md", "LICENSE", "METODO_DE_TRABALHO.md", "README.md"].sort
assert(root_names == expected_root, "raiz pública inesperada: #{root_names}")

texts = expected_root.to_h { |path| [path, public_file(path)] }

forbidden = [
  "ARA-pre-consolidation",
  "consolidation-control",
  "SOURCE_INVENTORY",
  "CONSOLIDATION_STATUS",
  "PROTOCOLO_CONSOLIDACAO_ARA",
  "SRC-000",
  "github:issue/",
  "github:pull/",
  "docs/ideation/",
  "research/data/",
  "research/pt-BR/"
]

texts.each do |path, text|
  forbidden.each do |term|
    assert(!text.include?(term), "referência privada ou antiga em #{path}: #{term}")
  end
  assert(!text.include?("—"), "travessão encontrado em #{path}")
end

issues = api("/repos/#{PUBLIC_REPO}/issues?state=all&per_page=100")
issues.each do |issue|
  combined = [issue["title"], issue["body"]].compact.join("\n")
  forbidden.each do |term|
    assert(!combined.include?(term), "referência privada em issue pública: #{term}")
  end
end

backlog = YAML.safe_load(texts.fetch("BACKLOG.yaml"), aliases: false)
states = backlog.fetch("states")
items = backlog.fetch("items")
assert(backlog.fetch("language") == "pt-BR", "idioma canônico incorreto")
assert(backlog.fetch("source_of_truth") == true, "backlog não marcado como fonte canônica")
assert(items.map { |item| item.fetch("id") }.uniq.length == items.length, "IDs duplicados no backlog")
items.each do |item|
  assert(states.include?(item.fetch("status")), "estado inválido em #{item.fetch("id")}")
end

approved = items.select { |item| item.fetch("status") == "approved" }
approved.each do |item|
  assert(item["decision_refs"].is_a?(Array) && !item["decision_refs"].empty?, "item aprovado sem decisão: #{item.fetch("id")}")
  assert(item["acceptance_criteria"].is_a?(Array) && !item["acceptance_criteria"].empty?, "item aprovado sem critérios: #{item.fetch("id")}")
end
items.reject { |item| item.fetch("status") == "approved" }.each do |item|
  assert(!item.key?("decision_refs"), "pendência com decisão vinculada: #{item.fetch("id")}")
end

decision_ids = texts.fetch("DECISOES.md").scan(/^## (DEC-\d{3}) - /).flatten
backlog_refs = approved.flat_map { |item| item.fetch("decision_refs") }
assert(decision_ids.to_set == backlog_refs.to_set, "decisões e referências do backlog divergem")
assert(decision_ids.length == 7 && decision_ids.uniq.length == 7, "registro de decisões deve conter sete decisões únicas")

expected_statuses = {
  "GOV-001" => "approved",
  "LANG-001" => "approved",
  "LANG-002" => "captured",
  "SCOPE-001" => "approved",
  "SCOPE-002" => "approved",
  "SCOPE-003" => "captured",
  "SCOPE-004" => "captured",
  "SCOPE-005" => "pending_research",
  "SCOPE-006" => "captured",
  "AGENT-001" => "captured",
  "RES-002" => "captured",
  "RES-003" => "pending_research",
  "VAL-001" => "captured"
}
items_by_id = items.to_h { |item| [item.fetch("id"), item] }
expected_statuses.each do |id, status|
  assert(items_by_id.fetch(id).fetch("status") == status, "estado incorreto em #{id}")
end

readme = texts.fetch("README.md")
assert(readme.include?("## Visão integral do produto"), "README não distingue visão integral")
assert(readme.include?("não constituem autorização para implementação"), "README não explicita limite de autorização")
assert(!readme.include?("A direção confirmada inclui"), "README ainda mistura visão e decisão")
["METODO_DE_TRABALHO.md", "BACKLOG.yaml", "DECISOES.md", "LICENSE"].each do |linked|
  assert(readme.include?(linked), "README não referencia #{linked}")
end

method = texts.fetch("METODO_DE_TRABALHO.md")
assert(method.include?("Ideia, problema, evidência, hipótese, alternativa, recomendação, decisão, requisito, implementação e validação são categorias distintas."), "método não preserva categorias")
assert(method.include?("Visão de produto, recorte de implementação, avaliação acadêmica e adoção institucional são escopos distintos."), "método não preserva escopos")

scope_six = items_by_id.fetch("SCOPE-006")
assert(!scope_six.fetch("summary").include?("idealização existente"), "SCOPE-006 ainda depende de artefato ausente")
assert(scope_six.fetch("summary").include?("repositório público"), "SCOPE-006 não explicita autonomia pública")

license = texts.fetch("LICENSE")
assert(license.include?("SPDX-License-Identifier: AGPL-3.0-or-later"), "licença pública divergente")

purpose.each { |record| record["status"] = "verified" }
final_counts = records.tally { |record| record.fetch("status") }
assert(final_counts == {"verified" => 35, "identified" => 523}, "contagens finais inesperadas: #{final_counts}")

File.write(
  inventory_path,
  records.map { |record| JSON.generate(record) }.join("\n") + "\n",
  mode: "w",
  encoding: "UTF-8"
)

File.write(
  "CONSOLIDATION_STATUS.yaml",
  <<~YAML,
    corpus:
      branch: main
      commit: d5f83c1fdb2047de0080510540d2b911aec3cd8b
      cutoff: "2026-08-06T00:32:00-03:00"

    phase: processing

    counts:
      total: 558
      identified: 523
      processed: 0
      discarded: 0
      blocked: 0
      verified: 35

    domains:
      finalidade_e_escopo: verified
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
      Auditoria do domínio finalidade e escopo concluída sobre 35 fontes. A visão
      integral foi distinguida de decisões aprovadas no README e SCOPE-006 foi
      reescrito para não depender de artefato ausente do repositório público.
      Backlog, decisões, método e licença estão consistentes; referências privadas
      ou antigas não foram encontradas nos arquivos canônicos nem nas issues públicas.

    next_step: >-
      Processar o primeiro lote de fundamentos educacionais: SRC-000028,
      SRC-000067, SRC-000317 a SRC-000320, SRC-000351, SRC-000456 e
      SRC-000467; consolidar prática, formatos de resposta, tentativas, reveal,
      feedback e consequências sem promover recomendações a decisões.
  YAML
  mode: "w",
  encoding: "UTF-8"
)

puts "purpose_scope_verified: 35"
puts "public_canonical_files_verified: 5"
puts "private_references_found: 0"
