# Prompt de continuidade — Volume XVII (Regex), Caps 1–22 — para Claude Code

Cole este conteúdo no Claude Code para produzir o **Volume XVII — Regex**, o **último volume** da coleção FullStack Manual. Leia também o `CLAUDE.md` na raiz.

---

## Contexto

Estou construindo a **FullStack Manual**: coleção de 17 manuais de referência fullstack em **português do Brasil**, cada um um arquivo HTML único e autocontido, tema *dark warm*, syntax highlighting customizado. Hospedados em `https://vitormattosdev.github.io/FullStack-Manual/`.

O **Volume XVII — Regex** é o **último da coleção** — ele a fecha. Continua e encerra a Onda 4. Os capítulos de shell (Vol XVI, grep/sed/awk) já anteciparam regex; aqui ela é tratada por inteiro.

## Arquivo de trabalho

Esqueleto em `pages/manual-regex.html` (~22 KB): head/CSS/JS reaproveitados, branding Regex (brand-mark `Rx`, título "Regex"), sidebar com os 22 capítulos. **Como é o último volume, o footer NÃO aponta para um próximo volume** — ele fecha a coleção ("Volume final da coleção · A fundação fullstack, completa em 17 volumes"). Marcador `<!-- CHAPTERS_INSERT_HERE -->` após o hero; **0 capítulos inseridos**.

## Workflow operacional

"continuar" → UM capítulo por turno (no Cap 22, marcador REMOVIDO). "Faça todos de forma autônoma" → os 22 em sequência. Use `_insert.py`: `python _insert.py pages/manual-regex.html capNN.html N [final]`. Permissão já configurada em `.claude/settings.json`.

**Antes de cada inserção, rode `python _check.py capNN.html`** para pegar `<`/`>` crus no temporário antes de inserir (este volume é o de MAIOR risco de escape — ver abaixo).

## Estratégia de modelo

Padrão **Opus 4.8**. Conceituais (modelo de matching, backtracking, ReDoS, lookaround) merecem Opus; referência prática (classes, quantificadores, flags) pode ir a Sonnet sob pedido de economia.

## Os 22 capítulos (IDs batem com a sidebar — NÃO alterar)

| # | Título | ID | Grupo |
|---|--------|----|-------|
| 1 | O que é uma expressão regular | `introducao` | Fundamentos |
| 2 | Literais e metacaracteres | `literais` | Fundamentos |
| 3 | Classes de caracteres | `classes` | Fundamentos |
| 4 | Quantificadores | `quantificadores` | Fundamentos |
| 5 | Âncoras e limites | `ancoras` | Âncoras e grupos |
| 6 | Grupos e captura | `grupos` | Âncoras e grupos |
| 7 | Alternância | `alternancia` | Âncoras e grupos |
| 8 | Backreferences | `backreferences` | Âncoras e grupos |
| 9 | Grupos não-capturantes e nomeados | `grupos-nomeados` | Avançado |
| 10 | Lookahead e lookbehind | `lookaround` | Avançado |
| 11 | Ganância vs preguiça | `ganancia` | Avançado |
| 12 | Flags e modificadores | `flags` | Avançado |
| 13 | Regex em JavaScript | `javascript` | Na prática |
| 14 | Regex no shell | `shell` | Na prática |
| 15 | Validação com regex | `validacao` | Na prática |
| 16 | Substituição e captura | `substituicao` | Na prática |
| 17 | Sabores: PCRE, POSIX, JS | `sabores` | Na prática |
| 18 | Performance e backtracking | `performance` | Produção |
| 19 | ReDoS: regex como ataque | `redos` | Produção |
| 20 | Legibilidade e manutenção | `legibilidade` | Produção |
| 21 | Ferramentas e depuração | `ferramentas` | Produção |
| 22 | Boas práticas (encerramento) | `producao` | Produção |

## Estrutura, spans, callouts, tom, densidade

