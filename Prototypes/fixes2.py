with open('act3-designed.html', 'r') as f:
    html = f.read()

# 1. Hero gap — reduce min-height on mobile
html = html.replace(
    'class="min-h-screen flex flex-col justify-center px-6',
    'class="min-h-[70vh] md:min-h-screen flex flex-col justify-end pb-12 md:pb-0 md:justify-center px-6'
)

# 2. Copy changes — journalism "thing" and writing "them"
html = html.replace(
    'the lead is the most important thing.',
    'the lead is everything.'
)
html = html.replace(
    "it's what makes them stay and pay",
    "it's what makes readers stay and pay"
)

# 3. Annotations on new lines — add block display
html = html.replace(
    'italic opacity-70">About you, not them. Zero specificity.',
    'italic opacity-70 block">About you, not them.<br>Zero specificity.'
)
html = html.replace(
    'italic opacity-70">About THEM. Specificity creates curiosity.',
    'italic opacity-70 block">About THEM.<br>Specificity creates curiosity.'
)

# 4. Terracotta — flip emphasis: punchline should be big, setup should be smaller
html = html.replace(
    '<p class="font-display font-bold type-display text-warm-25 text-balance leading-tight mb-6">\n          The right words don\'t just sound good.\n        </p>\n        <p class="font-body type-subhead text-warm-100/80 text-balance leading-relaxed">\n          They change what people do.\n        </p>',
    '<p class="font-body type-subhead text-warm-100/80 text-balance leading-relaxed mb-4">\n          The right words don\'t just sound good.\n        </p>\n        <p class="font-display font-bold type-display text-warm-25 text-balance leading-tight">\n          They change what people do.\n        </p>'
)

# 4b. Stats — on mobile, make them full width so no empty space on right
# The stats are in a grid col-1 lg:col-2, and within a flex-col — need to make stats bigger on mobile
html = html.replace(
    '<div class="flex flex-col gap-8 lg:gap-10">',
    '<div class="flex flex-col gap-6 lg:gap-10 w-full">'
)

with open('act3-designed.html', 'w') as f:
    f.write(html)
print('All fixes applied')
