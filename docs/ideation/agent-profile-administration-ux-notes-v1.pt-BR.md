# Notas de UX — administração simples de perfis de agente

**Estado:** rascunho não normativo  
**Finalidade:** registrar como uma arquitetura internamente complexa pode permanecer compreensível para autores, professores, pesquisadores e administradores não especialistas.

## 1. Princípio

```text
configuração interna detalhada
→ poucas escolhas orientadas a tarefa
→ detalhes progressivos
```

O usuário comum não administra system prompts, embeddings, tools ou schemas diretamente. Ele escolhe finalidade, domínio, fontes e nível de autoridade; o ARA mostra o resultado efetivo e as consequências.

## 2. Superfície comum

Exemplo conceitual:

```text
Perfil do assistente

Finalidade
[ Construir conteúdo ]

Domínio
[ Redes de computadores ]

Público
[ Iniciante ]

Fontes
[ Bibliografia do curso ]
[ Documentação técnica aprovada ]

[ Testar ]  [ Aplicar ]
```

## 3. Superfície avançada

Disponível somente a papéis autorizados:

- instruções completas e fragments herdados;
- prompt templates e argumentos;
- knowledge collections e versões;
- regras de retrieval e contexto;
- tools/resources MCP e contratos;
- modelo/provider e parâmetros;
- eval suites e casos de regressão;
- diff entre versões;
- ativação, retirada e rollback.

## 4. Visualização de versão

Cada objeto versionado deve apresentar, em linguagem curta:

- versão ativa;
- autor e data;
- finalidade;
- onde é usado;
- o que mudou;
- resultados de teste;
- limitações;
- ação de comparar ou restaurar.

IDs, digests e detalhes internos ficam em “Detalhes”.

## 5. Recomendações produzidas por analytics

Uma recomendação deve indicar destinatário e natureza:

```text
Para o professor
Rever o uso de flow neste conjunto de cards.

Para o curador do perfil de domínio
Adicionar orientação sobre escalabilidade vertical e horizontal.

Para a equipe de resources
Investigar seleção acessível de arestas em graph.

Para o proprietário
Comparar a revisão 4 do perfil FGV com a revisão 3 em casos congelados.
```

O botão principal não deve aplicar a recomendação automaticamente. Ações candidatas:

- abrir evidências;
- criar proposta de revisão;
- encaminhar;
- rejeitar com motivo;
- adiar.

## 6. Papel do chat

O chat é adequado para:

- explicar resultados e alternativas;
- discutir uma recomendação;
- montar um plano de teste;
- analisar um corpus ou dataset autorizado;
- propor revisão de perfil;
- produzir relatório metodológico.

O ARA é adequado para:

- escolher objetos e versões;
- ver escopos e autoridade;
- comparar diffs;
- revisar evidências;
- ativar ou restaurar versões;
- acompanhar operações e decisões.

## 7. Restrições

- não mostrar catálogo inteiro de parâmetros por padrão;
- não usar “qualidade” como número único;
- não esconder modelo, dados ou configuração quando forem relevantes à interpretação;
- não apresentar recomendação da IA como decisão tomada;
- não misturar analytics de operação, aprendizagem e pesquisa na mesma tela;
- não expor dados individuais além da finalidade e papel autorizados.
