# Prompt de continuidade — Volume XIX (DevOps), Caps 1–22 — para Claude Code

Cole no Claude Code para produzir o **Volume XIX — DevOps**, o **último volume** da coleção, que fecha a **Onda 5 — Qualidade e Operação**. Leia também o `CLAUDE.md` na raiz.

---

## Contexto

**FullStack Manual**: coleção de manuais de referência fullstack em **português do Brasil**, HTML único autocontido, tema *dark warm*. Hospedados em `https://vitormattosdev.github.io/FullStack-Manual/`.

O DevOps é o **último volume (XIX de XIX)**. Os Testes (XVIII) garantiram que o software funciona; o DevOps garante que ele chega à produção e se mantém lá. Fecha a Onda 5 e a coleção inteira.

## Arquivo de trabalho

Esqueleto em `pages/manual-devops.html` (~22 KB): branding DevOps (brand-mark `Op`, título "DevOps"), sidebar com 22 capítulos. **Como é o último volume, o footer fecha a coleção** ("Volume final da coleção · ... 19 volumes"), sem apontar para um próximo. Marcador `<!-- CHAPTERS_INSERT_HERE -->` após o hero; **0 capítulos**.

## Workflow

"continuar" → UM capítulo por turno (no Cap 22, marcador REMOVIDO). "Faça todos de forma autônoma" → os 22 em sequência. **Antes de inserir, rode `python _check.py capNN.html`**; depois `python _insert.py pages/manual-devops.html capNN.html N [final]`.

## Estratégia de modelo

Padrão **Opus 4.8**. Conceituais (cultura DevOps, estratégias de deploy, observabilidade, incidentes) merecem Opus; referência prática (sintaxe de pipeline, comandos) pode ir a Sonnet sob pedido.

## Os 22 capítulos (IDs batem com a sidebar — NÃO alterar)

| # | Título | ID | Grupo |
|---|--------|----|-------|
| 1 | O que é DevOps | `introducao` | Fundamentos |
| 2 | Ambientes: dev, staging, prod | `ambientes` | Fundamentos |
| 3 | Configuração e segredos | `configuracao` | Fundamentos |
| 4 | Build e artefatos reproduzíveis | `build` | Fundamentos |
| 5 | Integração contínua | `ci` | CI/CD |
| 6 | Pipelines de CI/CD | `pipelines` | CI/CD |
| 7 | Entrega e implantação contínua | `cd` | CI/CD |
| 8 | Estratégias de deploy | `estrategias-deploy` | CI/CD |
| 9 | Rollback e feature flags | `rollback` | CI/CD |
| 10 | Plataformas de hospedagem | `plataformas` | Infraestrutura |
| 11 | Infraestrutura como código | `iac` | Infraestrutura |
| 12 | Containers em produção | `orquestracao` | Infraestrutura |
| 13 | Redes, DNS e TLS | `rede` | Infraestrutura |
| 14 | Bancos em produção | `banco-producao` | Infraestrutura |
| 15 | Os três pilares da observabilidade | `observabilidade` | Observabilidade |
| 16 | Logging estruturado | `logging` | Observabilidade |
| 17 | Métricas e dashboards | `metricas` | Observabilidade |
| 18 | Tracing distribuído | `tracing` | Observabilidade |
| 19 | Alertas e SLOs | `alertas` | Observabilidade |
| 20 | Resposta a incidentes | `incidentes` | Operação |
| 21 | Segurança em produção | `seguranca` | Operação |
| 22 | Boas práticas (encerramento) | `producao` | Operação |

## Estrutura, spans, callouts, tom, densidade

Ver `CLAUDE.md`. Filenames típicos: `deploy.yml`, `terraform.tf`, `docker-compose.prod.yml`, `terminal`. Comentários em PT-BR. Modelo mental antes da ferramenta: explique *por que* e *o conceito* (ex.: o que é IaC, o que é um SLO) antes da sintaxe.

