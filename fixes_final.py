with open('index.html', 'r') as f:
    html = f.read()

# 1. Navbar — remove Method, add Audit linking to pagelifts.com
html = html.replace(
    '<a href="#method" class="font-display text-warm-300 hover:text-warm-50 transition-colors duration-200 text-sm font-semibold tracking-wide">Method</a>\n      <a href="#work"',
    '<a href="#work"'
)
html = html.replace(
    '<a href="#contact" class="font-display text-warm-300 hover:text-warm-50 transition-colors duration-200 text-sm font-semibold tracking-wide">Contact</a>',
    '<a href="#contact" class="font-display text-warm-300 hover:text-warm-50 transition-colors duration-200 text-sm font-semibold tracking-wide">Contact</a>\n      <a href="https://pagelifts.com" target="_blank" rel="noopener" class="font-display text-terra-light hover:text-warm-50 transition-colors duration-200 text-sm font-semibold tracking-wide">Audit</a>'
)

# 2. CTA section — split into two groups: Action CTAs + Contact CTAs
old_buttons = '''        <div class="flex flex-col md:flex-row flex-wrap justify-center gap-4 mb-0">
        <a href="https://docs.google.com/document/d/18RKoyBO-ca6TPP_vjRg73B7-TQQcI6fxhWaEYHUh-mk/edit?usp=sharing"
           target="_blank" rel="noopener"
           class="px-10 py-4 bg-terra text-warm-25 font-display font-semibold type-body rounded-full hover:bg-terra-light transition-colors duration-200 inline-block w-full md:w-auto text-center">
          See my work
        </a>
        <div class="flex gap-4 w-full md:w-auto">
        <a href="mailto:syedalimoiz@gmail.com?subject=Something%20to%20say"
           class="px-10 py-4 border-2 border-warm-500 text-warm-50 font-display font-semibold type-body rounded-full hover:border-warm-300 transition-colors duration-200 inline-block flex-1 md:flex-none text-center">
          Email
        </a>
        <a href="https://linkedin.com/in/syedalimoiz" target="_blank" rel="noopener"
           class="px-10 py-4 border-2 border-warm-500 text-warm-50 font-display font-semibold type-body rounded-full hover:border-warm-300 transition-colors duration-200 inline-block flex-1 md:flex-none text-center">
          LinkedIn
        </a>
        </div>'''

new_buttons = '''        <!-- Action CTAs -->
        <div class="flex flex-col md:flex-row justify-center gap-4 mb-6">
          <a href="https://docs.google.com/document/d/18RKoyBO-ca6TPP_vjRg73B7-TQQcI6fxhWaEYHUh-mk/edit?usp=sharing"
             target="_blank" rel="noopener"
             class="px-10 py-4 bg-terra text-warm-25 font-display font-semibold type-body rounded-full hover:bg-terra-light transition-colors duration-200 inline-block text-center">
            See my work
          </a>
          <a href="https://pagelifts.com" target="_blank" rel="noopener"
             class="px-10 py-4 bg-terra text-warm-25 font-display font-semibold type-body rounded-full hover:bg-terra-light transition-colors duration-200 inline-block text-center">
            Audit your page
          </a>
        </div>
        <!-- Contact CTAs -->
        <div class="flex justify-center gap-4 mb-0">
          <a href="mailto:syedalimoiz@gmail.com?subject=Something%20to%20say"
             class="px-10 py-4 border-2 border-warm-500 text-warm-50 font-display font-semibold type-body rounded-full hover:border-warm-300 transition-colors duration-200 inline-block text-center">
            Email
          </a>
          <a href="https://linkedin.com/in/syedalimoiz" target="_blank" rel="noopener"
             class="px-10 py-4 border-2 border-warm-500 text-warm-50 font-display font-semibold type-body rounded-full hover:border-warm-300 transition-colors duration-200 inline-block text-center">
            LinkedIn
          </a>
        </div>'''

html = html.replace(old_buttons, new_buttons)

with open('index.html', 'w') as f:
    f.write(html)
print('Done')
