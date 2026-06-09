# Prompt de continuidade — Volume XVI (Terminal & Bash), Caps 1–22 — para Claude Code

Cole este conteúdo no Claude Code para produzir o **Volume XVI — Terminal & Bash** da coleção FullStack Manual. Leia também o `CLAUDE.md` na raiz — ele tem as convenções gerais da coleção.

---

## Contexto

Estou construindo a **FullStack Manual**: coleção de 17 manuais de referência fullstack em **português do Brasil**, cada um um arquivo HTML único e autocontido, com tema *dark warm*, syntax highlighting customizado e navegação estruturada. Hospedados em `https://vitormattosdev.github.io/FullStack-Manual/`.

Os Volumes XIV (Git) e XV (Docker) estão completos. O **Volume XVI — Terminal & Bash** continua a **Onda 4 — Ferramentas do ofício**: do empacotamento do ambiente (Docker) ao domínio do shell que o opera.

## Arquivo de trabalho

O esqueleto está em `pages/manual-bash.html` (~22 KB): head + CSS + JS reaproveitados, branding de Bash (brand-mark `Sh`, título "Bash", hero "Terminal & Bash"), sidebar completa com os 22 capítulos, e footer apontando para o **Volume XVII — Regex** (último da coleção). Edição direta deste arquivo único. Marcador `<!-- CHAPTERS_INSERT_HERE -->` após o hero; **0 capítulos inseridos**.

## Workflow operacional

**Gatilho:** "continuar" → **UM capítulo por turno**, inserido por substituição exata do marcador (no Cap 22, o marcador é **REMOVIDO**). "Faça todos de forma autônoma" → produz os 22 em sequência. Use o `_insert.py` da raiz: `python _insert.py pages/manual-bash.html capNN.html N [final]`. Há permissão configurada em `.claude/settings.json` para rodar `python _insert.py` sem prompt.

## Estratégia de modelo

Padrão **Opus 4.8**. Capítulos conceituais (modelo do shell, pipes/composição, robustez) merecem Opus; os de referência prática (comandos de arquivo, filtros) podem ir a Sonnet sob pedido de economia.

## Os 22 capítulos (IDs batem com a sidebar — NÃO alterar)

| # | Título | ID | Grupo |
|---|--------|----|-------|
| 1 | O shell: o que é e como funciona | `introducao` | Fundamentos |
| 2 | Navegação e o sistema de arquivos | `navegacao` | Fundamentos |
| 3 | Comandos, argumentos e opções | `comandos` | Fundamentos |
| 4 | Ajuda e documentação | `ajuda` | Fundamentos |
| 5 | Manipulando arquivos e diretórios | `arquivos` | Arquivos e texto |
| 6 | Visualizando e editando texto | `texto` | Arquivos e texto |
| 7 | Permissões e propriedade | `permissoes` | Arquivos e texto |
| 8 | Globbing e wildcards | `globbing` | Arquivos e texto |
| 9 | Redirecionamento de E/S | `redirecionamento` | Pipes e fluxo |
| 10 | Pipes e composição | `pipes` | Pipes e fluxo |
| 11 | Filtros de texto | `filtros` | Pipes e fluxo |
| 12 | sed e awk | `sed-awk` | Pipes e fluxo |
| 13 | Escrevendo scripts | `scripts` | Scripting |
| 14 | Variáveis e expansão | `variaveis` | Scripting |
| 15 | Condicionais e testes | `condicionais` | Scripting |
| 16 | Loops | `loops` | Scripting |
| 17 | Funções | `funcoes` | Scripting |
| 18 | Argumentos e entrada | `argumentos` | Scripting |
| 19 | Processos e jobs | `processos` | Produção |
| 20 | Ambiente e configuração | `ambiente` | Produção |
| 21 | Robustez em scripts | `robustez` | Produção |
| 22 | Boas práticas (encerramento) | `producao` | Produção |

## Estrutura, spans, callouts, tom, densidade

