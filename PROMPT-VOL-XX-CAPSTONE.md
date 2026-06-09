# Prompt de continuidade — Volume XX (Projeto Fullstack / Capstone), Caps 1–22 — para Claude Code

Cole no Claude Code para produzir o **Volume XX — Projeto Fullstack**, o **capstone** da coleção: o volume que não ensina nenhuma tecnologia nova, mas costura todas as 19 anteriores construindo **um app real de ponta a ponta**. Leia também o `CLAUDE.md` na raiz.

---

## Contexto

**FullStack Manual**: coleção de manuais de referência fullstack em **português do Brasil**, HTML único autocontido, tema *dark warm*. Hospedados em `https://vitormattosdev.github.io/FullStack-Manual/`.

Os Vols I–XIX cobriram o stack **verticalmente** — cada um fundo num tema (TypeScript, React, Hono, Postgres, Docker, DevOps…). O que falta é o fio **horizontal**: como uma feature real atravessa o stack inteiro, do schema ao deploy. Esse é o conhecimento que só aparece quando se junta tudo, e que nenhum volume isolado entrega.

O Volume XX é esse fio. Ele é um **capstone / projeto-guia**: constrói uma aplicação real, e cada capítulo é uma fatia (vertical ou horizontal) que toca vários volumes ao mesmo tempo. Ele **não reexplica** as tecnologias — assume os 19 volumes e mostra a *costura* entre elas, linkando de volta para o aprofundamento ("o *porquê* está no Vol X Cap 4; aqui você vê *onde se encaixa*"). É o "agora junte tudo" depois de dominar as peças.

> **Princípio editorial nº 1:** se um capítulo está reexplicando como uma tecnologia funciona, ele está errado. O capstone mostra **decisões, integração e fluxo de dados ponta a ponta** — o que só existe quando as peças se encontram. Conceito de integração antes de código, sempre.

## A aplicação: **Quadro**

Um gerenciador de tarefas em time (mini-Trello/Linear). É pequeno, mas exercita o stack mais completo possível:

- **Usuários** se cadastram e logam (Vol XIII).
- **Times** (teams) agrupam usuários; um usuário pertence a vários times via **memberships** com **papel** (`admin` | `member`).
- **Tarefas** (tasks) pertencem a um time, têm título, descrição, status (`todo` | `doing` | `done`) e um responsável opcional.
- **Multi-tenancy + autorização**: cada usuário só vê e mexe nos times/tarefas a que pertence; admins do time podem mais que membros. (É aqui que mora o IDOR — o erro clássico de "esqueci de filtrar por team".)

> O nome **Quadro** é um placeholder — pode ser renomeado, mas mantenha consistência em todos os capítulos depois de fixado.

### Estrutura canônica do projeto (NÃO divergir entre capítulos)

O app é um **monorepo** (pnpm workspaces). Todo código de todo capítulo referencia estes caminhos — a coerência do exemplo entre os 22 capítulos depende disso:

```
quadro/
  package.json                 # workspace root
  pnpm-workspace.yaml
  packages/
    core/                      # contrato compartilhado (Cap 3)
      schema.ts                #   schemas Zod + tipos inferidos
  apps/
    api/                       # backend Hono (Caps 5-9)
      src/
        index.ts               #   bootstrap do servidor
        db/schema.ts           #   tabelas Drizzle (Cap 4)
        db/client.ts
        routes/tasks.ts        #   feature de tarefas (Cap 9)
        routes/auth.ts         #   registro/login (Cap 7)
        middleware/auth.ts     #   autenticação + escopo de team (Cap 8)
    web/                       # frontend Next.js (Caps 10-15)
      app/                     #   App Router
      lib/api.ts               #   cliente tipado (Cap 11)
  docker-compose.yml           # app + Postgres (Cap 19)
  Dockerfile                   # multi-stage por app (Cap 19)
  .github/workflows/ci.yml     # pipeline do monorepo (Cap 18)
```

## Arquivo de trabalho

