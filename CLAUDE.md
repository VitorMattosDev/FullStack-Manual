# CLAUDE.md — FullStack Manual

Guia operacional para produzir e manter os manuais desta coleção. Leia isto antes de escrever qualquer capítulo ou estruturar um volume novo.

## O que é o projeto

**FullStack Manual** é uma coleção de **17 manuais de referência fullstack em português do Brasil (PT-BR)**. Cada volume é um **arquivo HTML único e autocontido** — sem build, sem dependências, sem JS externo além das fontes do Google. Tema *dark warm*, syntax highlighting customizado em `<span>`, navegação por sidebar com scroll-spy e busca client-side.

Hospedados em GitHub Pages: `https://vitormattosdev.github.io/FullStack-Manual/`.

## Estrutura do repositório

```
index.html                         # landing page: hero + trilha de aprendizado (6 fases) + cards por volume
pages/
  typescript.html                  # Vol I    (mark: Ts)
  javascript.html                  # Vol II   (Js)
  manual-html.html                 # Vol III  (Hs)
  manual-css.html                  # Vol IV   (Cs)
  manual-react.html                # Vol V    (Rc)
  manual-tailwind.html             # Vol VI   (Tw)
  manual-nextjs.html               # Vol VII  (Nx)
  manual-nodejs.html               # Vol VIII (Nd)
  manual-hono.html                 # Vol IX   (Hn)
  manual-sql-postgresql.html       # Vol X    (Pg)
  manual-drizzle.html              # Vol XI   (Dz)
  manual-zod.html                  # Vol XII  (Zd)
  manual-autenticacao.html         # Vol XIII (Au)  ✅ 22 caps
  manual-git.html                  # Vol XIV  (Gt)  ✅ 22 caps
  manual-docker.html               # Vol XV   (Dk)  ✅ 22 caps
  manual-bash.html                 # Vol XVI  (Sh)  ✅ 22 caps
  manual-regex.html                # Vol XVII (Rx)  ✅ 22 caps (fim da Onda 4 / núcleo fullstack)
  manual-testes.html               # Vol XVIII (Te) ✅ 22 caps — Onda 5
  manual-devops.html               # Vol XIX  (Op)  ⬜ planejado — Onda 5
_insert.py                         # insere 1 capítulo no marcador + valida (ajustar `path`)
PROMPT-VOL-*.md                    # prompt de inicialização de cada volume futuro
CLAUDE.md                          # este arquivo
```

> **Nota:** os volumes I–XII usam nomes de arquivo variados (`typescript.html`, `manual-html.html`, etc.). Volumes novos seguem o padrão `manual-<slug>.html`.

## Roadmap dos volumes

| Onda | Vol | Tema | Arquivo | Mark | Status |
|------|-----|------|---------|------|--------|
| 1 Fundamentos da web | I | TypeScript | typescript.html | Ts | ✅ |
| 1 | II | JavaScript moderno | javascript.html | Js | ✅ |
| 1 | III | HTML semântico + a11y | manual-html.html | Hs | ✅ |
| 1 | IV | CSS moderno | manual-css.html | Cs | ✅ |
| 2 Camada visual | V | React | manual-react.html | Rc | ✅ |
| 2 | VI | Tailwind CSS | manual-tailwind.html | Tw | ✅ |
| 2 | VII | Next.js | manual-nextjs.html | Nx | ✅ |
| 3 Backend TypeScript | VIII | Node.js | manual-nodejs.html | Nd | ✅ |
| 3 | IX | Hono | manual-hono.html | Hn | ✅ |
| 3 | X | SQL + PostgreSQL | manual-sql-postgresql.html | Pg | ✅ |
| 3 | XI | Drizzle ORM | manual-drizzle.html | Dz | ✅ |
| 3 | XII | Zod | manual-zod.html | Zd | ✅ |
| 3 | XIII | Autenticação | manual-autenticacao.html | Au | ✅ |
| 4 Ferramentas do ofício | XIV | Git | manual-git.html | Gt | ✅ |
| 4 | XV | Docker | manual-docker.html | Dk | ✅ |
| 4 | XVI | Terminal & Bash | manual-bash.html | Sh | ✅ |
| 4 | XVII | Regex | manual-regex.html | Rx | ✅ |
| 5 Qualidade e operação | XVIII | Testes | manual-testes.html | Te | ✅ |
| 5 | XIX | DevOps | manual-devops.html | Op | ⬜ planejado |