Ver `CLAUDE.md`. Filename típico nos blocos: `terminal`, `script.sh`. Comentários de shell com `#`, sempre em PT-BR. Modelo mental antes do comando: explique como o shell lê/expande/executa antes da sintaxe.

## Disciplina de escape HTML (CRÍTICA — este volume é a de MAIOR risco)

Shell é cheio de `<`, `>`, `&`, `|`, `*`. Pontos quentes:

- Redirecionamentos: `>` → `&gt;`, `>>` → `&gt;&gt;`, `<` → `&lt;`, `2>&1` → `2&gt;&amp;1`, `<<` (heredoc) → `&lt;&lt;`
- Pipe `|` é seguro (não é especial em HTML), mas `&&`/`||` → `&amp;&amp;` / `||`
- Setas em comentários/saída: `->` → `-&gt;`, `-->` → `--&gt;` (erro recorrente nos Vols XIV-XV!)
- Comparações em testes: `[ "$a" -lt "$b" ]` (ok), mas `[[ $a > $b ]]` → `&gt;`
- Globs `*` e `?` são seguros; `[a-z]` é seguro
- Process substitution `<(cmd)` → `&lt;(cmd)`; `$()` é seguro
- Heredocs: o `<<EOF` precisa virar `&lt;&lt;EOF`

**Escape duplo (`&amp;gt;`) é erro grave.** Rode a validação por capítulo (passo 6: zero `<`/`>` cru em code) religiosamente — este volume vai acusar muito se descuidar.

## Validação e validação final

Ver `CLAUDE.md`. Não crie arquivos de backup — a validação por capítulo + commit no git são a salvaguarda. Validação final de 7 passos após o Cap 22.

## Convenções confirmadas

- **Bash** como shell de referência (não zsh/fish), mas apontar diferenças POSIX onde relevante (scripts portáteis usam `#!/bin/sh`).
- O usuário está no **Windows**: mencionar Git Bash / WSL como onde rodar Bash no Windows (conecta ao Vol XV, Cap 3).
- `set -euo pipefail` e `trap` no Cap 21 (robustez).
- Aspas em variáveis (`"$var"`) como disciplina central — a fonte nº 1 de bugs em shell.
- Comandos destrutivos (`rm -rf`, `>` que trunca) sempre com callout `warn`.

## Continuidade temática

- **Cap 1** abre conectando ao Vol XV (Docker empacota o ambiente; o shell o opera) e a toda a coleção: é no terminal que se roda build, deploy, git, docker.
- **Caps 9-12 (pipes/filtros)** são o coração conceitual: a filosofia Unix de pequenos programas compostos por pipes; grep/sed/awk como as ferramentas de texto que aparecem em todo o livro.
- **Caps 13-18 (scripting)** transformam comandos manuais em automação — conectar a hooks do Git (Vol XIV, Cap 20) e entrypoints/CI do Docker (Vol XV, Caps 5, 20).
- **Cap 21 (robustez)** revisita "falhar fechado" (Vol XIII, Cap 21) aplicado a scripts: `set -euo pipefail`, traps, aspas.
- **Cap 22 (encerramento)** fecha o volume e aponta para o **Volume XVII — Regex** — o último da coleção, e a ferramenta de texto que grep/sed/awk já anteciparam.

## Handoff ao final do Cap 22

Após o Cap 22: (a) esqueleto do **Volume XVII — Regex** (`_build_vol17.py` derivando de `manual-bash.html`; brand-mark `Rx`, branding Regex, sidebar dos capítulos, hero novo; como é o ÚLTIMO volume, o footer não aponta para um próximo volume — adaptar para um fechamento de coleção), e (b) `PROMPT-VOL-XVII-REGEX.md`. Atualizar o `index.html` tornando o card do Bash clicável e o `CLAUDE.md`.

## Gatilho para começar

Quando eu disser **"continuar"**, produza o **Capítulo 1 — O shell: o que é e como funciona** e insira no marcador de `pages/manual-bash.html`. Ao final, anuncie o Cap 2.
