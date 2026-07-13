with open('index.html', 'r') as f:
    html = f.read()

# Replace the CTA panel with two-option cards
old_cta = '''      <!-- THE CTA: visually separated panel -->
      <div class="bg-warm-800 rounded-2xl p-10 md:p-14 text-center">
        <p class="font-display font-bold type-cta text-warm-50 mb-10 md:mb-12 whitespace-nowrap">
          Let\'s get to work.
        </p>

        <!-- Action CTAs -->
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
        </div>
      </div>'''

new_cta = '''      <!-- Two paths -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8">

        <!-- Path 1: Hire me -->
        <div class="bg-warm-800 rounded-2xl p-8 md:p-10 flex flex-col">
          <p class="font-display font-bold type-headline text-warm-50 mb-4">Work with me</p>
          <p class="font-body type-body-lg text-warm-300 mb-8 flex-1">
            You need someone who finds the right words for your brand. I study your audience, define your voice, and build the copy from scratch.
          </p>
          <div class="flex flex-col gap-3">
            <a href="mailto:syedalimoiz@gmail.com?subject=Let%27s%20work%20together"
               class="px-8 py-3.5 bg-terra text-warm-25 font-display font-semibold type-body rounded-full hover:bg-terra-light transition-colors duration-200 text-center">
              Email me
            </a>
            <a href="https://linkedin.com/in/syedalimoiz" target="_blank" rel="noopener"
               class="px-8 py-3.5 border-2 border-warm-500 text-warm-50 font-display font-semibold type-body rounded-full hover:border-warm-300 transition-colors duration-200 text-center">
              LinkedIn
            </a>
          </div>
        </div>

        <!-- Path 2: Audit -->
        <div class="bg-warm-800 rounded-2xl p-8 md:p-10 flex flex-col">
          <p class="font-display font-bold type-headline text-warm-50 mb-4">Audit your page</p>
          <p class="font-body type-body-lg text-warm-300 mb-8 flex-1">
            You already have a landing page but it\'s not converting. I\'ll find what\'s broken, identify the lead it\'s missing, and tell you exactly what to fix.
          </p>
          <a href="https://pagelifts.com" target="_blank" rel="noopener"
             class="px-8 py-3.5 bg-terra text-warm-25 font-display font-semibold type-body rounded-full hover:bg-terra-light transition-colors duration-200 text-center">
            Book an audit
          </a>
        </div>

      </div>'''

html = html.replace(old_cta, new_cta)

with open('index.html', 'w') as f:
    f.write(html)
print('Done')
