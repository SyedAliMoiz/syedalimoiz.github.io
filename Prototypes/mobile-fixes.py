import re

with open('act3-designed.html', 'r') as f:
    html = f.read()

# 1. Hide devil image on mobile, hide "Ali Moiz" on mobile
html = html.replace(
    'class="absolute pointer-events-none"',
    'class="absolute pointer-events-none hidden md:block"'
)
html = html.replace(
    '<span class="font-display font-bold text-warm-50 text-lg tracking-tight">Ali Moiz</span>',
    '<span class="font-display font-bold text-warm-50 text-lg tracking-tight hidden md:inline">Ali Moiz</span>'
)

# 2. Hero text too big on mobile — reduce mobile min in clamp
html = html.replace(
    'font-size: clamp(2.8rem, 7.5vw, 7rem)',
    'font-size: clamp(2.2rem, 7.5vw, 7rem)'
)

# 3. Reduce gap between hero section and photo section
html = html.replace(
    '<section class="px-4 md:px-8 pb-4">',
    '<section class="px-4 md:px-8 pb-4 -mt-20 md:-mt-0">'
)

# 4. Finding the Lead — remove whitespace-nowrap on mobile (allow wrapping)
# Replace whitespace-nowrap with md:whitespace-nowrap so it only applies on desktop
html = html.replace(
    'font-display font-semibold text-warm-300 whitespace-nowrap"',
    'font-display font-semibold text-warm-300 md:whitespace-nowrap"'
)
html = html.replace(
    'font-display font-semibold text-warm-200 whitespace-nowrap"',
    'font-display font-semibold text-warm-200 md:whitespace-nowrap"'
)

# 5. Before/After cards — make BEFORE/AFTER labels bigger and bolder, annotations italic
# BEFORE label
html = html.replace(
    'font-display font-semibold text-warm-400 type-body tracking-wide block mb-4">BEFORE',
    'font-display font-bold text-warm-400 type-body-lg tracking-widest uppercase block mb-4">BEFORE'
)
# AFTER label  
html = html.replace(
    'font-display font-semibold text-terra-light type-body tracking-wide block mb-4">AFTER',
    'font-display font-bold text-terra-light type-body-lg tracking-widest uppercase block mb-4">AFTER'
)
# Annotations — make italic and smaller
html = html.replace(
    'font-display text-warm-400 type-body mt-5">About you, not them. Zero specificity.',
    'font-display text-warm-400 type-body mt-5 italic opacity-70">About you, not them. Zero specificity.'
)
html = html.replace(
    'font-display text-warm-400 type-body mt-5">About THEM. Specificity creates curiosity.',
    'font-display text-warm-400 type-body mt-5 italic opacity-70">About THEM. Specificity creates curiosity.'
)

# 6. Mariah — shorten name and designation on mobile
html = html.replace(
    '<span class="font-display font-semibold text-terra type-body-lg">Mariah Chew</span>',
    '<span class="font-display font-semibold text-terra type-body-lg"><span class="md:hidden">Mariah</span><span class="hidden md:inline">Mariah Chew</span></span>'
)
html = html.replace(
    '<span class="font-display font-semibold text-terra type-body-lg">— Therapist, Bay Area</span>',
    '<span class="font-display font-semibold text-terra type-body-lg"><span class="md:hidden">— Therapist</span><span class="hidden md:inline">— Therapist, Bay Area</span></span>'
)

# 7. Terracotta stats — bigger caption text on mobile
html = html.replace(
    'text-warm-100/80 type-body block mt-2">landing page conversion',
    'text-warm-100/80 type-body-lg block mt-2">landing page conversion'
)
html = html.replace(
    'text-warm-100/80 type-body block mt-2">client revenue from copy',
    'text-warm-100/80 type-body-lg block mt-2">client revenue from copy'
)

# 8. Dean's List — change "5 semesters" to "Part of the Dean's List" (both mobile and desktop)
html = html.replace(
    """Dean's List, <span class="text-gold font-display font-semibold">5</span> semesters""",
    """Part of the Dean's List"""
)

# 9. CTA buttons — restructure for mobile: See my work full width, Email+LinkedIn side by side
old_buttons = '''        <div class="flex flex-wrap justify-center gap-4 mb-0">'''
new_buttons = '''        <div class="flex flex-col md:flex-row flex-wrap justify-center gap-4 mb-0">'''
html = html.replace(old_buttons, new_buttons)

# Make See my work full width on mobile
html = html.replace(
    'class="px-10 py-4 bg-terra text-warm-25 font-display font-semibold type-body rounded-full hover:bg-terra-light transition-colors duration-200 inline-block">',
    'class="px-10 py-4 bg-terra text-warm-25 font-display font-semibold type-body rounded-full hover:bg-terra-light transition-colors duration-200 inline-block w-full md:w-auto text-center">'
)

# Wrap Email + LinkedIn in a flex row for mobile
html = html.replace(
    '''        <a href="mailto:syedalimoiz@gmail.com?subject=Something%20to%20say"
           class="px-10 py-4 border-2 border-warm-500 text-warm-50 font-display font-semibold type-body rounded-full hover:border-warm-300 transition-colors duration-200 inline-block">
          Email
        </a>
        <a href="https://linkedin.com/in/syedalimoiz" target="_blank" rel="noopener"
           class="px-10 py-4 border-2 border-warm-500 text-warm-50 font-display font-semibold type-body rounded-full hover:border-warm-300 transition-colors duration-200 inline-block">
          LinkedIn
        </a>''',
    '''        <div class="flex gap-4 w-full md:w-auto">
        <a href="mailto:syedalimoiz@gmail.com?subject=Something%20to%20say"
           class="px-10 py-4 border-2 border-warm-500 text-warm-50 font-display font-semibold type-body rounded-full hover:border-warm-300 transition-colors duration-200 inline-block flex-1 md:flex-none text-center">
          Email
        </a>
        <a href="https://linkedin.com/in/syedalimoiz" target="_blank" rel="noopener"
           class="px-10 py-4 border-2 border-warm-500 text-warm-50 font-display font-semibold type-body rounded-full hover:border-warm-300 transition-colors duration-200 inline-block flex-1 md:flex-none text-center">
          LinkedIn
        </a>
        </div>'''
)

# Make "Let's get to work" not wrap on mobile
html = html.replace(
    'font-display font-bold type-cta text-warm-50 mb-10 md:mb-12 text-balance',
    'font-display font-bold type-cta text-warm-50 mb-10 md:mb-12 whitespace-nowrap'
)

with open('act3-designed.html', 'w') as f:
    f.write(html)

print('All mobile fixes applied')
