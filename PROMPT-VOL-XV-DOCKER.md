# Prompt de continuidade — Volume XV (Docker), Caps 1–22 — para Claude Code

Cole este conteúdo no Claude Code para produzir o **Volume XV — Docker** da coleção FullStack Manual, do Capítulo 1 em diante. Leia também o `CLAUDE.md` na raiz — ele tem as convenções gerais da coleção.

---

## Contexto

Estou construindo a **FullStack Manual**: coleção de 17 manuais de referência fullstack em **português do Brasil**, cada um um arquivo HTML único e autocontido, com tema *dark warm*, syntax highlighting customizado e navegação estruturada. Hospedados em `https://vitormattosdev.github.io/FullStack-Manual/`.

O **Volume XIV — Git** já está estruturado (esqueleto). O **Volume XV — Docker** dá sequência à **Onda 4 — Ferramentas do ofício**: do versionamento do código (Git) à conteinerização do ambiente.

## Arquivo de trabalho

O esqueleto está em `pages/manual-docker.html` (~22 KB): head + CSS + JS reaproveitados, branding de Docker (brand-mark `Dk`, título "Docker"), sidebar completa com os 22 capítulos, hero novo e footer apontando para o **Volume XVI — Terminal & Bash**. Todo o trabalho é **edição direta deste arquivo único**.

Há um marcador `<!-- CHAPTERS_INSERT_HERE -->` logo após o hero, antes do `<footer>`. **Nenhum capítulo inserido ainda** (0 sections).

## Workflow operacional

**Gatilho:** eu digito **"continuar"** → você produz **UM capítulo por turno**, inserido por substituição exata do marcador:

```
<section class="chapter" id="...">...</section>

<!-- CHAPTERS_INSERT_HERE -->
```

**No Capítulo 22 (último), o marcador é REMOVIDO.** Se eu disser **"faça todos de forma autônoma"**, produza os 22 em sequência, validando cada um.

Use o `_insert.py` da raiz (ajustar `path` para `pages/manual-docker.html`): `python _insert.py capNN.html N [final]`.

## Estratégia de modelo

Padrão **Opus 4.8** para todos os capítulos. Sob pedido de economia, alternar capítulos de referência prática (comandos, flags do CLI) para Sonnet e reservar Opus para os conceituais (isolamento, layers, redes, segurança).

## Os 22 capítulos (IDs batem com a sidebar — NÃO alterar)

| # | Título | ID | Grupo |
|---|--------|----|-------|
| 1 | O que é conteinerização | `introducao` | Fundamentos |
| 2 | Imagens vs containers | `imagens-containers` | Fundamentos |
| 3 | A arquitetura do Docker Engine | `arquitetura` | Fundamentos |
| 4 | Primeiros containers | `primeiros-containers` | Fundamentos |
| 5 | Dockerfile: instruções | `dockerfile` | Imagens |
| 6 | Layers e cache de build | `layers-cache` | Imagens |
| 7 | Multi-stage builds | `multi-stage` | Imagens |
| 8 | Otimização de imagens | `otimizacao` | Imagens |
| 9 | Registries e tags | `registries` | Imagens |
| 10 | Ciclo de vida de containers | `ciclo-vida` | Runtime |
| 11 | Volumes e persistência | `volumes` | Runtime |
| 12 | Redes | `redes` | Runtime |
| 13 | Variáveis de ambiente e secrets | `env-secrets` | Runtime |
| 14 | Docker Compose | `compose` | Compose |
| 15 | Compose: múltiplos serviços | `compose-servicos` | Compose |
| 16 | Healthchecks e dependências | `healthchecks` | Compose |
| 17 | Segurança de containers | `seguranca` | Produção |
| 18 | Imagens enxutas e distroless | `distroless` | Produção |
| 19 | Logging e observabilidade | `logging` | Produção |
| 20 | CI/CD com Docker | `cicd` | Produção |
| 21 | Orquestração: além do Compose | `orquestracao` | Produção |
| 22 | Boas práticas (encerramento) | `producao` | Produção |

## Estrutura de cada capítulo, spans de highlight, callouts, tom, densidade

