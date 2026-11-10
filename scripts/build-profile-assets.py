"""Build transparent profile artwork with the original, unmodified JPEG.

No network or third-party packages required. SVGs keep native text and vector
icons; only the portrait is embedded as its original JPEG bytes.
"""
from pathlib import Path
from html import escape
import base64

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
STYLE = '''<style>
.text{fill:#28183d}.muted{fill:#59456f}.accent{fill:#7138c5}
.line{stroke:#9364c4}.surface{fill:#8b5cf6;fill-opacity:.035}
@media(prefers-color-scheme:dark){
.text{fill:#f8f7ff}.muted{fill:#c0b3d3}.accent{fill:#c4b5fd}
.line{stroke:#72518f}.surface{fill:#c4b5fd;fill-opacity:.035}}
text{font-family:Arial,Helvetica,sans-serif}
</style>'''
DEFS = '''<defs>
<linearGradient id="neon"><stop stop-color="#8B5CF6"/><stop offset="1" stop-color="#EC4899"/></linearGradient>
<radialGradient id="halo"><stop stop-color="#a855f7" stop-opacity=".18"/><stop offset="1" stop-color="#a855f7" stop-opacity="0"/></radialGradient>
</defs>'''

# Banners must also work when GitHub's selected theme and the SVG viewer's
# prefers-color-scheme differ. Keep a fixed, measured palette for these two
# assets instead of relying on the viewer to choose the correct text color.
BANNER_STYLE = '''<style>
text{font-family:Inter,"Segoe UI",Arial,Helvetica,sans-serif;paint-order:stroke fill;stroke-linejoin:round}
.name{fill:#8B5CF6;stroke:#F3EAFF;stroke-width:.7;font-weight:750}
.label{fill:#A277D8;stroke:#301A42;stroke-width:.85;font-weight:650}
.caption{fill:#A277D8;stroke:#301A42;stroke-width:.8;font-weight:600}
</style>'''

