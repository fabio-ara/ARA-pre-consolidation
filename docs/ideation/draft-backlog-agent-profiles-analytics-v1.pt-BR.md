# Extensão do pré-backlog — perfis de agente, curadoria participativa e analytics

**Estado:** candidato para discussão; não executável  
**Relação:** nova área Q do pré-backlog do ARA  
**Issue de pesquisa:** #77  
**Regra:** nenhum item autoriza código, coleta de participantes ou ativação autônoma de configurações.

## Como esta extensão integra o pré-backlog

O pré-backlog versionado passa a ser lido como:

```text
Áreas A–P
`docs/ideation/draft-backlog-v1.pt-BR.md`
+ Área Q
este documento
→ pré-backlog v2 para discussão
```

Os 171 itens anteriores permanecem preservados. Esta extensão acrescenta 26 itens, totalizando **197 itens candidatos em 17 áreas**. A união é registrada em `research/data/ara-draft-backlog-v2-manifest.json`.

---

## Q. Perfis modulares de agente, curadoria participativa e analytics assistidos por IA

### Q01 — Inventário da configuração monolítica do AraLearn

**Resultado candidato:** mapa verificável entre instruções do GPT, knowledge atual, papéis, prompts implícitos, tools MCP, resources/contratos, políticas de contexto, providers e fluxos de autoria/auditoria.  
**Herança:** extração da configuração funcional do predecessor, sem presumir que a divisão física atual seja normativa.  
**Decisão necessária:** o que pertence à base comum, ao domínio, à tarefa, ao contexto, ao MCP ou ao produto.

### Q02 — AgentProfile e versões

Definir uma identidade administrativa para configurações reutilizáveis e revisões imutáveis que possam ser comparadas, ativadas, retiradas e restauradas.

### Q03 — Papéis e subpapéis do agente

Representar planejador, construtor, auditor, reparador, reauditor, curador de fontes, avaliador de configurações, analista quantitativo, analista qualitativo e pesquisador-assistente sem exigir GPTs independentes.

### Q04 — Perfis de domínio

Configurações versionadas para domínios e práticas como programação, matemática, redes, línguas, análise de fontes, procedimentos administrativos e bancas de concurso. Devem permanecer separadas dos parâmetros pedagógicos do curso.

### Q05 — Coleções de conhecimento versionadas

Definir fontes, versões, proveniência, licença, validade, acesso, índices derivados, atualização e retenção de coleções recuperáveis pelo agente.

### Q06 — Templates de tarefa versionados

Modelar roteiros parametrizados para planejamento, construção, auditoria, reparo e análise, com argumentos, exemplos, contraexemplos, testes e histórico.

### Q07 — Fronteira entre prompts, resources e tools MCP

Definir o que é instrução reutilizável, contexto recuperável, operação executável, contrato de conteúdo e objeto do domínio ARA. A terminologia técnica não deve ser exposta obrigatoriamente ao autor comum.

### Q08 — Políticas de contexto e escopo de escrita

Separar, por operação:

- contexto integral;
- contexto indexado ou resumido;
- conteúdo omitido;
- objetos autorizados para mutação;
- objetos apenas legíveis.

O escopo inicial deve cobrir card, microssequência e lição. Não se recomenda assistência estrutural acima de lição enquanto a maior unidade criável for a microssequência.

### Q09 — Snapshot efetivo da configuração do agente

Persistir, em cada operação, modelo/provider, instruções, perfis, templates, knowledge snapshots, tools/resources/contracts, parâmetros, contexto, evals e autoridade.

### Q10 — Evals e corpus de regressão

Criar casos reais e sintéticos, rubricas, resultados esperados, repetição de execuções e comparação entre configurações. Um único score não decide ativação.

### Q11 — Administração em linguagem simples

Superfície para selecionar finalidade, domínio, público, fontes e versão; testar, comparar, encaminhar e ativar sem editar código. Detalhes avançados permanecem progressivos.

### Q12 — Lifecycle de configuração

Rascunho, em avaliação, recomendado, ativo, retirado e restaurado; toda ativação exige autoridade explícita, evidência e rollback.

### Q13 — Proveniência e diff da operação do agente

