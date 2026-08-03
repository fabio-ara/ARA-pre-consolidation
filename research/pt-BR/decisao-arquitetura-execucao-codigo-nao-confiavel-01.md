# Decisão arquitetural provisória — execução de código não confiável

**Data local:** 3 de agosto de 2026  
**Issue:** #40  
**Estado:** decisão provisória de fronteiras; nenhuma tecnologia de isolamento selecionada

## 1. Problema

Uma atividade de programação pode precisar executar código produzido pelo estudante. “Executar” não é uma propriedade suficiente para declarar o runtime seguro, reproduzível ou adequado à avaliação.

A rodada anterior demonstrou funcionalmente:

- parsing;
- execução;
- testes;
- timeout;
- interrupção;
- limitação de saída;
- separação de testes públicos e protegidos.

Também mostrou que Web Worker e Node `vm` não constituem fronteiras produtivas contra código hostil.

## 2. Princípio

A ARA separará:

```text
code response
public validation
protected validation
execution service
isolation assurance
resource policy
diagnostic evidence
```

Um renderer ou editor de código não recebe autoridade implícita para executar. Um runtime funcional não recebe autoridade implícita para proteger o host.

## 3. Perfis de implantação

### 3.1 Cliente somente e offline

Pode oferecer execução local e testes públicos para estudo de baixo risco.

Não oferece:

- segredo dos testes;
- garantia contra código hostil;
- equivalência com a avaliação protegida;
- controle uniforme de memória entre navegadores.

A interface deve declarar `public-validation-only` e não apresentar o resultado como avaliação completa.

### 3.2 Host gerenciado e confiável

É o perfil candidato para testes protegidos. Requer jobs efêmeros com:

- isolamento revisto;
- imagem e pacotes versionados;
- rede desativada por padrão;
- base somente leitura;
- armazenamento temporário limitado;
- CPU, tempo, memória e saída limitados;
- cancelamento garantido;
- testes protegidos fora do curso;
- redação de diagnósticos;
- coleta mínima e governada de logs.

Container ou microVM são categorias de trabalho, não escolha desta rodada. A garantia depende da implementação e da operação.

### 3.3 Self-hosted conforme

Uma implantação própria pode:

- fornecer serviço de execução que passe os testes de conformidade; ou
- desativar a validação protegida.

Ela não pode substituir silenciosamente um requisito de host por um Worker e continuar declarando equivalência.

### 3.4 Ferramenta local de autor

Execução de código confiável pelo autor pertence a outro limite de confiança. Ela não deve compartilhar credenciais, permissões ou infraestrutura com a execução de código do estudante.

## 4. Testes públicos e protegidos

O curso pode carregar testes públicos. Testes protegidos devem ser referidos por identificador opaco de host:

```json
{
  "suiteId": "protected",
  "visibility": "protected",
  "hostReference": "protected-suite:example:v1"
}
```

O curso não contém o código, entradas ou respostas esperadas da suíte protegida.

Evidências devolvidas ao estudante devem informar critérios e diagnósticos úteis sem reconstruir material protegido.

## 5. Reprodutibilidade

Cada execução autoritativa deverá registrar:

- linguagem e versão;
- imagem ou pacote do runtime;
- digest;
- bibliotecas permitidas;
- limites aplicados;
- localização da validação;
- versão da suíte;
- política de evidência.

A resposta do estudante permanece independente do runtime.

## 6. Pyodide, Papyros e runtimes de navegador

Runtimes em navegador podem ser úteis para:

- feedback rápido;
- estudo offline após o download;
- visualização;
- testes públicos;
- ciência computacional local.

Eles não resolvem automaticamente:

- isolamento de código hostil;
- segredo de testes;
- limites rígidos de memória;
- governança de pacotes;
- abuso;
- equivalência entre dispositivos.

Por isso, sua eventual adoção será uma decisão de runtime e UX, não uma alegação de segurança.

## 7. Estado da decisão

Nesta rodada:

- Worker: rejeitado como sandbox produtiva;
- Node `vm`: rejeitado como sandbox produtiva;
- execução cliente: permitida apenas como perfil público e não protegido;
- validação protegida: exige host confiável;
- tecnologia de isolamento: não selecionada;
- custo operacional: ainda não estimado.

A arquitetura detalhada será consolidada depois de um threat model específico e da avaliação das opções de implantação.