def write(name, w, h, title, body):
    style = BANNER_STYLE if name in ('banner.svg', 'banner-mobile.svg') else STYLE
    (ASSETS / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>{style}{DEFS}{body}</svg>\n')

def text(x, y, content, size=16, cls='text', weight=400, extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" class="{cls}" {extra}>{escape(content)}</text>'

portrait = base64.b64encode((ASSETS / 'profile.jpg').read_bytes()).decode()

def photo(cx, cy, r):
    # The JPEG bytes are embedded unchanged. Only the SVG viewport clips them.
    return f'''<defs><clipPath id="portrait"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath></defs>
<circle cx="{cx}" cy="{cy}" r="{r+25}" fill="url(#halo)"/>
<circle cx="{cx}" cy="{cy}" r="{r+9}" fill="none" stroke="url(#neon)" stroke-width="1.5"/>
<image x="{cx-r}" y="{cy-r-20}" width="{2*r}" height="{2*r*1447/1087:.3f}" href="data:image/jpeg;base64,{portrait}" clip-path="url(#portrait)"/>
<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#c4b5fd" stroke-opacity=".4"/>
<circle cx="{cx+r*.75}" cy="{cy-r*.75}" r="5" fill="#ec4899"/>
'''

BANNER_TITLE = 'Rayssa Cardoso — Software Development | AI | Automation. Building experiences with code & creativity.'

# Three lines, a transparent canvas and a single quiet neon portrait frame.
body = photo(753, 123, 100)
body += text(24, 100, 'Rayssa Cardoso', 65, 'name', 750, 'letter-spacing="-1.8"')
body += text(27, 145, 'Software Development | AI | Automation', 24, 'label', 650)
body += text(27, 185, 'Building experiences with code & creativity.', 21, 'caption', 600)
write('banner.svg', 900, 246, BANNER_TITLE, body)

# Keep the name alongside the portrait, then use the full width below them.
body = photo(305, 88, 66)
body += text(18, 79, 'Rayssa', 44, 'name', 750, 'letter-spacing="-1"')
body += text(18, 128, 'Cardoso', 44, 'name', 750, 'letter-spacing="-1"')
body += text(18, 191, 'Software Development | AI | Automation', 19, 'label', 650)
body += text(18, 228, 'Building experiences with code & creativity.', 18, 'caption', 600)
write('banner-mobile.svg', 400, 255, BANNER_TITLE, body)

# Project artwork: transparent canvas, a light wash and precise corner accents.
ICONS = {
    'chat': '<path d="M12 14h45v31H36L25 56V45H12zM27 24l4 7-4 7m12-14-4 7 4 7"/>',
    'stay': '<path d="M15 56V17h34v39M9 56h46M28 56V43h9v13M23 25h3m11 0h3m-17 8h3m11 0h3"/><path d="m38 9 8-5 8 5v10l-8 5-8-5z"/>',
    'auto': '<path d="M12 21h36l-7-7m7 7-7 7M50 44H14l7 7m-7-7 7-7M22 30h20v9H22z"/>',
    'med': '<rect x="15" y="12" width="35" height="43" rx="6"/><path d="M26 33h13m-6-6v13M24 19h17M28 49h10"/>'
}

def icon(name, x, y, scale=1):
    return f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="url(#neon)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>'

main = [
    ('chat-rai','chat','01 / INTELIGÊNCIA ARTIFICIAL','Chat rAI','Uma conversa entre código & IA.',
     ['IA generativa, histórico contextual e', 'consulta de projetos públicos do GitHub.'],
     ['React · Python · FastAPI','JavaScript · Gemini API']),
    ('acho','stay','02 / EXPERIÊNCIA WEB','Achô','Achou. Explorou. Descobriu.',
     ['Hospedagens, favoritos e telas de acesso.', 'Pesquisa e detalhes com dados locais.'],
     ['React · TypeScript · Vite','React Router · LocalStorage'])
]
for slug, glyph, category, title, subtitle, desc, stack in main:
    body = '<rect x="1" y="1" width="398" height="300" rx="18" class="surface"/>'
    body += '<circle cx="331" cy="68" r="98" fill="url(#halo)"/>'
    body += '<path d="M20 1h110M1 20v70M270 301h110q19 0 19-19v-55" fill="none" stroke="url(#neon)" stroke-width="1.5"/>'
    body += '<path d="M150 1h230q19 0 19 19v186M1 112v170q0 19 19 19h227" fill="none" class="line" stroke-opacity=".45"/>'
    body += text(22, 31, category, 10, 'accent', 700, 'letter-spacing="1"')
    body += icon(glyph, 307, 40)
    body += text(20, 104, title, 43, 'text', 700, 'letter-spacing="-1"')
    body += text(22, 133, subtitle, 15, 'accent', 600)
    for i, line in enumerate(desc): body += text(22, 170+22*i, line, 15, 'muted')
    body += '<path d="M22 212h352" class="line" stroke-opacity=".4"/>'
    for i, line in enumerate(stack): body += text(22, 235+19*i, line, 13, 'accent', 600)
    body += text(22, 282, 'VER PROJETO', 11, 'accent', 700, 'letter-spacing="1.5"')
    body += '<path d="M340 277h33m-7-7 7 7-7 7" fill="none" stroke="url(#neon)" stroke-width="1.5"/>'
    write(f'project-{slug}.svg', 400, 302, f'{title} — {subtitle} {" ".join(desc)} {"; ".join(stack)}. Ver repositório.', body)

additional = [
    ('smartseller','auto','SmartSeller','Integrações com Mercado Livre.', 'Autenticação · Gerenciamento · Automação'),
    ('medbox','med','MedBox 1.0','Lembretes com horários configuráveis.', 'ESP32 · MicroPython · LCD · Buzzer · LEDs')
]
for slug,glyph,title,desc,stack in additional:
    body = '<path d="M1 12v100M15 119h370" class="line" stroke-opacity=".5" fill="none"/>'
    body += icon(glyph, 7, 10, .75)
    body += text(66, 32, title, 24, 'text', 700)
    body += text(66, 55, desc, 13, 'muted')
    body += text(16, 82, stack, 12, 'accent', 600)
    body += text(16, 104, 'Repositório público ainda não confirmado', 11, 'muted')
    write(f'project-{slug}.svg',400,124,f'{title}. {desc} {stack}. Repositório público não confirmado.',body)

# Local logo paths, vendored from Simple Icons (CC0) and Devicon (MIT).
LOGOS = {}
LOGOS['react'] = ('0 0 24 24', ['M14.23 12.004a2.236 2.236 0 0 1-2.235 2.236 2.236 2.236 0 0 1-2.236-2.236 2.236 2.236 0 0 1 2.235-2.236 2.236 2.236 0 0 1 2.236 2.236zm2.648-10.69c-1.346 0-3.107.96-4.888 2.622-1.78-1.653-3.542-2.602-4.887-2.602-.41 0-.783.093-1.106.278-1.375.793-1.683 3.264-.973 6.365C1.98 8.917 0 10.42 0 12.004c0 1.59 1.99 3.097 5.043 4.03-.704 3.113-.39 5.588.988 6.38.32.187.69.275 1.102.275 1.345 0 3.107-.96 4.888-2.624 1.78 1.654 3.542 2.603 4.887 2.603.41 0 .783-.09 1.106-.275 1.374-.792 1.683-3.263.973-6.365C22.02 15.096 24 13.59 24 12.004c0-1.59-1.99-3.097-5.043-4.032.704-3.11.39-5.587-.988-6.38-.318-.184-.688-.277-1.092-.278zm-.005 1.09v.006c.225 0 .406.044.558.127.666.382.955 1.835.73 3.704-.054.46-.142.945-.25 1.44-.96-.236-2.006-.417-3.107-.534-.66-.905-1.345-1.727-2.035-2.447 1.592-1.48 3.087-2.292 4.105-2.295zm-9.77.02c1.012 0 2.514.808 4.11 2.28-.686.72-1.37 1.537-2.02 2.442-1.107.117-2.154.298-3.113.538-.112-.49-.195-.964-.254-1.42-.23-1.868.054-3.32.714-3.707.19-.09.4-.127.563-.132zm4.882 3.05c.455.468.91.992 1.36 1.564-.44-.02-.89-.034-1.345-.034-.46 0-.915.01-1.36.034.44-.572.895-1.096 1.345-1.565zM12 8.1c.74 0 1.477.034 2.202.093.406.582.802 1.203 1.183 1.86.372.64.71 1.29 1.018 1.946-.308.655-.646 1.31-1.013 1.95-.38.66-.773 1.288-1.18 1.87-.728.063-1.466.098-2.21.098-.74 0-1.477-.035-2.202-.093-.406-.582-.802-1.204-1.183-1.86-.372-.64-.71-1.29-1.018-1.946.303-.657.646-1.313 1.013-1.954.38-.66.773-1.286 1.18-1.868.728-.064 1.466-.098 2.21-.098zm-3.635.254c-.24.377-.48.763-.704 1.16-.225.39-.435.782-.635 1.174-.265-.656-.49-1.31-.676-1.947.64-.15 1.315-.283 2.015-.386zm7.26 0c.695.103 1.365.23 2.006.387-.18.632-.405 1.282-.66 1.933-.2-.39-.41-.783-.64-1.174-.225-.392-.465-.774-.705-1.146zm3.063.675c.484.15.944.317 1.375.498 1.732.74 2.852 1.708 2.852 2.476-.005.768-1.125 1.74-2.857 2.475-.42.18-.88.342-1.355.493-.28-.958-.646-1.956-1.1-2.98.45-1.017.81-2.01 1.085-2.964zm-13.395.004c.278.96.645 1.957 1.1 2.98-.45 1.017-.812 2.01-1.086 2.964-.484-.15-.944-.318-1.37-.5-1.732-.737-2.852-1.706-2.852-2.474 0-.768 1.12-1.742 2.852-2.476.42-.18.88-.342 1.356-.494zm11.678 4.28c.265.657.49 1.312.676 1.948-.64.157-1.316.29-2.016.39.24-.375.48-.762.705-1.158.225-.39.435-.788.636-1.18zm-9.945.02c.2.392.41.783.64 1.175.23.39.465.772.705 1.143-.695-.102-1.365-.23-2.006-.386.18-.63.406-1.282.66-1.933zM17.92 16.32c.112.493.2.968.254 1.423.23 1.868-.054 3.32-.714 3.708-.147.09-.338.128-.563.128-1.012 0-2.514-.807-4.11-2.28.686-.72 1.37-1.536 2.02-2.44 1.107-.118 2.154-.3 3.113-.54zm-11.83.01c.96.234 2.006.415 3.107.532.66.905 1.345 1.727 2.035 2.446-1.595 1.483-3.092 2.295-4.11 2.295-.22-.005-.406-.05-.553-.132-.666-.38-.955-1.834-.73-3.703.054-.46.142-.944.25-1.438zm4.56.64c.44.02.89.034 1.345.034.46 0 .915-.01 1.36-.034-.44.572-.895 1.095-1.345 1.565-.455-.47-.91-.993-1.36-1.565z'])
LOGOS['python'] = ('0 0 24 24', ['M11.858 0c-.978.005-1.913.088-2.736.234C6.7.662 6.26 1.558 6.26 3.21v2.182h5.725v.727H4.111c-1.664 0-3.121 1-3.577 2.903-.526 2.181-.549 3.542 0 5.82.407 1.694 1.379 2.902 3.043 2.902h1.969v-2.616c0-1.89 1.635-3.557 3.576-3.557h5.72c1.591 0 2.862-1.31 2.862-2.91v-5.45c0-1.553-1.309-2.718-2.863-2.977A18 18 0 0 0 11.858 0M8.762 1.755c.591 0 1.074.491 1.074 1.095 0 .601-.483 1.087-1.074 1.087A1.08 1.08 0 0 1 7.688 2.85c0-.604.48-1.095 1.074-1.095m9.656 4.364v2.543c0 1.971-1.671 3.63-3.577 3.63H9.122c-1.566 0-2.862 1.34-2.862 2.91v5.452c0 1.551 1.349 2.464 2.862 2.91 1.813.532 3.55.628 5.72 0 1.44-.418 2.862-1.258 2.862-2.91V18.47h-5.719v-.727h8.582c1.664 0 2.284-1.16 2.862-2.903.598-1.793.573-3.518 0-5.819-.41-1.656-1.196-2.903-2.862-2.903zm-3.216 13.807a1.08 1.08 0 0 1 1.074 1.088c0 .604-.48 1.094-1.074 1.094-.592 0-1.075-.49-1.075-1.094 0-.601.483-1.088 1.075-1.088'])
LOGOS['fastapi'] = ('0 0 24 24', ['M12 .0387C5.3729.0384.0003 5.3931 0 11.9988c-.001 6.6066 5.372 11.9628 12 11.9625 6.628.0003 12.001-5.3559 12-11.9625-.0003-6.6057-5.3729-11.9604-12-11.96m-.829 5.4153h7.55l-7.5805 5.3284h5.1828L5.279 18.5436q2.9466-6.5444 5.892-13.0896'])
LOGOS['typescript'] = ('0 0 24 24', ['M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z'])
LOGOS['gemini'] = ('0 0 24 24', ['M11.04 19.32Q12 21.51 12 24q0-2.49.93-4.68.96-2.19 2.58-3.81t3.81-2.55Q21.51 12 24 12q-2.49 0-4.68-.93a12.3 12.3 0 0 1-3.81-2.58 12.3 12.3 0 0 1-2.58-3.81Q12 2.49 12 0q0 2.49-.96 4.68-.93 2.19-2.55 3.81a12.3 12.3 0 0 1-3.81 2.58Q2.49 12 0 12q2.49 0 4.68.96 2.19.93 3.81 2.55t2.55 3.81'])
LOGOS['github'] = ('0 0 128 128', ['M64 5.103c-33.347 0-60.388 27.035-60.388 60.388 0 26.682 17.303 49.317 41.297 57.303 3.017.56 4.125-1.31 4.125-2.905 0-1.44-.056-6.197-.082-11.243-16.8 3.653-20.345-7.125-20.345-7.125-2.747-6.98-6.705-8.836-6.705-8.836-5.48-3.748.413-3.67.413-3.67 6.063.425 9.257 6.223 9.257 6.223 5.386 9.23 14.127 6.562 17.573 5.02.542-3.903 2.107-6.568 3.834-8.076-13.413-1.525-27.514-6.704-27.514-29.843 0-6.593 2.36-11.98 6.223-16.21-.628-1.52-2.695-7.662.584-15.98 0 0 5.07-1.623 16.61 6.19C53.7 35 58.867 34.327 64 34.304c5.13.023 10.3.694 15.127 2.033 11.526-7.813 16.59-6.19 16.59-6.19 3.287 8.317 1.22 14.46.593 15.98 3.872 4.23 6.215 9.617 6.215 16.21 0 23.194-14.127 28.3-27.574 29.796 2.167 1.874 4.097 5.55 4.097 11.183 0 8.08-.07 14.583-.07 16.572 0 1.607 1.088 3.49 4.148 2.897 23.98-7.994 41.263-30.622 41.263-57.294C124.388 32.14 97.35 5.104 64 5.104z', 'M26.484 91.806c-.133.3-.605.39-1.035.185-.44-.196-.685-.605-.543-.906.13-.31.603-.395 1.04-.188.44.197.69.61.537.91zm2.446 2.729c-.287.267-.85.143-1.232-.28-.396-.42-.47-.983-.177-1.254.298-.266.844-.14 1.24.28.394.426.472.984.17 1.255zM31.312 98.012c-.37.258-.976.017-1.35-.52-.37-.538-.37-1.183.01-1.44.373-.258.97-.025 1.35.507.368.545.368 1.19-.01 1.452zm3.261 3.361c-.33.365-1.036.267-1.552-.23-.527-.487-.674-1.18-.343-1.544.336-.366 1.045-.264 1.564.23.527.486.686 1.18.333 1.543zm4.5 1.951c-.147.473-.825.688-1.51.486-.683-.207-1.13-.76-.99-1.238.14-.477.823-.7 1.512-.485.683.206 1.13.756.988 1.237zm4.943.361c.017.498-.563.91-1.28.92-.723.017-1.308-.387-1.315-.877 0-.503.568-.91 1.29-.924.717-.013 1.306.387 1.306.88zm4.598-.782c.086.485-.413.984-1.126 1.117-.7.13-1.35-.172-1.44-.653-.086-.498.422-.997 1.122-1.126.714-.123 1.354.17 1.444.663zm0 0'])
for slug,label in [('react','React'),('python','Python'),('fastapi','FastAPI'),('typescript','TypeScript'),('gemini','Gemini'),('github','GitHub')]:
    view,paths=LOGOS[slug]
    vw=float(view.split()[2])
    body = '<rect x=".5" y=".5" width="123" height="71" rx="12" fill="none" class="line" stroke-opacity=".5"/>'
    body += f'<g transform="translate(48 10) scale({28/vw})" class="accent">'+''.join(f'<path d="{d}"/>' for d in paths)+'</g>'
    body += text(62, 59, label, 13, 'text', 600, 'text-anchor="middle"')
    write(f'tech-{slug}.svg', 124, 72, label, body)

# Social buttons are transparent and inherit the same adaptive palette.
for name,label,paths in [
    ('github','GitHub','<path d="m14 13-4 5 4 5m14-10 4 5-4 5m-7-12-4 16"/>'),
    ('portfolio','Portfólio','<rect x="10" y="11" width="20" height="15" rx="3"/><path d="M16 11V8h8v3m-14 7h20m-11-2v4"/>'),
    ('linkedin','LinkedIn','<path d="M12 15v11m0-17v1m7 16V15m0 5c0-7 9-7 9 0v6"/>')]:
    body='<rect x=".5" y=".5" width="111" height="35" rx="8" fill="none" stroke="url(#neon)" stroke-opacity=".75"/>'
    body+=f'<g fill="none" class="line" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{paths}</g>'
    body+=text(40,23,label,13,'text',600)
    write(f'link-{name}.svg',112,36,label,body)
