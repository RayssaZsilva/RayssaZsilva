# Artes do perfil

## Composição e manutenção

As artes principais têm fundo transparente. O retrato faz parte do cabeçalho, com recorte circular e uma conexão gráfica com o nome; os botões continuam sendo links HTML independentes. Não há CSS global, JavaScript, fontes remotas ou uma imagem única para todo o README.

- `banner.svg`: cabeçalho para desktop.
- `banner-mobile.svg`: composição própria para telas de até 600 px, selecionada por `<picture>`.
- `tech-*.svg`: seis tecnologias prioritárias, com ícones locais.
- `project-*.svg`: dois cards principais e duas faixas compactas para projetos adicionais.
- `link-*.svg`: botões transparentes de GitHub, portfólio e LinkedIn.

Os cards, botões e ícones adaptam as cores com `prefers-color-scheme`. Os dois cabeçalhos usam uma paleta fixa independente dessa preferência: nome em roxo e textos de apoio em malva, com acabamento fino. Assim, continuam legíveis quando o tema selecionado no GitHub difere da preferência do visualizador SVG, sem adicionar caixas ou fundo ao banner. As artes não dependem de fontes personalizadas ou imagens remotas. A biografia permanece em texto HTML; ferramentas complementares, descrições e links dos projetos também ficam disponíveis em blocos `<details>`, além dos textos alternativos nas imagens.

Para reconstruir todas as artes, a partir da raiz do repositório:

```sh
python3 scripts/build-profile-assets.py
```

O gerador usa somente a biblioteca padrão do Python e é determinístico. Edite títulos, descrições, estilos e coordenadas no script e execute-o novamente. Ao alterar informações, atualize também os textos alternativos e descrições no README.

## Fotografia e ícones

`profile.jpg` é a fotografia original copiada de `public/preview/perfil.jpeg` em [Portfolio-rayssa](https://github.com/RayssaZsilva/Portfolio-rayssa), commit `49c2e24fb48c6f6d48e0c60379ad522d265ae7cf`. O arquivo permanece inalterado. Os dois cabeçalhos incorporam esses mesmos bytes JPEG em uma URI de dados, dentro de um recorte SVG: não há geração, retoque ou substituição do rosto. Não são necessárias requisições externas para exibir a fotografia.

React, Python, FastAPI, TypeScript e Google Gemini usam paths de [Simple Icons](https://github.com/simple-icons/simple-icons), sob CC0. O ícone de GitHub vem de [Devicon](https://github.com/devicons/devicon/blob/master/icons/github/github-original.svg), sob a licença MIT reproduzida em `DEVICON-LICENSE.txt`. Os paths ficam no gerador, sem downloads durante sua execução. Os demais ícones e elementos gráficos são vetores personalizados para este perfil.

## Cobrinha preservada

O README mantém `https://raw.githubusercontent.com/RayssaZsilva/RayssaZsilva/output/snake.svg`. O workflow `.github/workflows/main.yml` permanece integralmente inalterado: actions, permissões, cron, disparo manual, saída `dist/snake.svg` e publicação na branch `output`. Não foi disparado durante a revisão.

Também permanecem os comportamentos anteriores: gatilho de push em `master`, embora a principal consultada seja `main`, e cron `* */12 * * *` (a cada minuto das horas 0 e 12 UTC). Ajustá-los está fora desta etapa visual.

## Revisão

Validação local em Chromium nos temas claro e escuro, a 320, 375, 768 e 1440 px, com todos os assets carregados, sem overflow horizontal e com os blocos expansíveis fechados e abertos. O cabeçalho mobile é selecionado até 600 px. Os limites de todos os textos nos SVGs e a integridade da fotografia incorporada foram conferidos.

SmartSeller e MedBox mantêm descrições fornecidas pela autora, sem links para repositórios não confirmados. Estatísticas externas continuam substituídas por links nativos do GitHub. A abertura automática de Pull Requests depende do acesso à API do GitHub; a política de rede deste ambiente bloqueia `api.github.com`.

### Conferência da branch publicada

O HTML sanitizado do README foi obtido da página da branch no GitHub com TLS validado: `<picture>`, sua fonte mobile, os dois blocos expansíveis, links e a URL da cobrinha foram preservados. Os 15 SVGs publicados foram baixados e comparados byte a byte aos locais. A revisão em oito cenários foi repetida usando esse HTML e os assets publicados. O retrato incorporado também renderizou com a política CSP enviada pelo serviço raw do GitHub.

A captura direta da página hospedada pelo navegador não foi possível: a confiança TLS do navegador falhou, e a revisão automática bloqueou o registro persistente de uma autoridade certificadora. Não foi desativada a validação TLS. As capturas desta revisão são locais, com o conteúdo servido pelo GitHub.

### Cabeçalhos simplificados e contraste

Os banners contêm apenas o nome, “Software Development | AI | Automation” e “Building experiences with code & creativity.”, com fotografia circular e moldura neon. A versão desktop usa três linhas; a mobile divide somente o nome em duas linhas para preservar o espaço do retrato. As caixas individuais e as linhas de conexão foram removidas.

O fundo continua transparente. O nome usa roxo sem contorno e peso 600; os textos de apoio usam malva em pesos 500 e 400, com acabamento de 0,35–0,4 unidade SVG. A família tipográfica prioriza a fonte de interface do sistema. `paint-order: stroke fill` mantém o interior das letras nítido, sem o aspecto de letras vazadas. Não há filtros ou sombras na fotografia, nem dependência da preferência de tema para escolher as cores dos banners.

A revisão usa fundos reais branco `#FFFFFF` e escuro `#0D1117`, com as preferências clara e escura do visualizador, incluindo combinações divergentes. Doze renderizações cobrem o desktop a 900 px e o mobile a 350 e 270 px. Os limites dos textos e a ausência de sobreposição com a foto/moldura são medidos no Chromium. Os dois SVGs não contêm retângulos. A fotografia original, os cards, os botões, o toolkit e o workflow da cobrinha são preservados. O texto alternativo do cabeçalho no README acompanha a nova redação.
