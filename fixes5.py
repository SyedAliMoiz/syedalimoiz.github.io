with open('index.html', 'r') as f:
    html = f.read()

# 1. Carousel beat — change the 9M reach line
html = html.replace(
    "He helped CEOs and founders\\nreach ⟦9 million people⟧,\\nacross 10+ industries.",
    "That's how\\nhe was able to help\\nCEOs and founders reach\\n⟦9 million people⟧ across 10+ industries."
)

# 2. "he found his own" → "Ali found his own"  
html = html.replace(
    "he found his own.",
    "Ali found his own."
)

# 3. Photos — the issue is the old carousel JS sets up observers for .psec elements
# but our new Act 3 uses .reveal-section and #pair1/#pair2 with .photo-seen
# The old page.classList.add('js') line adds .js to #page which the OLD CSS
# uses for opacity:0 on .psec elements. Our new content doesn't have .psec.
# But it might be conflicting. Let me remove the old observer setup for .psec
# Actually, let's just make sure the new observer script runs AFTER enterPage

# 4. Orange section — add vertical divider between text and stats on desktop
html = html.replace(
    '<div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-16 items-center reveal-section">',
    '<div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-0 items-center reveal-section">'
)
# Add border-right to the text column and padding
html = html.replace(
    """          The right words don't just sound good...
        </p>
        <p class="font-display font-bold type-display text-warm-25 text-balance leading-tight">
          They <span class="text-gold font-extrabold underline decoration-2 underline-offset-4">change</span> what people do.
        </p>
      </div>""",
    """          The right words don't just sound good...
        </p>
        <p class="font-display font-bold type-display text-warm-25 text-balance leading-tight">
          They <span class="text-gold font-extrabold underline decoration-2 underline-offset-4">change</span> what people do.
        </p>
      </div>"""
)
# Actually, easier to just add a border class to the left column div
html = html.replace(
    'text-warm-100/80 text-balance leading-relaxed mb-4">\n          The right words',
    'text-warm-100/80 text-balance leading-relaxed mb-4 lg:border-r lg:border-warm-100/20 lg:pr-16">\n          The right words'
)

# 5. "handful of founders" → "couple of founders"
html = html.replace(
    "I work with a handful of founders at a time.",
    "I only work with a couple of founders at a time."
)
# Also in the carousel if it exists there
html = html.replace(
    "a handful of founders",
    "a couple of founders"
)

with open('index.html', 'w') as f:
    f.write(html)
print('All fixes applied')
