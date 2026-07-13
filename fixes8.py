with open('index.html', 'r') as f:
    html = f.read()

# 1. "the boy's spirit" → "his spirit" (Image 79)
html = html.replace(
    "the boy\xe2\x80\x99s spirit got",
    "his spirit got"
)

# 2. Afraid beat — new text (Image 80)
html = html.replace(
    "As he grew up,\\nthe boy began to feel scared of failing, scared of falling.",
    "As he grew up,\\nthe boy felt scared of failing,\\nhe felt scared of falling."
)

# 3. Split doctor beat — move "But he ran..." to its own beat (Image 82)
html = html.replace(
    "They took him to the doctor...\\nwho gave him a couple stitches\\nand a stern warning.\\nBut he ran right out of the hospital, as carefree as ever.",
    "They took him to the doctor...\\nwho gave him a couple stitches\\nand a stern warning."
)
# Add new beat after the doctor beat
html = html.replace(
    "{ t: 'line', x: 'They took him to the doctor...\\nwho gave him a couple stitches\\nand a stern warning.' },",
    "{ t: 'line', x: 'They took him to the doctor...\\nwho gave him a couple stitches\\nand a stern warning.' },\n        { t: 'line', x: 'Then, he ran right out of the hospital,\\nas carefree as ever.' },"
)

# 4. "But as his voice" → "Then, as his voice" (Image 83) — wait, Ali said replace "But" with "Then,"
# The beat starts with "But as his voice got deeper"
html = html.replace(
    "But as his voice got deeper,",
    "Then, as his voice got deeper,"
)

# 5. "older still" → "even older" (Image 81)
html = html.replace("older still", "even older")

# 6. Fix the 9M reach beat — 3 lines not 4
html = html.replace(
    "That\xe2\x80\x99s how he was able to help\\nCEOs and founders reach\\n",
    "That\xe2\x80\x99s how he helped\\nCEOs and Founders reach\\n"
)

# 7. Skip button — move to bottom right
html = html.replace(
    "left:50%; transform:translateX(-50%);",
    "right: max(1.4rem, env(safe-area-inset-right)); left:auto; transform:none;"
)

with open('index.html', 'w') as f:
    f.write(html)
print('All fixes applied')
