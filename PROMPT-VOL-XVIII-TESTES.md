# Prompt de continuidade — Volume XVIII (Testes), Caps 1–22 — para Claude Code

Cole no Claude Code para produzir o **Volume XVIII — Testes**, que abre a **Onda 5 — Qualidade e Operação**. Leia também o `CLAUDE.md` na raiz.

---

## Contexto

**FullStack Manual**: coleção de manuais de referência fullstack em **português do Brasil**, cada um um HTML único autocontido, tema *dark warm*, syntax highlighting customizado. Hospedados em `https://vitormattosdev.github.io/FullStack-Manual/`.

A coleção tinha 17 volumes (núcleo fullstack, Ondas 1–4). A **Onda 5 — Qualidade e Operação** a estende com **Testes (XVIII)** e **DevOps (XIX)** — as práticas de engenharia que garantem que o stack funciona e se mantém em produção. Total agora: 19 volumes.

## Arquivo de trabalho

Esqueleto em `pages/manual-testes.html` (~22 KB): branding de Testes (brand-mark `Te`, título "Testes"), sidebar com 22 capítulos, footer apontando para **Vol XIX — DevOps**. Marcador `<!-- CHAPTERS_INSERT_HERE -->` após o hero; **0 capítulos**.

## Workflow

"continuar" → UM capítulo por turno (no Cap 22, marcador REMOVIDO). "Faça todos de forma autônoma" → os 22 em sequência. **Antes de inserir, rode `python _check.py capNN.html`**; depois `python _insert.py pages/manual-testes.html capNN.html N [final]`. Permissão já configurada em `.claude/settings.json`.

## Estratégia de modelo

Padrão **Opus 4.8**. Conceituais (pirâmide, TDD, o que testar, estratégia) merecem Opus; referência prática (matchers, setup) pode ir a Sonnet sob pedido.

## Os 22 capítulos (IDs batem com a sidebar — NÃO alterar)

| # | Título | ID | Grupo |
|---|--------|----|-------|
| 1 | Por que testar | `introducao` | Fundamentos |
| 2 | Anatomia de um teste | `anatomia` | Fundamentos |
| 3 | Vitest: setup e primeiro teste | `vitest` | Fundamentos |
| 4 | Asserções e matchers | `matchers` | Fundamentos |
| 5 | Testando funções puras | `funcoes-puras` | Testes unitários |
| 6 | Mocks, stubs e spies | `test-doubles` | Testes unitários |
| 7 | Mockando módulos e dependências | `mocking` | Testes unitários |
| 8 | Testando código assíncrono | `async` | Testes unitários |
| 9 | Tempo, timers e datas | `timers` | Testes unitários |
| 10 | Cobertura de testes | `cobertura` | Qualidade |
| 11 | TDD: test-driven development | `tdd` | Qualidade |
| 12 | O que (e o que não) testar | `o-que-testar` | Qualidade |
| 13 | Testando componentes React | `react` | Frontend |
| 14 | Testing Library | `testing-library` | Frontend |
| 15 | Interações e eventos | `interacoes` | Frontend |
| 16 | Mockando APIs com MSW | `msw` | Frontend |
| 17 | Testes de integração | `integracao` | Integração e E2E |
| 18 | Testando a camada de dados | `banco` | Integração e E2E |
| 19 | Playwright: end-to-end | `playwright` | Integração e E2E |
| 20 | Estratégia E2E e page objects | `e2e-estrategia` | Integração e E2E |
| 21 | Testes no CI | `ci` | Produção |
| 22 | Estratégia e boas práticas (encerramento) | `producao` | Produção |

## Estrutura, spans, callouts, tom, densidade

Ver `CLAUDE.md`. Filenames típicos: `soma.test.ts`, `vitest.config.ts`, `Botao.test.tsx`. Comentários em PT-BR. Modelo mental antes da ferramenta: explique *por que* e *o que* testar antes da API.

## Disciplina de escape HTML (CRÍTICA)

Dentro de `<pre><code>`, escape `<`→`&lt;`, `>`→`&gt;`, `&`→`&amp;`. Pontos quentes:

- Arrows: `=>` → `=&gt;` (onipresente em testes); `->` em comentários → `-&gt;`
- Generics: `expect<T>`, `Array<string>` → escapar
- JSX em `.tsx` (Cap 13-15): `<Botao />` → `&lt;Botao /&gt;`, `<button>` → `&lt;button&gt;`
- Comparações em asserts: `expect(a < b)` → `&lt;`
- `&&`/`||` → `&amp;&amp;` / `||`

`python _check.py capNN.html` antes de cada inserção pega isto.

## Validação e validação final

Ver `CLAUDE.md`. Não crie arquivos de backup — validação por capítulo + commit no git são a salvaguarda. Validação final de 7 passos após o Cap 22.

## Convenções confirmadas (Jun/2026)

- **Vitest** como runner de referência (sucessor do Jest no ecossistema Vite/TS); mencionar Jest como equivalente onde relevante.
- **Testing Library** (`@testing-library/react`) — testar como o usuário, por papel/texto, não por implementação.
- **MSW** (Mock Service Worker) para mockar rede a nível de requisição.
- **Playwright** para E2E (preferido sobre Cypress no ecossistema atual).
- Conectar ao stack: testar funções (Zod schemas Vol XII), endpoints Hono (Vol IX), camada Drizzle/Postgres (Vols X-XI), componentes React/Next (Vols V/VII), fluxos de auth (Vol XIII).

## Continuidade temática

- **Cap 1** abre conectando à coleção inteira: você construiu o stack; os testes garantem que ele funciona e sobrevive a mudanças. A pirâmide de testes (muitos unitários, alguns de integração, poucos E2E).
- **Caps 3-9 (Vitest/unitários)** usam exemplos do stack: testar um schema Zod, uma função de cálculo, a verificação de senha (Vol XIII, Cap 2 — hashing).
- **Caps 13-16 (frontend)** testam componentes React (Vol V) com Testing Library; MSW mocka as APIs Hono.
- **Cap 17-18 (integração/banco)** testam endpoints reais e a camada Drizzle (Vol XI) com Postgres (Vol X) conteinerizado (Vol XV) — Testcontainers.
- **Cap 19-20 (E2E)** testam fluxos completos (login, Vol XIII) no navegador com Playwright.
- **Cap 21 (CI)** integra os testes ao pipeline (Vol XIV, Cap 19 + Vol XV, Cap 20): testes como barreira automática contra regressão.
- **Cap 22 (encerramento)** fecha com a estratégia de testes (a pirâmide aplicada), o que NÃO testar, e aponta para o **Vol XIX — DevOps**.

## Handoff ao final do Cap 22

Após o Cap 22: (a) tornar o card de Testes clicável no `index.html` (Passo 18, contador 18/19, progress 94.7%); (b) atualizar `CLAUDE.md` (Testes ✅); (c) estruturar o **Vol XIX — DevOps** (`_build_vol19.py` derivando de `manual-testes.html`; brand-mark `Op`, branding DevOps, sidebar dos capítulos, hero; footer = ÚLTIMO da coleção, fechamento como o Regex fazia) e `PROMPT-VOL-XIX-DEVOPS.md`.

## Gatilho para começar

Quando eu disser **"continuar"**, produza o **Capítulo 1 — Por que testar** e insira no marcador de `pages/manual-testes.html`. Ao final, anuncie o Cap 2.
