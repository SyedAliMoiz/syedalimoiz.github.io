with open('index.html', 'r') as f:
    html = f.read()

# 1. Skip button — dark bg, light gray text, hugging bottom-right corner
html = html.replace(
    'z-index:15; opacity:0.5; font-size:0.7rem; letter-spacing:0.12em; text-transform:uppercase; color:var(--muted); cursor:pointer; transition: opacity 0.3s ease, background 0.3s ease; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.12); border-radius: 999px; padding: 0.5em 1.2em;',
    'z-index:15; opacity:0.7; font-size:0.7rem; letter-spacing:0.12em; text-transform:uppercase; color: #b8b0a2; cursor:pointer; transition: opacity 0.3s ease; background: rgba(22,19,15,0.85); border: 1px solid rgba(255,255,255,0.1); border-radius: 6px; padding: 0.6em 1.1em;'
)
# Move to absolute bottom-right corner with minimal margin
html = html.replace(
    "bottom: max(3.2rem, calc(env(safe-area-inset-bottom) + 2rem)); right: max(1.4rem, env(safe-area-inset-right));",
    "bottom: max(0.8rem, env(safe-area-inset-bottom)); right: max(0.8rem, env(safe-area-inset-right));"
)
# Update hover
html = html.replace(
    'onmouseenter="this.style.opacity=0.6" onmouseleave="this.style.opacity=0.35"',
    'onmouseenter="this.style.opacity=1" onmouseleave="this.style.opacity=0.7"'
)
# Change text
html = html.replace('>skip to portfolio</div>', '>Skip to Portfolio</div>')

# 2. Fix the 9M beat — "CEOs and founders reach" on one line, not split
html = html.replace(
    "That\xe2\x80\x99s how he helped\\nCEOs and Founders reach\\n\xe2\x9f\xa69 million people\xe2\x9f\xa7 across 10+ industries.",
    "That\xe2\x80\x99s how he was able to help\\nCEOs and founders reach\\n\xe2\x9f\xa69 million people\xe2\x9f\xa7 across 10+ industries."
)

with open('index.html', 'w') as f:
    f.write(html)
print('Done')
