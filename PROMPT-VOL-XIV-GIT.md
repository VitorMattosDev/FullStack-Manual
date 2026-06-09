# Prompt de continuidade — Volume XIV (Git), Caps 1–22 — para Claude Code

Cole este conteúdo no Claude Code para produzir o **Volume XIV — Git** da coleção FullStack Manual, do Capítulo 1 em diante.

---

## Contexto

Estou construindo a **FullStack Manual**: coleção de 17 manuais de referência fullstack em **português do Brasil**, cada um um arquivo HTML único e autocontido, com tema *dark warm*, syntax highlighting customizado e navegação estruturada. Hospedados em `https://vitormattosdev.github.io/FullStack-Manual/`.

O **Volume XIII — Autenticação** está **completo e validado** (22 capítulos), e fechou a Onda 3 — Backend TypeScript. Inicio agora o **Volume XIV — Git**, que abre a **Onda 4**.

## Arquivo de trabalho

O esqueleto já está pronto em `pages/manual-git.html` (~21 KB): head + CSS + JS reaproveitados do Vol XIII, branding de Git (brand-mark `Gt`, título "Git"), sidebar completa com os 22 capítulos, hero novo e footer apontando para o **Volume XV — Docker**. Todo o trabalho é **edição direta deste arquivo único**.

Há um marcador `<!-- CHAPTERS_INSERT_HERE -->` posicionado logo após o hero, antes do `<footer>`. É nele que cada capítulo entra. **Nenhum capítulo foi inserido ainda** (0 sections).

## Workflow operacional

**Gatilho:** eu digito **"continuar"** → você produz **UM capítulo por turno**, e o insere substituindo:

```
<!-- CHAPTERS_INSERT_HERE -->
```

por:

```
<section class="chapter" id="...">...</section>

<!-- CHAPTERS_INSERT_HERE -->
```

**No Capítulo 22 (último), o marcador é REMOVIDO**, não reposto.

A inserção é feita por **substituição de string exata** (não regex em massa). Há um script reutilizável `_insert.py` na raiz (do Vol XIII) que pode ser adaptado: ele lê o capítulo de um arquivo temporário (`cap01.html` etc.), faz `replace(marker, chapter)`, salva e roda a validação por capítulo. **Atenção:** ajustar o `path` para `pages/manual-git.html`.

Se eu disser **"faça todos de forma autônoma"**, produza os 22 em sequência sem esperar gatilho, validando cada um.

## Estratégia de modelo

Por padrão, **Opus 4.8** para todos os capítulos (foi o pedido no Vol XIII). Se eu pedir economia, alterne capítulos de referência prática (comandos, flags) para Sonnet e reserve Opus para os conceituais (modelo de objetos, merge vs rebase, workflows).

## Os 22 capítulos (IDs batem com a sidebar de `pages/manual-git.html` — NÃO alterar)

| # | Título | ID | Grupo |
|---|--------|----|-------|
| 1 | O modelo de dados do Git | `introducao` | Fundamentos |
| 2 | Repositório, working tree e staging | `repositorio` | Fundamentos |
| 3 | Commits e o grafo de objetos | `commits` | Fundamentos |
| 4 | O índice (staging area) | `indice` | Fundamentos |
| 5 | Branches e referências | `branches` | Branches e história |
| 6 | HEAD e detached HEAD | `head` | Branches e história |
| 7 | Merge | `merge` | Branches e história |
| 8 | Rebase | `rebase` | Branches e história |
| 9 | Cherry-pick e revert | `cherry-pick` | Branches e história |
| 10 | Remotos e tracking branches | `remotos` | Trabalho remoto |
| 11 | Fetch, pull e push | `fetch-pull-push` | Trabalho remoto |
| 12 | Resolução de conflitos | `conflitos` | Trabalho remoto |
| 13 | Stash | `stash` | Ferramentas |
| 14 | Reflog e recuperação | `reflog` | Ferramentas |
| 15 | Reset, restore e checkout | `reset-restore` | Ferramentas |
| 16 | Tags e versionamento | `tags` | Ferramentas |
| 17 | .gitignore e atributos | `gitignore` | Ferramentas |
| 18 | Workflows de branching | `workflows` | Colaboração |
| 19 | Pull requests e code review | `pull-requests` | Colaboração |
| 20 | Hooks | `hooks` | Colaboração |
| 21 | Bisect e arqueologia | `bisect` | Colaboração |
| 22 | Boas práticas (encerramento) | `producao` | Colaboração |

