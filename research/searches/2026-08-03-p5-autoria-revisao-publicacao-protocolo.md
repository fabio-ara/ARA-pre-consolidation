# Protocolo focado P5 — autoria, revisão, auditoria, reparo, publicação e políticas institucionais

**Issue governante:** #4  
**Pacote:** P5  
**Data:** 3 de agosto de 2026  
**Estado:** protocolo concluído para a primeira taxonomia; não autoriza implementação.

## 1. Pergunta decisória

Como o ARA deve organizar autoria humano–IA, busca e composição de microssequências, contexto autorizado, revisão, comentários, reparo, versões, proveniência, publicação, permissões, compartilhamento, retirada e exclusão sem reduzir o controle humano, sem ocultar responsabilidade e sem sobrecarregar GPT ou usuário?

## 2. Decisões que o pacote informa

O P5 informa:

- parâmetros de autoria, revisão, auditoria, reparo, versionamento, reutilização, publicação, licenciamento e governança;
- perfis pessoais, colaborativos, acadêmicos, institucionais, abertos, confidenciais e offline;
- separação de papéis, estados e autoridades;
- handoff para protocolos/analytics (#5), produto/domínio (#6), arquitetura (#7) e UX (#8).

Não decide schema, API, banco, Storage, contrato MCP, interface ou stack.

## 3. Handoffs recebidos

### P1

- feedback e revelação não equivalem a aprovação;
- consequência e autoridade precisam ser explícitas;
- respostas abertas e avaliação automática autoritativa permanecem limitadas.

### P2

- sequência, progressão, exemplos e scaffolds exigem snapshots e autoria versionada;
- conclusão estrutural não é mastery;
- mudanças de apoio e sequência alteram a condição pedagógica.

### P3

- IA é assistente delimitado;
- propostas de IA usam `preview-only` ou `recommend-and-confirm`;
- ciclo `suggestion → draft → validated-structure → audited → human-approved → published`;
- contexto, grounding, provider/model, provenance, editabilidade, contestação e fallback precisam ser explícitos;
- chat/MCP e ARA são canais complementares.

### P4

- finalidade, protocolo, condição, evento, medida, constructo, interpretação e decisão não se confundem;
- versões, diffs e provenance sustentam comparabilidade;
- papéis, acesso, retenção e exportação são governados;
- logs operacionais não substituem evidência educacional.

### Hipóteses transversais

- microssequência versionada como candidata a unidade autoral/reutilizável;
- curso como composição versionada de ocorrências contextuais;
- materialização offline autossuficiente;
- estado associado ao contexto do curso/versão/posição/card;
- perfis e overrides esparsos;
- administração por linguagem pedagógica;
- cursos derivados com invariantes e diffs explícitos.

## 4. Estratos de evidência

A amostragem foi organizada em oito estratos:

1. **AraLearn implementado:** planejamento, construção em partes, auditoria independente, reparo localizado, reauditoria, revisions, readiness e publicação explícita;
2. **autoria humano–IA e mixed initiative:** coautoria, divisão de papéis, supervisão, confiança e overreliance;
3. **avaliação e revisão de conteúdo gerado por IA:** quality assurance, rubricas, revisão humana e limitações de LLM reviewers;
4. **workflows editoriais e de software:** review requests, CODEOWNERS, branch protection, separation of duties e publication gates;
5. **objetos educacionais e reutilização:** OER, H5P, content libraries, referências, forks, adaptação e contextualização;
6. **provenance, anotações e autenticidade:** PROV-O, Web Annotation, C2PA, autoria e contribuição;
7. **licenciamento, confidencialidade e lifecycle:** Creative Commons, acesso, withdrawal, deletion e preservação de versões;
8. **administração não técnica e contextos institucionais:** professores, tutores, pesquisadores, workspaces, papéis, permissões e progressive disclosure.

## 5. Fontes e estratégia de busca

Foram priorizadas:

- documentação oficial de padrões e plataformas;
- código e documentação do AraLearn como fonte primária implementada;
- revisões, estudos empíricos e sistemas acadêmicos com workflows descritos;
- orientações institucionais reconhecidas;
- casos contrastantes, inclusive resultados negativos e riscos.

Buscas temáticas incluíram combinações de:

```text
human AI coauthoring education workflow review repair publication provenance
AI generated educational content human review quality assurance
mixed initiative authoring intelligent tutoring content authoring
Open Educational Resources reuse remix provenance licensing
learning object repository reusable learning units versioning
educational content library reuse fork publish workflow
W3C PROV Web Annotation educational content provenance
C2PA content credentials provenance generative AI education
GitHub pull request review CODEOWNERS branch protection publication workflow
LLM as reviewer educational content bias reliability human oversight
```

## 6. Critérios de inclusão

Incluiu-se uma fonte quando contribuía para pelo menos uma decisão sobre:

- estado, função ou autoridade de autoria;
- revisão, auditoria, aprovação ou publicação;
- provenance, grounding ou atribuição;
- reutilização, fork, adaptação ou propagação;
- comentários/anotações e resolução;
- versionamento, diff, rollback, retirada ou exclusão;
- roles, permissions, confidentiality ou separation of duties;
- administração compreensível para autores não técnicos.

## 7. Critérios de exclusão

- listas genéricas de boas práticas de prompt sem método;
- marketing de ferramenta sem documentação operacional;
- sistemas sem workflow verificável;
- opiniões sobre autoria por IA sem implicação decisória;
- propostas de arquitetura prematuras;
- fontes que apenas afirmam eficiência sem governança ou avaliação.

## 8. Estado de acesso

Cada registro indica acesso como:

- texto integral ou artigo aberto;
- documentação oficial;
- código/schema primário;
- resumo/metadados;
- fonte secundária;
- acesso limitado.

Limitações de acesso permanecem explícitas e impedem alegações metodológicas detalhadas.

## 9. Critério de suficiência

A amostragem foi considerada suficiente para a primeira taxonomia quando:

1. todos os estratos continham fonte central e caso contrastante;
2. as adições finais não criaram nova família decisória;
3. benefícios de IA estavam acompanhados de riscos e limites;
4. o fluxo implementado do AraLearn foi confrontado com workflows externos;
5. questões arquiteturais permaneceram separadas;
6. incertezas capazes de mudar decisões foram registradas.

Suficiência significa capacidade de definir a taxonomia inicial, não prova de efetividade universal.

## 10. Método de síntese

1. Extrair capacidade, risco ou obrigação.
2. Separar comportamento implementado, evidência, hipótese e decisão.
3. Formular dimensões independentes.
4. Registrar relação com AraLearn.
5. Comparar autoridade, escopo e precedência.
6. Definir incompatibilidades e inferências proibidas.
7. Montar perfis contrastantes.
8. Classificar aceitos, adiados e rejeitados.
9. Produzir handoffs sem converter achado em arquitetura.

## 11. Cenários de validação

A taxonomia P5 foi verificada contra:

- autoria manual pessoal;
- autoria pessoal assistida por IA;
- construção por GPT+MCP em partes com ARA em tempo real;
- auditoria independente e reparo localizado;
- curso com microssequência reutilizada por referência;
- fork contextualizado sem propagação silenciosa;
- estudo comparativo com condição bloqueada;
- publicação aberta de OER;
- conteúdo institucional confidencial;
- revisão por especialista externo;
- revisão de acessibilidade;
- operação offline com capacidades indisponíveis;
- retirada de compartilhamento e preservação de snapshot;
- conflito entre autor, revisor, instituição e protocolo.

## 12. Limitações

- a literatura de autoria educacional com LLM muda rapidamente;
- muitos sistemas descrevem geração, mas não lifecycle completo;
- workflows editoriais e de software exigem adaptação ao contexto pedagógico;
- padrões de provenance não resolvem validade, qualidade ou licenciamento automaticamente;
- granularidade ótima de reutilização permanece questão de #6;
- persistência, sincronização e revogação offline pertencem a #7;
- interface e terminologia exigem pesquisa com usuários em #8;
- contextos brasileiros, portugueses e não WEIRD permanecem sub-representados.

## 13. Não autorizações

Este pacote não autoriza:

- MCP ou API de produção;
- schema, banco, Storage ou IndexedDB;
- automação integral de autoria ou publicação;
- LLM como autoridade final;
- reuse ou repair automáticos entre cursos;
- propagação silenciosa de mudanças;
- curso/microssequência como contrato técnico definitivo;
- UI, dashboard, workflow executável ou código;
- tratamento de dados pessoais ou conteúdo confidencial;
- abertura de nova issue automática.

## 14. Entregas

- corpus estruturado;
- parâmetros estruturados;
- perfis comparativos;
- síntese decisória em JSON;
- síntese crítica em `pt-BR`;
- bibliografia focada;
- atualização dos documentos canônicos.
