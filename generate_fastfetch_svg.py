import os

debian_ascii = [
    '       _,met$$$$$gg.',
    '    ,g$$$$$$$$$$$$$$$P.',
    '  ,g$$P"        """Y$$.',
    ' ,$$P\'              `$$$.',
    '\',$$P       ,ggs.     `$$b:',
    '`d$$\'     ,$P"\'   .    $$$',
    ' $$P      d$\'     ,    $$P',
    ' $$:      $$.   -    ,d$$\'',
    ' $$;      Y$b._   _,d$P\'',
    ' Y$$.      `."T$$$$P"\'',
    '  `$$b      "-.__',
    '   `Y$$b',
    '    `Y$$.',
    '      `$$b.',
    '        `Y$$b.',
    '          `"Y$b._',
    '              `"""'
]

specs = [
    ("header", "luis@backend-cluster"),
    ("divider", "--------------------"),
    ("Rol", "Desarrollador Backend & Bases de Datos"),
    ("Ubicación", "Colombia"),
    ("Stack", "TypeScript · Python · Go · Rust · NestJS · FastAPI · Next.js"),
    ("Bases Datos", "PostgreSQL · Redis · Prisma · Neon · Supabase"),
    ("DevOps & Cloud", "Docker · Nginx · Git · GitHub Actions · CI/CD · Render · Vercel"),
    ("Seguridad", "OWASP · Web & API Security · JWT · Authentication"),
    ("Herramientas", "VS Code · Obsidian · Expo · Android Studio"),
    ("Filosofía", "Diseño técnico sólido, baja latencia y máxima eficiencia"),
    ("Uptime", "99.9% (alimentado a café)")
]

ansi_colors_1 = ["#2e3436", "#cc0000", "#4e9a06", "#c4a000", "#3465a4", "#75507b", "#06989a", "#d3d7cf"]
ansi_colors_2 = ["#555753", "#ef2929", "#8ae234", "#fce94f", "#729fcf", "#ad7fa8", "#34e2e2", "#eeeeec"]

svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 490" width="100%" height="100%">']
svg.append('''<defs>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&amp;display=swap');
    .term-window { fill: #0d1117; stroke: #30363d; stroke-width: 1px; rx: 8px; }
    .titlebar { fill: #161b22; }
    .title-text { font-family: 'JetBrains Mono', monospace; font-size: 13px; fill: #d3d7cf; }
    .menu-bar { fill: #0d1117; stroke: #21262d; stroke-width: 1px; }
    .menu-text { font-family: 'JetBrains Mono', monospace; font-size: 12px; fill: #8b949e; }
    .mono { font-family: 'JetBrains Mono', monospace; font-size: 13px; white-space: pre; }
    .prompt-user { fill: #3fb950; font-weight: bold; }
    .prompt-cmd { fill: #ffffff; }
    .debian-red { fill: #ff4d4d; font-weight: bold; }
    .label-red { fill: #ff4d4d; font-weight: bold; }
    .val-white { fill: #e6edf3; }
    .header-user { fill: #ff4d4d; font-weight: bold; font-size: 14px; }
    .divider { fill: #ff4d4d; }
    .cursor { fill: #ffffff; animation: blink 1s step-start infinite; }
    @keyframes blink { 50% { opacity: 0; } }
  </style>
</defs>''')

# Background window
svg.append('<rect width="940" height="490" class="term-window" />')

# Titlebar
svg.append('<path d="M0,8 Q0,0 8,0 L932,0 Q940,0 940,8 L940,32 L0,32 Z" class="titlebar" />')
svg.append('<text x="25" y="21" class="title-text">Terminal - luis@backend-cluster: ~</text>')
# Window buttons on right
svg.append('<g transform="translate(860, 11)">')
svg.append('  <rect x="0" y="0" width="18" height="12" fill="none" stroke="#8b949e" stroke-width="1.5" />')
svg.append('  <rect x="25" y="0" width="14" height="12" fill="none" stroke="#8b949e" stroke-width="1.5" />')
svg.append('  <line x1="50" y1="0" x2="62" y2="12" stroke="#ff4d4d" stroke-width="1.5" />')
svg.append('  <line x1="62" y1="0" x2="50" y2="12" stroke="#ff4d4d" stroke-width="1.5" />')
svg.append('</g>')

# Menu bar
svg.append('<rect x="0" y="32" width="940" height="24" class="menu-bar" />')
svg.append('<text x="18" y="48" class="menu-text">Archivo    Editar    Ver    Terminal    Pestañas    Ayuda</text>')

# Fastfetch Command
svg.append('<g transform="translate(24, 82)" class="mono">')
svg.append('  <text><tspan class="prompt-user">luis@backend-cluster:~$</tspan> <tspan class="prompt-cmd">fastfetch</tspan></text>')
svg.append('</g>')

# Main content
y_start = 106
line_height = 19

# Render Debian ASCII logo on left
for i, line in enumerate(debian_ascii):
    y = y_start + (i * line_height)
    escaped_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    svg.append(f'<text x="24" y="{y}" class="mono debian-red">{escaped_line}</text>')

# Render specs on right
x_specs = 300
for i, item in enumerate(specs):
    y = y_start + (i * line_height)
    if item[0] == "header":
        svg.append(f'<text x="{x_specs}" y="{y}" class="mono header-user">{item[1]}</text>')
    elif item[0] == "divider":
        svg.append(f'<text x="{x_specs}" y="{y}" class="mono divider">{item[1]}</text>')
    else:
        label, val = item
        svg.append(f'<text x="{x_specs}" y="{y}" class="mono"><tspan class="label-red">{label}: </tspan><tspan class="val-white">{val}</tspan></text>')

# Color palette blocks below specs
palette_y1 = y_start + (len(specs) * line_height) + 10
palette_y2 = palette_y1 + 16

for idx, color in enumerate(ansi_colors_1):
    svg.append(f'<rect x="{x_specs + (idx * 30)}" y="{palette_y1}" width="30" height="15" fill="{color}" />')
for idx, color in enumerate(ansi_colors_2):
    svg.append(f'<rect x="{x_specs + (idx * 30)}" y="{palette_y2}" width="30" height="15" fill="{color}" />')

# Bottom prompt below Debian logo
final_y = 450
svg.append(f'<g transform="translate(24, {final_y})" class="mono">')
svg.append('  <text><tspan class="prompt-user">luis@backend-cluster:~$</tspan> <tspan class="cursor">█</tspan></text>')
svg.append('</g>')

svg.append('</svg>')

with open(r'C:\LuisGCarpio\fastfetch.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg))

print("Regenerated fastfetch.svg successfully")