Ver `CLAUDE.md` (seção "Convenções de conteúdo"). Resumo: `chapter-number` + `chapter-title` (com `<em>`) + `chapter-intro` (modelo mental antes da sintaxe); 6–8 `<h3 class="topic">`; 5–7 blocos `code-wrap`; 2–3 callouts (`note`/`tip`/`warn`); 1 tabela de referência ao final. Comentários de código sempre em PT-BR. Filename típico nos blocos: `Dockerfile`, `docker-compose.yml`, `terminal`.

## Disciplina de escape HTML (CRÍTICA)

Dentro de `<pre><code>`, escape manual e cirúrgico (nunca regex em massa): `<`→`&lt;`, `>`→`&gt;`, `&`→`&amp;`, `&&`→`&amp;&amp;`. Pontos quentes deste volume:

- Shell em `RUN`/`CMD`: redirecionamentos `2>&1` → `2&gt;&amp;1`, pipes com `&&`
- `CMD ["node", "server.js"]` (JSON array) — aspas são seguras, mas confira
- Placeholders `<imagem>:<tag>`, `<container_id>` → `&lt;imagem&gt;:&lt;tag&gt;`
- YAML do Compose raramente tem `<`/`>`, mas portas `"3000:3000"` e env `${VAR}` são literais
- Escape duplo (`&amp;gt;`) é erro grave.

## Validação por capítulo e validação final

Ver `CLAUDE.md` (seções de validação). Resumo:

- **Por capítulo:** marcador==1, sections==N, tags balanceadas, typos==0, escape duplo==0, code sem `<`/`>` cru, arrows JS cruas==0 (raras aqui — Docker usa shell/YAML).
- **Salvaguarda:** não crie arquivos de backup; a validação por capítulo + commit no git cobrem o risco (ver `CLAUDE.md`).
- **Final (7 passos):** marcador removido, 22 sections, sidebar↔ids, tags balanceadas, typos/escape duplo==0, cauda `</script></body></html>`, ordem dos IDs e `Capítulo 1`–`22` sequenciais.

## Versões e convenções confirmadas (revalidar via web no Cap relevante)

- Docker Engine / CLI atual; **BuildKit** como builder padrão (mencionar `docker build` moderno e `docker buildx`).
- **Compose v2** (plugin `docker compose`, sem hífen — não o legado `docker-compose`).
- Imagens base: preferir tags específicas e enxutas (`node:22-alpine`, `-slim`), e **distroless** (`gcr.io/distroless/...`) no Cap 18.
- Segurança (Cap 17): usuário não-root (`USER`), `--read-only`, secrets fora da imagem, scan de vulnerabilidades.
- Comandos destrutivos (`docker system prune -a`, `-v` em volumes) sempre com callout `warn`.

## Continuidade temática

- **Cap 1** abre conectando ao Vol XIV (Git versiona o código; Docker empacota o ambiente) e ao stack da coleção: conteinerizar a app Hono+Drizzle+Postgres (Vols IX–XIII).
- **Caps 5–8 (imagens)** usam a app TypeScript dos volumes de backend como exemplo de build: `node:22-alpine`, multi-stage para compilar TS e descartar devDependencies.
- **Cap 11 (volumes)** e **Cap 12 (redes)** conectam ao Postgres (Vol X) conteinerizado — persistência de dados e comunicação entre containers app↔banco.
- **Caps 14–16 (Compose)** orquestram o stack completo (app + Postgres + Redis do Vol XIII/Cap 6) num `docker-compose.yml`.
- **Cap 17 (segurança)** revisita princípios do Vol XIII Cap 21 (menor privilégio, falhar fechado) aplicados a containers.
- **Cap 22 (encerramento)** fecha o volume e aponta para o **Volume XVI — Terminal & Bash** (a Onda 4 continua: do empacotamento do ambiente ao domínio do shell que o opera).

## Handoff ao final do Cap 22

Após o Cap 22, produzir: (a) esqueleto HTML do **Volume XVI — Terminal & Bash** (`_build_vol16.py` derivando do esqueleto Docker; brand-mark `Sh`, branding Bash, sidebar dos capítulos, hero novo, footer apontando para **Volume XVII — Regex**), e (b) `PROMPT-VOL-XVI-BASH.md` no mesmo formato. Atualizar o `index.html` tornando o card do Docker clicável (ver `CLAUDE.md`).

## Gatilho para começar

Quando eu disser **"continuar"**, produza o **Capítulo 1 — O que é conteinerização** e insira no marcador de `pages/manual-docker.html`. Ao final, anuncie o Cap 2.
