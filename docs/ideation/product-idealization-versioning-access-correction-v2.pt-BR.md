# Correção versionada da idealização — versionamento, acesso e lifecycle

**Estado:** addendum não normativo  
**Issue:** #81  
**Documento anterior:** `ara-product-idealization-v1.pt-BR.md`

Este documento substitui apenas as interpretações indicadas abaixo. O restante da idealização v1 permanece em discussão.

## 1. Lifecycle

Substituir a centralidade de `approved → published` por dimensões independentes:

```text
revisão
+ visibilidade
+ audiência
+ disponibilidade
+ versão atual
+ versão fixada
+ trajetória
```

Nenhum artefato é considerado definitivo. Uma revisão pode ser utilizada, compartilhada, fixada em pesquisa ou tornada atual e continuar aberta a evolução.

## 2. Permissões cotidianas

Substituir a hierarquia global de papéis como mecanismo principal de acesso por:

```text
autoria do nó
+ público | privado
+ pessoas/grupos de um privado
+ herança restritiva pelas derivações
```

Papéis continuam possíveis para responsabilidades administrativas, metodológicas e técnicas, mas não governam automaticamente o acesso cotidiano a todo conteúdo.

## 3. Regra de derivação

Uma derivação:

- herda o teto de audiência dos pais necessários;
- pode restringir a audiência;
- não pode ampliá-la;
- pode ser bloqueada por revogação em ancestral;
- permanece no grafo mesmo quando inacessível.

## 4. Autoria sem burocracia

O fluxo comum é:

```text
editar localmente
→ autosave
→ checkpoint automático
→ sync
→ revisão imutável
```

Confirmações ficam reservadas a efeitos realmente externos ou irreversíveis; não acompanham cada edição.

## 5. Restauração

Restauração é uma operação reversível que produz nova revisão. Caminhos posteriores permanecem como evidência e podem ser revisitados pelo usuário ou pelo GPT.

## 6. Grafo

O grafo de versões é superfície legítima do produto para autoria, curadoria e pesquisa. Não precisa ser escondido sob uma história linear obrigatória.

## 7. Armazenamento

O conteúdo versionado é candidato a artifact storage imutável. O banco mantém metadata, relações, refs, acesso efetivo e índices. IndexedDB mantém trabalho local e materialização offline.

## 8. Fontes externas

O ARA não armazena automaticamente livros, normas, PDFs ou outros materiais usados como ancoragem. O escopo deste modelo são os artefatos gerados no ARA.

## 9. Pesquisa

O histórico pode ser consultado:

- longitudinalmente, pela trajetória de um artefato;
- transversalmente, por observações, branches, grupos e condições;
- conjuntamente, para investigar padrões, causas possíveis e efeitos de reparos.