## Disciplina de escape HTML (CRÍTICA)

Dentro de `<pre><code>`, escape `<`→`&lt;`, `>`→`&gt;`, `&`→`&amp;`. Pontos quentes:

- YAML de pipeline: `>-` (block scalar) → `&gt;-`; `${{ }}` é seguro
- Shell: `2>&1` → `2&gt;&amp;1`, `&&`/`||` → `&amp;&amp;`/`||`, `|` é seguro
- Setas em diagramas/comentários: `->` → `-&gt;`, `-->` → `--&gt;` (erro recorrente em todos os volumes)
- Comparações/HCL/config raramente têm `<`/`>`, mas confira heredocs e templates

`python _check.py capNN.html` antes de cada inserção pega isto.

## Validação e validação final

Ver `CLAUDE.md`. Não crie arquivos de backup. Validação final de 7 passos após o Cap 22.

## Convenções confirmadas (Jun/2026)

- **GitHub Actions** como CI/CD de referência (mais usado no ecossistema); mencionar GitLab CI onde relevante.
- **Plataformas**: Vercel (frontend/Next), Fly.io / Railway / Render (apps conteinerizadas), AWS/GCP como IaaS; serverless como categoria.
- **IaC**: Terraform como referência (e a categoria — Pulumi, etc.).
- **Observabilidade**: OpenTelemetry como padrão de instrumentação; Prometheus/Grafana (métricas), Loki/ELK (logs), Jaeger/Tempo (traces); Sentry para erros.
- Conectar ao stack: deploy da app Hono/Next conteinerizada (Vols IX/VII/XV), CI dos testes (Vol XVIII Cap 21), segredos (Vol XIII Cap 22), logging para stdout (Vol XV Cap 19).

## Continuidade temática

- **Cap 1** abre conectando a Testes (Vol XVIII: validar antes de sair; DevOps: entregar e operar) e à coleção: o stack inteiro enfim encontra os usuários. A cultura DevOps (dev + ops integrados).
- **Caps 5-9 (CI/CD)** aprofundam o que Vols XIV (Cap 19), XV (Cap 20) e XVIII (Cap 21) introduziram: o pipeline completo, com estratégias de deploy (blue-green/canary/rolling, revisitando Vol XV Cap 20) e feature flags (revisita Vol XIV Cap 18).
- **Caps 10-14 (infra)** usam Docker (Vol XV) e orquestração (Vol XV Cap 21); banco em produção conecta a Vols X-XI (migrations, backups — revisita Vol XV Cap 11).
- **Caps 15-19 (observabilidade)** expandem o que Vol XV (Cap 19) e Vol XIII (Cap 22) tocaram: os três pilares, logging estruturado (stdout, Vol XV), métricas, traces, alertas e SLOs.
- **Cap 21 (segurança em produção)** revisita Vol XIII (Cap 21 OWASP, menor privilégio) e Vol XV (Cap 17 segurança de containers), aplicados à operação.
- **Cap 22 (encerramento)** fecha o DevOps, a Onda 5, **e a coleção inteira** (19 volumes). Faça uma retrospectiva final: das 5 ondas (Fundamentos → Visual → Backend → Ferramentas → Qualidade e Operação), do código que funciona ao software operado em produção. A jornada completa.

## Handoff ao final do Cap 22

Como é o ÚLTIMO volume: (a) NÃO há próximo esqueleto; (b) tornar o card de DevOps clicável no `index.html` (Passo 19, contador **19/19**, progress **100%**); (c) atualizar `CLAUDE.md` (DevOps ✅, coleção completa em 19/19); (d) sugerir ao usuário uma varredura final de toda a coleção e o commit/push final.

## Gatilho para começar

Quando eu disser **"continuar"**, produza o **Capítulo 1 — O que é DevOps** e insira no marcador de `pages/manual-devops.html`. Ao final, anuncie o Cap 2.
