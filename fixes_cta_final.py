with open('index.html', 'r') as f:
    html = f.read()

# Update Card 1: single CTA + cheeky text link
old_card1_ctas = '''          <div class="flex flex-col gap-3">
            <a href="mailto:syedalimoiz@gmail.com?subject=Let%27s%20work%20together"
               class="px-8 py-3.5 bg-terra text-warm-25 font-display font-semibold type-body rounded-full hover:bg-terra-light transition-colors duration-200 text-center">
              Email me
            </a>
            <a href="https://linkedin.com/in/syedalimoiz" target="_blank" rel="noopener"
               class="px-8 py-3.5 border-2 border-warm-500 text-warm-50 font-display font-semibold type-body rounded-full hover:border-warm-300 transition-colors duration-200 text-center">
              LinkedIn
            </a>
          </div>'''

new_card1_ctas = '''          <a href="https://calendly.com/syedalimoiz/meet" target="_blank" rel="noopener"
             class="px-8 py-3.5 bg-terra text-warm-25 font-display font-semibold type-body rounded-full hover:bg-terra-light transition-colors duration-200 text-center mb-3">
            Book a call
          </a>
          <a href="https://docs.google.com/document/d/18RKoyBO-ca6TPP_vjRg73B7-TQQcI6fxhWaEYHUh-mk/edit?usp=sharing"
             target="_blank" rel="noopener"
             class="font-body type-body text-warm-400 hover:text-warm-200 transition-colors duration-200 text-center italic">
            if you're still not convinced, see my work first
          </a>'''

html = html.replace(old_card1_ctas, new_card1_ctas)

# Move Email + LinkedIn to the signature area
html = html.replace(
    '<p class="text-warm-400 type-subhead text-center tracking-wide font-body mt-12">\xe2\x80\x94 Ali</p>',
    '<div class="flex justify-center gap-6 mt-12 mb-3">\n          <a href="mailto:syedalimoiz@gmail.com" class="font-body type-body text-warm-500 hover:text-warm-300 transition-colors duration-200">Email</a>\n          <a href="https://linkedin.com/in/syedalimoiz" target="_blank" rel="noopener" class="font-body type-body text-warm-500 hover:text-warm-300 transition-colors duration-200">LinkedIn</a>\n        </div>\n        <p class="text-warm-400 type-subhead text-center tracking-wide font-body">\xe2\x80\x94 Ali</p>'
)

with open('index.html', 'w') as f:
    f.write(html)
print('Done')
