# Ledger de decisões — discussão posterior à PR #80

**Estado:** registro interpretativo para revisão do proprietário  
**Período:** da integração da PR #80 até a abertura da Issue #81  
**Regra:** “aceito” significa afirmado pelo proprietário ou não contestado após formulação explícita; não autoriza implementação.

## Aceito ou incorporado

1. O versionamento é requisito central do ARA.
2. A finalidade principal do histórico é permitir trabalho rápido e reversível, não impor cerimônia.
3. A edição direta deve salvar primeiro no IndexedDB e sincronizar quando houver conexão.
4. Autosaves locais, checkpoints automáticos e revisões duráveis são camadas diferentes.
5. Restaurar uma versão cria uma nova revisão; não apaga versões posteriores.
6. O histórico pode e deve formar um grafo quando surgem derivações.
7. O grafo pode ser apresentado diretamente na interface e seus nós podem ser clicáveis.
8. Cursos, microssequências e cards permanecem provisórios; “publicação” não é endpoint central.
9. A microssequência é a principal candidata a unidade de coerência e contexto.
10. Cards podem ser unidades menores de versão e deduplicação.
11. Resources podem possuir identidade quando isso trouxer valor.
12. O GPT pode investigar a trajetória de um artefato verticalmente.
13. O GPT pode agregar observações e derivações horizontalmente.
14. A combinação das duas análises pode orientar reparos e evolução.
15. Guardar o histórico não significa enviá-lo integralmente ao modelo.
16. A interface cotidiana deve evitar mensagens, aprovações e confirmações repetidas.
17. A colaboração ocorre por derivações e grafo, sem alteração destrutiva do nó alheio.
18. O modelo cotidiano de visibilidade possui apenas público e privado.
19. Privado admite uma lista simples de pessoas ou grupos.
20. Derivação não pode conceder acesso mais amplo do que recebeu.
21. O acesso efetivo depende do nó, dos pais necessários e dos contêineres.
22. Revogação no ancestral pode retirar acesso ao descendente, inclusive de seu autor.
23. A revogação não apaga o nó nem a trajetória.
24. O autor do ancestral necessário conserva autoridade sobre sua disponibilidade.
25. O ARA não armazena, por padrão, as fontes externas usadas para gerar o curso.
26. O ARA armazena os artefatos gerados e a proveniência interna entre eles.
27. O conteúdo versionado deve residir prioritariamente no Storage/object store.
28. O banco guarda metadata, relações, refs, operações, observações e projeções.
29. O backend precisa ser compatível com implantação pública e institucional.
30. Pesquisa educacional precisa fixar versões, condições e políticas de acesso.

## Rejeitado ou substituído

1. Publicação como estado final ou sinal de que o curso está pronto.
2. Um sistema cotidiano baseado em papéis globais como admin, autor e estudante.
3. Uma matriz geral de permissões exposta ao usuário comum.
4. Aprovação ou confirmação para cada alteração.
5. Apagar versões posteriores quando se restaura uma versão antiga.
6. Ocultar obrigatoriamente o grafo para simplificar a interface.
7. Proibir tecnicamente toda derivação interna para manter uma linha estrita.
8. Conceder ao autor do descendente acesso independente do ancestral.
9. Permitir que um descendente amplie a audiência herdada.
10. Transformar o ARA em repositório das fontes de estudo.
11. Perguntar rotineiramente sobre proveniência e direitos de cada fonte importada.
12. Usar fixtures equivalentes do AraLearn para uma arquitetura que ele não possui.
13. Event sourcing integral como pressuposto de todo o produto.
14. Dependência obrigatória de Git verdadeiro ou versionamento nativo do bucket.

## Em aberto

1. Regras exatas de checkpoint automático.
2. Retenção do diário local e dos checkpoints transitórios.
3. Granularidade física final dos JSONs.
4. Merge entre duas ou mais derivações.
5. Conteúdo mínimo exibido em nós bloqueados.
6. Atualização de acesso quando grupos mudam.
7. Snapshot de acesso para pesquisa versus política corrente.
8. Escala e cache da interseção de audiências.
9. Retenção e garbage collection de descendentes bloqueados.
10. Biblioteca de grafo para o front-end.
11. BaaS e arquitetura de deployment.
12. Procedimentos excepcionais de privacidade, segurança ou ordem legal.
