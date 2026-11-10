# Assets do perfil

Os SVGs são locais, sem scripts, fontes remotas ou imagens externas. O README usa HTML e Markdown compatíveis com o GitHub; os cards são imagens independentes para que possam quebrar de linha em telas menores.

- `banner.svg`: identidade visual, nome e composição orbital. Edite o texto diretamente no SVG, preservando o `viewBox`.
- `profile.jpg`: fotografia original, copiada sem alterações de `public/preview/perfil.jpeg` no repositório [Portfolio-rayssa](https://github.com/RayssaZsilva/Portfolio-rayssa), commit `49c2e24fb48c6f6d48e0c60379ad522d265ae7cf`. Não contém geração ou retoque de rosto.
- `link-*.svg`: botões visuais; seus destinos estão no README, fora dos SVGs, para manter os links clicáveis no GitHub.
- `project-*.svg`: cards de projetos. Ao editar descrições, atualize também o texto alternativo no README. SmartSeller e MedBox têm informações fornecidas pela autora, sem repositórios públicos confirmados.

## Cobrinha

A animação permanece externa aos assets: `https://raw.githubusercontent.com/RayssaZsilva/RayssaZsilva/output/snake.svg`.

O workflow `.github/workflows/main.yml` foi preservado integralmente: `Platane/snk/svg-only@v3` gera `dist/snake.svg`, e `crazy-max/ghaction-github-pages@v3.1.0` publica na branch `output`, com permissão `contents: write`. O agendamento e o acionamento manual também foram mantidos. O SVG existente contém animação; não foi substituído por uma imagem estática.

O gatilho de push existente aponta para `master`, embora a branch principal consultada seja `main`. Isso não foi alterado neste redesign. O cron existente é `* */12 * * *`: ele executa a cada minuto das horas 0 e 12 UTC, apesar do comentário dizer “every 12 hours”. Ambos os comportamentos foram preservados conforme solicitado; ajustes devem ser revisados separadamente.

## Validação e limites

Revisão local em Chromium, com Markdown renderizado por Marked e estilos de referência do GitHub: larguras de 375, 768 e 1440 px, nos temas claro e escuro, sem rolagem horizontal e com todas as imagens carregadas. Essa revisão local não equivale à renderização hospedada pelo GitHub.

Os links dos dois projetos públicos e a URL da cobrinha responderam corretamente. Portfólio, LinkedIn e serviços externos de estatísticas não puderam ser validados por causa da política de rede deste ambiente. Por isso, a seção de atividade usa links nativos do GitHub, sem gráficos externos de disponibilidade não verificada. A geração do workflow não foi disparada durante a revisão.