## Estrutura de cada capítulo

```html
<section class="chapter" id="ID">
  <div class="chapter-number">Capítulo N</div>
  <h2 class="chapter-title">Título com <em>palavra</em></h2>
  <p class="chapter-intro">Parágrafo de abertura: modelo mental antes do comando.</p>

  <h3 class="topic"><span class="hash">#</span> Subtítulo</h3>
  <p>...</p>

  <div class="code-wrap">
    <div class="code-header"><span class="filename">terminal</span><button class="copy-btn">Copiar</button></div>
    <pre><code>... (syntax highlight em spans) ...</code></pre>
  </div>

  <div class="callout note">  <!-- ou tip | warn -->
    <div class="callout-label">Rótulo</div>
    <div class="callout-body">...</div>
  </div>

  <!-- ao final: tabela de referência -->
  <div class="table-wrap"><table><thead>...</thead><tbody>...</tbody></table></div>
</section>
```

**Spans de syntax highlight** (dentro de `<code>`): `cm` (comentário), `kw` (keyword), `st` (string), `nm` (número), `cl` (classe/tipo), `fn` (função/subcomando), `pr` (propriedade/flag), `op` (operador). Para blocos de terminal/shell, use `cm` para comentários (`# ...`), `kw` para o binário (`git`), `fn` para o subcomando (`commit`, `rebase`), `pr` para flags (`--amend`), `st` para argumentos string. Mantenha o mesmo vocabulário de spans do Vol XIII — não introduza classes novas (`at`/`dr`/`tg` não estão em uso).

**Callouts em uso:** `note`, `tip`, `warn`.

**Tom:** prosa enxuta, modelo mental antes da sintaxe. Evitar "vamos explorar" e "imagine que". Comentários de código/terminal sempre em PT-BR. Git é uma ferramenta de **modelo de dados** — sempre que possível, explique a estrutura (grafo de commits, refs, índice) antes do comando que a manipula.

**Densidade típica:** 6–8 `<h3 class="topic">`, 5–7 blocos de código, 2–3 callouts, 1 tabela de referência ao final (5–7 linhas). Cada capítulo adiciona ~14–20 KB.

## Disciplina de escape HTML (CRÍTICA)

Dentro de `<pre><code>`, **todo** caractere especial é escapado:

- `<` → `&lt;` · `>` → `&gt;` · `&` → `&amp;`
- `&&` → `&amp;&amp;`
- Redirecionamentos e pipes em shell: `2>&1` → `2&gt;&amp;1`, `<file` → `&lt;file`
- Comparações e setas em saída de diff/log: `<<<<<<<`, `=======`, `>>>>>>>` (marcadores de conflito) → escapar cada `<`/`>`
- Refspecs e ranges: `HEAD~3`, `main..feature`, `origin/main` são seguros, mas `<commit>` (placeholder) → `&lt;commit&gt;`
- URLs em comentários com múltiplos params: `?a=1&b=2` → `?a=1&amp;b=2`

**Nunca** use regex em massa para escapar — escape cirúrgico, manual. Escape duplo (`&amp;gt;`) é erro grave. **Atenção especial aos marcadores de conflito** (`<<<<<<<`, `>>>>>>>`) no Cap 12 — são a maior fonte de `<`/`>` cru neste volume.

## Validação por capítulo (rodar APÓS cada inserção)

Adaptar o `_insert.py` do Vol XIII (mudar `path` para `pages/manual-git.html`). Ele já checa:

1. marcador `CHAPTERS_INSERT_HERE` == 1 (ou 0 no Cap 22)
2. nº de `<section class="chapter">` == N esperado
3. tags balanceadas (`section`, `pre`, `code`, `div`, `span`) via regex de abertura assimétrica `<tag[\s>]` vs `</tag>`
4. typos == 0: `<pre">`, `<code">`, `<span">`, `<div">`
5. escape duplo == 0: `&amp;gt;`, `&amp;lt;`, `&amp;amp;`
6. dentro de cada `<pre><code>`: removidos spans e entidades, resíduo de `<`/`>` cru == 0
7. (este volume usa shell, não JS) — checar arrows não se aplica; em vez disso, atenção redobrada ao passo 6 com marcadores de conflito

## Salvaguarda

Não crie arquivos de backup — a validação por capítulo já impede corrupção silenciosa, e o git é o ponto de restauração (commit ao concluir o manual). Ver `CLAUDE.md`.

## Validação final — 7 passos (após o Cap 22)

1. marcador removido (0 ocorrências)
2. 22 `<section class="chapter">`
3. cross-check: 22 hrefs da sidebar ↔ 22 section ids, zero divergência
4. tags balanceadas (section, pre, code, div, span)
5. typos == 0, escape duplo == 0
6. cauda == `</script></body></html>` (com `</main></div>` antes)
7. varredura global: 0 blocos `<code>` com `<`/`>` cru; ordem dos 22 IDs correta; `Capítulo 1`–`22` sequenciais

## Convenções de conteúdo confirmadas (Jun/2026)

- Git moderno: branch padrão **`main`** (não `master`). `git switch`/`git restore` preferidos a `git checkout` para clareza didática, mas explicar `checkout` por ser onipresente (Cap 15).
- Plataformas: GitHub como referência primária (PRs, Actions). Mencionar GitLab (MRs) e Bitbucket onde relevante, sem aprofundar.
- `git config` com `pull.rebase`, `init.defaultBranch=main`, `core.autocrlf` (relevante no Windows — o usuário está em Windows 11).
- Comandos destrutivos (`reset --hard`, `push --force`, `rebase`) sempre com callout `warn` e a alternativa segura (`--force-with-lease`, `revert`).

## Continuidade temática (referências a fixar)

- **Cap 1 (modelo de dados)** abre conectando ao Vol XIII: o Git versiona todo o código de autenticação escrito. Estabelece blob/tree/commit como grafo de objetos imutáveis endereçados por hash (SHA). Modelo mental antes de qualquer comando.
- **Cap 3 (commits)** aprofunda o grafo: commit = snapshot + parent(s) + metadados; hash como identidade imutável; por que reescrever história cria commits novos.
- **Caps 7–8 (merge/rebase)** são o par conceitual central — merge preserva história (commit de merge, dois parents), rebase reescreve (replay linear). Capítulo denso: dedicar o contraste e quando usar cada um. "Não rebaseie história pública" é o callout `warn` obrigatório.
- **Cap 12 (conflitos)** é o capítulo de maior risco de escape HTML (marcadores `<<<<<<<`/`>>>>>>>`). Conectar a merge (7) e rebase (8).
- **Caps 18–19 (workflows/PRs)** fecham com colaboração: Git Flow vs trunk-based; PR como unidade de revisão; conectar ao code review e à autorização do Vol XIII (quem aprova merge).
- **Cap 22 (encerramento)** fecha o volume e aponta para o **Volume XV — Docker** (Onda 4 continua: do versionamento do código à conteinerização do ambiente).

## Handoff ao final do Cap 22

Após o Cap 22, produzir: (a) esqueleto HTML do **Volume XV — Docker** (mesma técnica: `_build_vol15.py` reaproveitando head/CSS/JS, brand-mark `Do`, branding Docker, sidebar dos capítulos de Docker, hero novo, footer apontando para **Volume XVI**), e (b) um prompt de inicialização `.md` no mesmo formato deste.

## Gatilho para começar

Quando eu disser **"continuar"**, produza o **Capítulo 1 — O modelo de dados do Git** e insira no marcador de `pages/manual-git.html`. Ao final, anuncie o Cap 2.
