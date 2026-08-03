# Backlog e fluxo de trabalho do ARA

**Estado:** documento operacional vigente  
**Idioma:** `pt-BR`  
**Última revisão:** 3 de agosto de 2026

## 1. Navegação e autoridade

1. `docs/vision/product-vision.pt-BR.md`;
2. `docs/research/research-programme-index.pt-BR.md`;
3. este documento.

Especificações aprovadas da fase prevalecem sobre ADRs, issues operacionais, sínteses, evidência, protótipos e conversas, nessa ordem. Fontes primárias prevalecem para afirmar o que ocorreu.

## 2. Caminho linear

```text
#3 evidência contínua
→ #4 taxonomia — concluída
→ #5 protocolos e analytics — concluída
→ #6 produto e domínio — atual
→ #7 arquitetura e ADRs
→ #8 UX/UI
→ #9 releases e backlog executável
→ implementação e avaliação
```

A Issue #2 corre em paralelo quando questões jurídicas e institucionais forem relevantes.

## 3. Estado das issues principais

| Issue | Fase | Estado | Saída |
|---|---:|---|---|
| #10 | 00 | aberta | roadmap e gates |
| #2 | 10 | paralela | propriedade intelectual, licença e identidade |
| #3 | 20 | contínua | evidência e atualização bibliográfica |
| #4 | 30 | concluída | `ara.configuration-taxonomy.v1` |
| #5 | 40 | concluída | `ara.research-framework.v1` |
| #6 | 50 | ativa | requisitos, atores, jornadas, entidades e estados |
| #7 | 60 | futura | arquitetura, perfis de implantação e ADRs |
| #8 | 70 | futura | jornadas, telas, acessibilidade e sistema visual |
| #9 | 80 | futura | releases, quality gates e issues executáveis |

## 4. Handoffs concluídos

### Issue #4

- 205 parâmetros canônicos;
- 38 perfis;
- camadas, precedência, aliases e snapshots;
- 36 candidatos adiados e 41 princípios rejeitados.

Manifesto: `research/data/issue4-final-artifact-manifest-v1.json`.

### Issue #5

- framework normativo de pergunta, protocolo, condição, assignment, evento, instrumento, evidência, medida, constructo e interpretação;
- 24 eventos mínimos autorizáveis;
- 16 medidas candidatas;
- 14 famílias de instrumentos;
- 15 regras de governança;
- 12 cenários validados.

Manifesto: `research/data/issue5-artifact-manifest-v1.json`.

Decisões permanentes:

- evento disponível não autoriza coleta;
- evento, medida, constructo, interpretação e intervenção permanecem separados;
- perfil pessoal é data-minimal;
- analytics pessoais, pedagógicos, de pesquisa e operacionais têm autoridades distintas;
- Caliper/xAPI e outros padrões são mapeamentos, não o domínio do ARA.

## 5. Trabalho atual — Issue #6

A Issue #6 deverá aceitar uma baseline normativa para:

- atores e jornadas;
- hierarquia educacional e composição;
- curso, microssequência, placement, card, resource, prática, resposta, validator e feedback;
- perfil, configuração efetiva, snapshot e capability;
- protocolo, condição, participante, assignment, evento, instrumento, medida, constructo e evidência;
- autoria, workspace, anotação, revisão, reparo, versão e publicação;
- biblioteca, pasta, referência, coleção, programa e catálogo;
- visibilidade, confidencialidade, licença, retenção, retirada e exclusão;
- estado local, sincronizado e publicado;
- importação, exportação, portabilidade e migração;
- classificação de capacidades core, opcionais, conectadas, experimentais e fora de escopo.

A hipótese de composição por microssequências deve receber decisão explícita. A Issue #6 não seleciona banco, framework, Storage ou interface.

## 6. Regras permanentes

- Pesquisa, decisão, produto, arquitetura, UX e implementação permanecem separados.
- Não há fallback, compatibilidade ou legado não documentado.
- Software tests não demonstram efetividade educacional.
- Um recurso tecnicamente possível não se torna requisito automaticamente.
- Issues de implementação para Codex devem apontar requisito, ADR, tela/jornada, aceite, testes, documentação e rollback.
- Mudanças em taxonomia ou framework de pesquisa criam nova versão; não reescrevem silenciosamente as fontes.

## 7. Experimentos e placeholders

#36–#40 permanecem não normativos; #42 permanece adiado. Issues #50 e #53 foram placeholders acidentais encerrados como `not_planned` e não autorizam trabalho.

## 8. Próxima ação

Executar e concluir a **Issue #6**. Somente depois iniciar #7.