O `mark` de cada volume (2 letras) **deve ser idêntico** no card do `index.html` e no `brand-mark` do manual.

## Anatomia de um manual

Cada arquivo segue esta espinha (reaproveitada entre volumes — o `<head>`/CSS/JS são copiados e só o branding muda):

```
<!DOCTYPE html><html lang="pt-BR">
<head>
  <title>TEMA — Manual de Referência · Volume NN</title>
  <link ... fonts: Fraunces + IBM Plex Sans + JetBrains Mono>
  <style> :root{ paleta dark warm + --sx-* (syntax) } ... </style>
</head>
<body>
  <div class="scroll-progress" id="progress"></div>
  <header class="top"><div class="inner">
    <a href="#top" class="brand">
      <div class="brand-mark">XX</div>
      <div class="brand-text"><div class="title">Tema</div><div class="sub">Referência · ...</div></div>
    </a>
    <input id="search" ...>
    <div class="header-meta"><span>Volume NN</span><span>22 capítulos</span></div>
    <button id="menuToggle">☰</button>
  </div></header>
  <div class="layout" id="top">
    <aside class="sidebar" id="sidebar"><nav>
      <div class="nav-group"><div class="nav-group-title">Grupo</div><ul>
        <li><a href="#id">01 · Título</a></li> ...
      </ul></div> ...
    </nav></aside>
    <main>
      <div class="hero"> eyebrow + h1 + lead + hero-meta </div>
      <!-- CHAPTERS_INSERT_HERE -->
      <footer class="page-footer"> ornament + próximo volume + meta </footer>
    </main>
  </div>
  <script> scroll-progress + copy-btn + scroll-spy (IntersectionObserver) + busca + menu mobile </script>
</body></html>
```

### Estrutura de cada capítulo

```html
<section class="chapter" id="ID">
  <div class="chapter-number">Capítulo N</div>
  <h2 class="chapter-title">Título com <em>palavra</em></h2>
  <p class="chapter-intro">Abertura: modelo mental antes da sintaxe.</p>

  <h3 class="topic"><span class="hash">#</span> Subtítulo</h3>
  <p>...</p>

  <div class="code-wrap">
    <div class="code-header"><span class="filename">arquivo.ext</span><button class="copy-btn">Copiar</button></div>
    <pre><code>... (highlight em spans) ...</code></pre>
  </div>

  <div class="callout note">   <!-- note | tip | warn -->
    <div class="callout-label">Rótulo</div>
    <div class="callout-body">...</div>
  </div>

  <div class="table-wrap"><table><thead>...</thead><tbody>...</tbody></table></div>
</section>
```

## Convenções de conteúdo

**Spans de syntax highlight** (dentro de `<code>`) — vocabulário fixo, NÃO inventar classes novas:

| Classe | Uso |
|--------|-----|
| `cm` | comentário |
| `kw` | keyword / binário (`git`, `import`, `const`) |
| `st` | string |
| `nm` | número |
| `cl` | classe / tipo |
| `fn` | função / subcomando |
| `pr` | propriedade / flag (`--amend`) |
| `op` | operador |

(As classes `at`/`dr`/`tg` **não** estão em uso nos volumes recentes — não as introduza.)

**Callouts:** `note` (contexto), `tip` (recomendação), `warn` (perigo/erro comum). Cada um com `.callout-label` + `.callout-body`.