Esqueleto em `pages/manual-capstone.html` (a ser criado no bootstrapping): branding **brand-mark `Fs`**, título **"Projeto Fullstack"**, sub "Referência · O stack inteiro, ponta a ponta", header-meta "Volume XX". Sidebar com os 22 capítulos abaixo. **Como é o novo último volume**, o footer fecha a coleção ("Volume final da coleção · 20 volumes", sem próximo). Marcador `<!-- CHAPTERS_INSERT_HERE -->` após o hero; **0 capítulos**.

## Workflow

"continuar" → UM capítulo por turno (no Cap 22, marcador REMOVIDO). "Faça todos de forma autônoma" → os 22 em sequência. **Antes de inserir, rode `python _check.py capNN.html`**; depois `python _insert.py pages/manual-capstone.html capNN.html N [final]`. Apagar o `capNN.html` após validar.

## Estratégia de modelo

Padrão **Opus 4.8**. Os capítulos conceituais/de integração (arquitetura, contrato compartilhado, autorização/multi-tenancy, retrospectiva) merecem Opus; os de implementação mais mecânica (montar a UI, formulários) podem ir a Sonnet sob pedido. Como o volume é code-heavy, **redobrar a atenção ao escape** (ver abaixo).

## Os 22 capítulos (IDs batem com a sidebar — NÃO alterar)

| # | Título | ID | Grupo | Volumes que costura |
|---|--------|----|-------|---------------------|
| 1 | Anatomia de um app fullstack | `arquitetura` | Fundação | todos (o mapa + a ideia de fatia vertical) |
| 2 | O monorepo e o tooling | `monorepo` | Fundação | I, II, XVI |
| 3 | O contrato compartilhado | `contrato` | Fundação | I, XII |
| 4 | Modelagem de dados | `modelagem` | Fundação | X, XI |
| 5 | A API com Hono | `api` | Backend | VIII, IX, XII |
| 6 | Persistência com Drizzle | `persistencia` | Backend | X, XI |
| 7 | Autenticação | `autenticacao` | Backend | XIII |
| 8 | Autorização e multi-tenancy | `autorizacao` | Backend | XIII |
| 9 | Uma feature completa no servidor | `feature-servidor` | Backend | IX–XIII |
| 10 | O frontend Next.js | `frontend` | Frontend | VII |
| 11 | Falando com a API, com tipos | `cliente` | Frontend | I, IX, XII |
| 12 | Interface com React + Tailwind | `interface` | Frontend | III, IV, V, VI |
| 13 | Dados no cliente | `dados-cliente` | Frontend | V, VII |
| 14 | Formulários e validação | `formularios` | Frontend | V, XII |
| 15 | Autenticação no frontend | `auth-cliente` | Frontend | VII, XIII |
| 16 | Testando a fatia vertical | `testes` | Qualidade | XVIII |
| 17 | Testes E2E do fluxo crítico | `e2e` | Qualidade | XVIII |
| 18 | CI: a barreira do monorepo | `ci` | Qualidade | XIV, XVIII, XIX |
| 19 | Conteinerizando o stack | `containers` | Produção | XV, XIX |
| 20 | Deploy de ponta a ponta | `deploy` | Produção | XIX |
| 21 | Operando em produção | `operacao` | Produção | XIX |
| 22 | Retrospectiva: o stack inteiro | `retrospectiva` | Produção | todos (encerramento) |

Grupos da sidebar: **Fundação** (1–4) · **Backend** (5–9) · **Frontend** (10–15) · **Qualidade** (16–18) · **Produção** (19–22).

## Estrutura, spans, callouts, tom, densidade

Ver `CLAUDE.md`. Filenames típicos: `schema.ts`, `db/schema.ts`, `routes/tasks.ts`, `lib/api.ts`, `docker-compose.yml`, `ci.yml`, `terminal`. Comentários em PT-BR. **Modelo mental de integração antes do código**: cada capítulo abre explicando *que costura ele faz* e *por que naquela ordem*, antes de qualquer sintaxe. Densidade igual aos outros volumes (6–8 `topic`, 5–7 blocos de código, 2–3 callouts, 1 tabela final).

## Disciplina de escape HTML (CRÍTICA — este é o volume mais code-heavy da coleção)

Dentro de `<pre><code>`, escape `<`→`&lt;`, `>`→`&gt;`, `&`→`&amp;`. Pontos quentes deste volume:

- **Arrows JS/TS** `=>` → `=&gt;` (onipresente em TS/React — a fonte de erro nº 1 aqui)
- **Generics**: `Promise<T>`, `z.infer<typeof X>`, `Array<Task>`, `useState<...>` → escapar `<`/`>`
- **JSX**: `<div>`, `<form>`, `<TaskCard />` → `&lt;div&gt;` etc.
- **Shell**: `2>&1` → `2&gt;&amp;1`, `&&`/`||` → `&amp;&amp;`/`||`
- **YAML/Docker**: `>-`, comparações; **setas em diagramas/comentários** `->`/`-->` → `-&gt;`/`--&gt;`
- **JSX comparações em condicionais** e `&&` de render: `{x && <C/>}` → `{x &amp;&amp; &lt;C/&gt;}`

`python _check.py capNN.html` antes de cada inserção pega isto. **Escape duplo (`&amp;gt;`) é erro grave.**

## Validação e validação final

Ver `CLAUDE.md`. Não crie arquivos de backup. Validação por capítulo após cada inserção; validação final de 7 passos após o Cap 22.

## Convenções confirmadas (Jun/2026)

- Stack do app = o stack canônico da coleção: **TS + Hono + Drizzle + Postgres + Zod + Next.js + React + Tailwind**, testado com **Vitest + Testing Library + Playwright**, conteinerizado com **Docker**, entregue por **GitHub Actions**, hospedado num PaaS (Fly/Railway, Vol XIX Cap 10).
- **Revalidar versões via npm** antes de fixar qualquer pacote nos capítulos (regra do `CLAUDE.md`), registrando a data no callout.
- O capstone **cita capítulos específicos** dos outros volumes em vez de reexplicar ("queries parametrizadas — Vol X Cap 7").

## Continuidade temática

- **Cap 1** abre conectando à coleção inteira: os 19 volumes deram as peças; este as junta. Apresenta o **Quadro**, a arquitetura, e a ideia de **fatia vertical** (uma feature atravessando todas as camadas) como o organizador do volume.
- **Caps 2–4 (Fundação)** montam o terreno compartilhado: o monorepo, o pacote `core` com os schemas Zod que viram a *única fonte de verdade de tipos* para back e front (a cola ponta a ponta), e a modelagem do domínio em Drizzle/Postgres.
- **Caps 5–9 (Backend)** constroem o servidor camada por camada até a **primeira feature inteira** (CRUD de tarefas), culminando em autorização/multi-tenancy — o tema mais sutil e o que mais conecta segurança (Vol XIII) à modelagem (Cap 4).
- **Caps 10–15 (Frontend)** consomem o backend reusando o contrato do Cap 3 (tipos ponta a ponta, fim do `any` na fronteira), constroem a UI e fecham o loop com auth no cliente.
- **Caps 16–18 (Qualidade)** aplicam a pirâmide do Vol XVIII ao app real, e erguem o CI do monorepo como barreira.
- **Caps 19–22 (Produção)** levam o Quadro ao ar com o Vol XIX (containers, deploy, operação) e encerram com a **retrospectiva da coleção inteira** — as 6 fases pedagógicas, da primeira linha de TS ao app operado em produção.

## Handoff ao final do Cap 22

Como passa a ser o ÚLTIMO volume (20 no total): (a) NÃO há próximo esqueleto; (b) tornar o card de Projeto Fullstack clicável no `index.html` — nova **fase-8** na trilha ("Junte tudo / O projeto completo"), card com **Passo 20 · Vol XX**, mark `Fs`, status "Pronto", contador **20/20**, progress **100%**; (c) atualizar `CLAUDE.md` (nova linha no roadmap como **Onda 6 — Síntese**, tabela de arquivos, "coleção completa em 20/20", e os contadores `/19`→`/20`); (d) sugerir varredura final de toda a coleção e commit/push.

## Gatilho para começar

Quando eu disser **"continuar"**, **primeiro** faça o bootstrapping do esqueleto `pages/manual-capstone.html` (técnica do `CLAUDE.md`, derivando de um manual recente — validar o esqueleto antes de prosseguir), **depois** produza o **Capítulo 1 — Anatomia de um app fullstack** e insira no marcador. Ao final, anuncie o Cap 2.