Ver `CLAUDE.md`. Filename típico nos blocos: `regex`, `exemplo.js`, `terminal`. Comentários em PT-BR. Modelo mental antes da sintaxe: explique o que o motor de regex faz (matching, backtracking) antes dos metacaracteres.

## Disciplina de escape HTML (CRÍTICA — risco máximo)

Regex é densa em caracteres especiais de HTML. Pontos quentes:

- Âncoras e literais: a regex em si raramente tem `<`/`>`, MAS exemplos de validação de HTML/XML têm (`&lt;`, `&gt;`)
- Em código JS: generics e arrows — `string.match()` é seguro, mas `=>` → `=&gt;`, `Array<string>` → `Array&lt;string&gt;`
- Lookaround: `(?=...)`, `(?<=...)` — o `<` do lookbehind `(?<=` → `(?&lt;=` e `(?<!` → `(?&lt;!`; grupos nomeados `(?<nome>)` → `(?&lt;nome&gt;)`
- Setas em comentários/diagramas: `->` → `-&gt;`, `-->` → `--&gt;` (erro recorrente em TODOS os volumes anteriores)
- Classes negadas `[^...]` — o `^` é seguro; `&` em `[&]` → `&amp;`
- Quantificadores `{n,m}`, `*`, `+`, `?`, `|`, `.` são seguros em HTML

**Atenção redobrada ao lookbehind `(?<=` e grupos nomeados `(?<nome>)` — o `<` é cru.** Rode `_check.py` em todo capítulo antes de inserir. Escape duplo (`&amp;gt;`) é erro grave.

## Validação e validação final

Ver `CLAUDE.md`. Não crie arquivos de backup — validação por capítulo + commit no git são a salvaguarda. Validação final de 7 passos após o Cap 22.

## Convenções confirmadas

- **Sabor de referência: JavaScript** (regex nativa, `/padrão/flags`), por ser o do stack da coleção; apontar diferenças de PCRE e POSIX no Cap 17.
- Conectar à validação do **Zod** (Vol XII): `z.string().regex(...)`, e a tensão entre validar com regex vs com parsers dedicados (e-mail!).
- **ReDoS** (Cap 19) é o capítulo de segurança: conectar ao Vol XIII (input malicioso, DoS) — regex com backtracking exponencial sobre input do atacante derruba o servidor.
- Ferramentas (Cap 21): regex101.com como depurador visual de referência.

## Continuidade temática

- **Cap 1** abre conectando ao Vol XVI (grep/sed/awk já usavam regex) e à coleção inteira (validação no Zod, busca de código, processamento de texto).
- **Caps 13-14 (JS/shell)** ligam aos volumes de origem: regex em JavaScript (Vols I-II) e no shell (Vol XVI).
- **Cap 15 (validação)** conecta ao Zod (Vol XII) e à fronteira de dados de toda a coleção; discutir o clássico "não valide e-mail com regex".
- **Cap 19 (ReDoS)** revisita segurança (Vol XIII): catastrophic backtracking como vetor de DoS sobre input não confiável.
- **Cap 22 (encerramento)** é o fechamento da **coleção inteira** — não só do volume. Faça uma retrospectiva do arco: tipos → interface → backend → autenticação → git → docker → shell → regex. A fundação fullstack, completa.

## Handoff ao final do Cap 22

Após o Cap 22, como é o ÚLTIMO volume: (a) NÃO há próximo esqueleto a criar; (b) atualizar o `index.html` tornando o card do Regex clicável e o contador para **17/17 (100%)**; (c) atualizar o `CLAUDE.md` (Regex ✅, coleção completa). Opcionalmente, sugerir ao usuário uma revisão/varredura final de toda a coleção e o commit final no git.

## Gatilho para começar

Quando eu disser **"continuar"**, produza o **Capítulo 1 — O que é uma expressão regular** e insira no marcador de `pages/manual-regex.html`. Ao final, anuncie o Cap 2.
