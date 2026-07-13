with open('index.html', 'r') as f:
    html = f.read()

# 1. Hide invert + sound buttons when entering the page (Act 3)
# Find enterPage function and add hiding those buttons
html = html.replace(
    "document.body.classList.add('reading');",
    "document.body.classList.add('reading');\n          document.getElementById('invert').style.display = 'none';\n          document.getElementById('sound').style.display = 'none';"
)

# 2. Fix the carousel beat line breaks
html = html.replace(
    "That\xe2\x80\x99s how he was able to help\\nCEOs and founders\\nreach",
    "That\xe2\x80\x99s how he was able to help\\nCEOs and founders reach\\n"
)

# 3. Add a subtle "skip to portfolio" link during the carousel
# Add it near the hint element
html = html.replace(
    '<div id="hint">tap to continue</div>',
    '<div id="hint">tap to continue</div>\n  <div id="skip" style="position:fixed; bottom: max(3.2rem, calc(env(safe-area-inset-bottom) + 2rem)); left:50%; transform:translateX(-50%); z-index:15; opacity:0.35; font-size:0.7rem; letter-spacing:0.12em; text-transform:uppercase; color:var(--muted); cursor:pointer; transition: opacity 0.3s ease;" onmouseenter="this.style.opacity=0.6" onmouseleave="this.style.opacity=0.35">skip to portfolio</div>'
)

# Make skip button trigger enterPage and hide itself
html = html.replace(
    "var mode = 'carousel';",
    "var mode = 'carousel';\n      var skipBtn = null;\n      setTimeout(function() { skipBtn = document.getElementById('skip'); if(skipBtn) skipBtn.addEventListener('click', function(e) { e.stopPropagation(); i = beats.length - 1; render(i); setTimeout(enterPage, 400); }); }, 100);"
)

# Hide skip button when entering page
html = html.replace(
    "document.getElementById('sound').style.display = 'none';",
    "document.getElementById('sound').style.display = 'none';\n          var sk = document.getElementById('skip'); if(sk) sk.style.display = 'none';"
)

with open('index.html', 'w') as f:
    f.write(html)
print('Done')
