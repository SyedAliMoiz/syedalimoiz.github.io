with open('index.html', 'r') as f:
    html = f.read()

# 1. "wearing" → "and wearing"
html = html.replace(
    "One day, running downhill,\\nwearing a pair of oversized sunglasses",
    "One day, running downhill,\\nand wearing a pair of oversized sunglasses"
)

# 2. Doctor beat — new text
html = html.replace(
    "Thankfully, the doctors saved him.\\nBut he ran right out of the hospital.\\nStill fearless.",
    "They took him to the doctor...\\nwho gave him a couple stitches and a stern warning.\\nBut he ran right out of the hospital, as carefree as he always was."
)

# 3. Afraid beat — new text
html = html.replace(
    "Now, he was afraid of falling.\\nHe was afraid of people laughing at him.",
    "As he grew up,\\nthe boy began to feel scared of failing, scared of falling."
)

# 4. Remove "to save himself" from hiding beat
html = html.replace(
    "So, to save himself, he started",
    "So, he started"
)

# 5. "grew up and decided to change" → "grew older still and decided..."
# The ⟪⟫ markers create the "emph" style (same as "he fell...")
html = html.replace(
    "Then, one day,\\nthe boy grew up and decided to change.\\n⟪He thought…⟫",
    "Then, one day,\\nthe boy grew older still\\n⟪and decided…⟫"
)

# 6. "That's how" beat — new line breaks
html = html.replace(
    "That’s how\\nhe was able to help\\nCEOs and founders reach\\n⟦9 million people⟧ across 10+ industries.",
    "That’s how he was able to help\\nCEOs and founders\\nreach ⟦9 million people⟧ across 10+ industries."
)

with open('index.html', 'w') as f:
    f.write(html)
print('All carousel beats updated')