**Tom:** prosa enxuta, **modelo mental antes da sintaxe**. Evitar "vamos explorar", "imagine que". Comentários de código sempre em PT-BR. Conectar capítulos entre si e a volumes anteriores ("o Cap X do Vol Y...") — a coleção é um arco, não capítulos soltos.

**Densidade típica por capítulo:** 6–8 `<h3 class="topic">`, 5–7 blocos de código, 2–3 callouts, 1 tabela de referência ao final (5–7 linhas). ~14–22 KB por capítulo.

## Disciplina de escape HTML (CRÍTICA)

Dentro de `<pre><code>`, **todo** caractere especial é escapado, **manualmente e cirurgicamente** (nunca regex em massa):

- `<` → `&lt;` · `>` → `&gt;` · `&` → `&amp;`
- `&&` → `&amp;&amp;` · arrow JS `=>` → `=&gt;`
- Generics: `Promise<T>` → `Promise&lt;T&gt;`, `z.infer<typeof X>` → `z.infer&lt;typeof X&gt;`
- JSX/HTML: `<form>` → `&lt;form&gt;`
- Shell: `2>&1` → `2&gt;&amp;1`, marcadores de conflito `<<<<<<<` / `>>>>>>>` → escapar cada caractere
- **Setas em comentários/diagramas ASCII**: `->` → `-&gt;`, `-->` → `--&gt;` (fonte recorrente de `>` cru — checar sempre)
- Comparações: `a < b` → `a &lt; b`
- URLs com vários params: `?a=1&b=2` → `?a=1&amp;b=2`

**Escape duplo (`&amp;gt;`) é erro grave.** Fora de `<pre><code>`, na prosa, use entidades só quando necessário.

## Workflow de produção

1. **Gatilho `"continuar"`** → produzir **UM capítulo por turno**. Se o usuário disser "faça todos de forma autônoma", produzir todos em sequência.
2. Escrever o capítulo num arquivo temporário `capNN.html` (raiz).
3. Inserir por **substituição de string exata** do marcador:
   ```
   <!-- CHAPTERS_INSERT_HERE -->
   ```
   por
   ```
   <section ...>...</section>

   <!-- CHAPTERS_INSERT_HERE -->
   ```
   No **último capítulo**, o marcador é **REMOVIDO** (não reposto).
4. Usar `_insert.py`: `python _insert.py <pages/manual-slug.html> capNN.html N [final]`.
5. Apagar o `capNN.html` temporário após validar.
6. Anunciar o próximo capítulo ao final do turno.

### `_insert.py`

Script reutilizável na raiz. Faz `replace(marker, chapter)` e roda a **validação por capítulo** (ver abaixo). Argumentos: `<path>` (caminho do manual, ex.: `pages/manual-docker.html`), `capNN.html` (arquivo do capítulo), `N` (contagem esperada de sections após inserir), `final` (opcional — remove o marcador).

### Validação por capítulo (após cada inserção)

1. marcador `CHAPTERS_INSERT_HERE` == 1 (ou 0 no último)
2. nº de `<section class="chapter">` == N esperado
3. tags balanceadas (`section`, `pre`, `code`, `div`, `span`) via `<tag[\s>]` vs `</tag>`
4. typos == 0: `<pre">`, `<code">`, `<span">`, `<div">`
5. escape duplo == 0: `&amp;gt;`, `&amp;lt;`, `&amp;amp;`
6. dentro de cada `<pre><code>`: removidos spans+entidades, resíduo de `<`/`>` cru == 0
7. arrows JS cruas (`=>`) == 0 dentro de code (só em volumes com JS/TS)

### Salvaguarda (NÃO criar arquivos de backup)

**Não** crie arquivos `*-backup-capNN.html`. Eles são redundantes e só inflam o repositório. A proteção real vem de duas fontes que já cobrem o risco:

1. **Validação por capítulo** — o `_insert.py` aborta na hora se uma inserção corromper o arquivo, então erros nunca se propagam silenciosamente.
2. **Git** — ao concluir um manual, faça um commit (`Manual X adicionado`, seguindo o histórico do repo). Cada commit é um ponto de restauração recuperável, muito superior a snapshots em marcos arbitrários. Em produções autônomas longas, um commit ao final é o backup; se quiser checkpoints intermediários, use commits, não cópias de arquivo.

### Validação final — 7 passos (após o último capítulo)

1. marcador removido (0 ocorrências)
2. nº correto de `<section class="chapter">`
3. cross-check: hrefs da sidebar ↔ section ids, zero divergência
4. tags balanceadas (section, pre, code, div, span)
5. typos == 0, escape duplo == 0
6. cauda == `</script></body></html>` (precedida de `</main></div>`)
7. varredura global: 0 code com `<`/`>` cru; ordem dos IDs correta; `Capítulo 1`–`N` sequenciais

## Estruturar um volume novo (bootstrapping)

Cada esqueleto novo é derivado do manual anterior, reaproveitando head/CSS/JS. Técnica (script Python `_build_volNN.py` descartável):

1. Ler o manual anterior (ou um esqueleto já limpo) como base.
2. Trocar `<title>`, `brand-mark` (2 letras = mark do index), `brand-text` (title + sub), `header-meta` (Volume NN).
3. Substituir o `<nav>` inteiro pela sidebar do novo volume (grupos + 22 itens com IDs novos).
4. Substituir o bloco `<div class="hero">...</div>` — **ancorar o fim do hero no início da primeira `<section>` ou no marcador** (`(?=\n\s*<section)` ou `(?=\n\s*<!-- CHAPTERS)`), senão o regex não-guloso corta no primeiro `</div></div>` interno do hero-meta.
5. Remover todos os capítulos e deixar só `<!-- CHAPTERS_INSERT_HERE -->`.
6. Atualizar o `<footer>`: "Próximo volume: <strong>PRÓXIMO</strong> — ..." e "Volume NN de XVII".
7. **Validar o esqueleto:** marcador == 1, sections == 0, zero resíduo do volume anterior (branding antigo, "Volume N-1", hero antigo), brand-mark novo presente, tags balanceadas, termina em `</html>`.
8. Escrever `PROMPT-VOL-NN-<TEMA>.md` (mesmo formato dos existentes: contexto, arquivo, workflow, tabela de capítulos, escape, validação, continuidade temática, handoff). Não inclua seção de backups.

## Atualizar o `index.html` ao concluir um volume

- O index é uma **trilha de aprendizado**: 6 seções `<section class="wave" id="fase-N">` (fases pedagógicas, NÃO a ordem dos volumes), cada card com `<span class="vol">Passo N · Vol XX</span>`. A ordem dos cards é a ordem de estudo recomendada para iniciantes; o "Vol XX" é só a referência canônica.
- Trocar o card de `<div class="card planned">` para `<a class="card" href="pages/manual-<slug>.html">`, status "Planejado" → "Pronto", e inseri-lo na fase certa da trilha com o `Passo N` correto.
- Atualizar o hero: contador `N / 17 publicados` e `progress-fill` width = `N/17 * 100`%.
- Manter o `mark` do card consistente com o `brand-mark` do manual.

## Estratégia de modelo

Padrão recente: **Opus 4.8** para todos os capítulos. Sob pedido de economia, alternar capítulos de referência prática (sintaxe, comandos, flags) para **Sonnet** e reservar Opus para os conceituais (modelos mentais, arquitetura, segurança, trade-offs).

## Versões de bibliotecas

Capítulos sobre bibliotecas mudam rápido. **Revalidar versões via npm** (`https://registry.npmjs.org/<pkg>/latest`) antes de fixar, e conferir notas de migração / deprecação. Registrar a data da verificação no callout. O padrão por baixo muda mais devagar que a API que o expõe.

## Git / deploy

Branch padrão `main`. Hospedagem GitHub Pages serve o repositório direto — `index.html` na raiz, manuais em `pages/`. Commitar só quando o usuário pedir.