Registrar o que foi lido, o que podia ser alterado, o que mudou e por quê. Diffs devem separar conteúdo, composição, parâmetros, configuração do agente, knowledge/retrieval, tools/contracts e efeitos técnicos ou pedagógicos possíveis.

### Q14 — Corpus versionado de observações

Congelar conjuntos de observações por alvo e revisão, preservando autor/papel ou pseudônimo autorizado, finalidade, evidência, visibilidade, relações e uso permitido.

### Q15 — Síntese argumentativa de observações

Agrupar duplicações, convergências, conflitos, evidências e contraexemplos sem tratar quantidade, extensão textual ou eloquência como verdade. Preservar contribuições minoritárias e incerteza.

### Q16 — Ciclo observação → finding → reparo → reauditoria

Transformar sínteses em findings auditáveis; propor reparo; gerar diff; auditar regressões; registrar decisão humana e nova revisão.

### Q17 — Taxonomia de falhas do agente

Distinguir problemas de:

- instrução/template;
- knowledge ou fonte;
- retrieval/contexto;
- tool/permissão;
- contrato JSON/schema;
- modelo/provider;
- resource/practice/renderer;
- parâmetro pedagógico;
- conteúdo-fonte ou decisão humana.

### Q18 — Analytics de autoria, agente e sistema

Responder quais configurações, resources e fluxos concentram falhas, reparos e regressões. Resultados operacionais não podem ser convertidos automaticamente em conclusões educacionais.

### Q19 — Encaminhamento de recomendações

Direcionar recomendações, com evidência e natureza explícitas, para professor, curador de domínio, proprietário, pesquisador ou equipe de desenvolvimento de resources/contracts.

### Q20 — Workbench quantitativo de pesquisa

Protocolos, condições, grupos, atribuição, métricas, instrumentos, datasets congelados, estatísticas descritivas, tamanhos de efeito, incerteza, pressupostos, missingness, attrition, fidelity e análises de sensibilidade.

### Q21 — Workbench qualitativo

Corpus autorizado, codebooks, codificação assistida, temas, evidências, divergências, memos, reflexividade, comparação entre analistas e preservação do contexto original.

### Q22 — Integração de métodos mistos

Representar integração explícita entre evidência quantitativa e qualitativa, temporalidade, unidades de análise, matrizes conjuntas, convergências, divergências e explicações concorrentes.

### Q23 — ResearchAnalysisRun reproduzível

Cada análise deve registrar protocolo, dataset, plano, configuração do agente, código, ambiente, outputs brutos e validados, pressupostos, decisões humanas, limitações e conclusões permitidas/proibidas.

### Q24 — GPT como pesquisador-assistente

Auxiliar desenho, plano de análise, execução verificável, interpretação, explicações concorrentes e ensino de metodologia. O GPT não é autoridade científica, não aprova seu próprio resultado e não substitui revisão metodológica.

### Q25 — Direitos, privacidade e governança analítica

Purpose binding, consentimento quando aplicável, minimização, pseudonimização, acesso, provider boundary, retenção, exportação, retirada e proibição de reutilização silenciosa de dados operacionais como dados de pesquisa.

### Q26 — Ensaio de continuidade AraLearn → configuração modular

Reproduzir jornadas reais do AraLearn com uma composição modular equivalente e comparar cobertura, validade JSON, reparos, contexto, custo, estabilidade e compreensão. A modularização falha se piorar silenciosamente o fluxo funcional já validado.

---

## Dependências e sequência de investigação

1. concluir Q01 e selecionar fixtures reais;
2. definir Q02–Q09 em documentos e exemplos fechados;
3. construir Q10 antes de recomendar perfis especializados;
4. validar continuidade por Q26;
5. aprofundar Q14–Q19 com cenários participativos;
6. aprofundar Q20–Q25 por desenhos de pesquisa prioritários;
7. revisar requisitos, domínio, arquitetura e UX antes de qualquer implementação.

## Critério de promoção futura

Um item desta área somente poderá virar issue de implementação quando possuir:

- problema e público explícitos;
- evidência e alternativas;
- objeto, autoridade e lifecycle definidos;
- dados de entrada e saída;
- contexto de leitura e escopo de escrita;
- interface e consequências compreensíveis;
- privacidade, segurança e retenção;
- evals, aceite, rollback e limitações;
- relação verificável com o AraLearn funcional.
