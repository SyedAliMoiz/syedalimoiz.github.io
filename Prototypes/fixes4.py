with open('act3-designed.html', 'r') as f:
    html = f.read()

# 1. Fix "change" — terracotta italic on terracotta bg is invisible. Use gold or warm-25 bold instead
html = html.replace(
    'They <span class="text-terra italic">change</span> what people do.',
    'They <span class="text-gold font-extrabold underline decoration-2 underline-offset-4">change</span> what people do.'
)

# 2. Remove labels from ghostwritten reach numbers
html = html.replace(
    '''          <span class="font-body type-body text-warm-500 block mt-1">top single post</span>''',
    ''
)
html = html.replace(
    '''          <span class="font-body type-body text-warm-500 block mt-1">second highest</span>''',
    ''
)
html = html.replace(
    '''          <span class="font-body type-body text-warm-500 block mt-1">third highest</span>''',
    ''
)
html = html.replace(
    '''          <span class="font-body type-body text-warm-500 block mt-1">fourth highest</span>''',
    ''
)

with open('act3-designed.html', 'w') as f:
    f.write(html)
print('Done')
