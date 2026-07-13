with open('act3-designed.html', 'r') as f:
    html = f.read()

# 1. Fix hero — remove the broken justify-end, go back to justify-center with less min-height
html = html.replace(
    'class="min-h-[70vh] md:min-h-screen flex flex-col justify-end pb-12 md:pb-0 md:justify-center px-6',
    'class="min-h-[75vh] md:min-h-screen flex flex-col justify-center px-6'
)
# Remove the negative margin on photo section
html = html.replace(
    '<section class="px-4 md:px-8 pb-4 -mt-20 md:-mt-0">',
    '<section class="px-4 md:px-8 pb-4">'
)

# 2. Finding the Lead heading — smaller on mobile so it fits one line
html = html.replace(
    "font-size: clamp(3.5rem, 8vw, 7rem); line-height: 1.05; letter-spacing: -0.03em;\">Finding the Lead</p>",
    "font-size: clamp(2.4rem, 8vw, 7rem); line-height: 1.05; letter-spacing: -0.03em;\">Finding the Lead</p>"
)

# 3. Finding the Lead body lines — slightly smaller on mobile
html = html.replace(
    "font-size: clamp(1.6rem, 3.2vw, 2.8rem); line-height: 1.2;",
    "font-size: clamp(1.3rem, 3.2vw, 2.8rem); line-height: 1.2;",
)
html = html.replace(
    "font-size: clamp(1.8rem, 3.8vw, 3.2rem); line-height: 1.2;",
    "font-size: clamp(1.4rem, 3.8vw, 3.2rem); line-height: 1.2;",
)

# 4. "sound good." → "sound good..."
html = html.replace(
    "just sound good.",
    "just sound good..."
)

# 5. Make "change" pop in "They change what people do."
html = html.replace(
    "They change what people do.",
    'They <span class="text-terra italic">change</span> what people do.'
)

# 6. Stats labels
html = html.replace("landing page conversion", "cold audience conversion")
html = html.replace("client revenue from copy", "client revenue")

# 7. Stats layout — horizontal with dash: 40% — cold audience conversion
html = html.replace(
    '''        <div>
          <span class="font-display font-extrabold type-stat text-warm-25 block">40%</span>
          <span class="text-warm-100/80 type-body-lg block mt-2">cold audience conversion</span>
        </div>
        <div>
          <span class="font-display font-extrabold type-stat text-warm-25 block">$215K+</span>
          <span class="text-warm-100/80 type-body-lg block mt-2">client revenue</span>
        </div>''',
    '''        <div class="flex items-baseline gap-4">
          <span class="font-display font-extrabold type-stat text-warm-25">40%</span>
          <span class="text-warm-100/80 type-body-lg">— cold audience conversion</span>
        </div>
        <div class="flex items-baseline gap-4">
          <span class="font-display font-extrabold type-stat text-warm-25">$215K+</span>
          <span class="text-warm-100/80 type-body-lg">— client revenue</span>
        </div>'''
)

# 8. Dean's List — remove standalone line, add to IBA Karachi
html = html.replace(
    """          <div class="flex flex-wrap gap-x-6 gap-y-2">
            <span class="font-body type-body text-warm-300"><span class="text-gold font-display font-semibold">3.57</span> GPA</span>
            <span class="font-body type-body text-warm-300">Thesis: <span class="text-gold font-display font-semibold">93/100</span></span>
            <span class="font-body type-body text-warm-300">Part of the Dean's List</span>
          </div>""",
    """          <div class="flex flex-wrap gap-x-6 gap-y-2">
            <span class="font-body type-body text-warm-300"><span class="text-gold font-display font-semibold">3.57</span> GPA</span>
            <span class="font-body type-body text-warm-300">Thesis: <span class="text-gold font-display font-semibold">93/100</span></span>
          </div>"""
)
html = html.replace(
    '>IBA Karachi</p>',
    '>IBA Karachi <span class="text-warm-400 font-normal">(Dean\'s List)</span></p>'
)

# 9. CTA text
html = html.replace(
    "If you've got something to say and you think nobody can hear you, I can help.",
    "If you're a founder who wants their brand to get noticed, I can help!"
)

with open('act3-designed.html', 'w') as f:
    f.write(html)
print('All fixes applied')
