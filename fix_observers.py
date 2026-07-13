with open('index.html', 'r') as f:
    html = f.read()

# Replace the old .psec observer with new .reveal-section + photo observers
old_observer = """      page.classList.add('js'); // enables the gentle scroll-reveal pre-state
      var io = null;
      if ('IntersectionObserver' in window) {
        io = new IntersectionObserver(function (entries) {
          entries.forEach(function (en) {
            if (en.isIntersecting) { en.target.classList.add('seen'); io.unobserve(en.target); }
          });
        }, { threshold: 0.12 });
        [].forEach.call(page.querySelectorAll('.psec'), function (s) { io.observe(s); });
      } else {
        [].forEach.call(page.querySelectorAll('.psec'), function (s) { s.classList.add('seen'); });
      }"""

new_observer = """      // Scroll-reveal for new Act 3 sections
      var io = null;
      var pio = null;
      if ('IntersectionObserver' in window) {
        io = new IntersectionObserver(function (entries) {
          entries.forEach(function (en) {
            if (en.isIntersecting) { en.target.classList.add('seen'); io.unobserve(en.target); }
          });
        }, { threshold: 0.15 });
        pio = new IntersectionObserver(function (entries) {
          entries.forEach(function (en) {
            if (en.isIntersecting) { en.target.classList.add('photo-seen'); pio.unobserve(en.target); }
          });
        }, { threshold: 0.3 });
      }
      function setupObservers() {
        if (io) {
          [].forEach.call(page.querySelectorAll('.reveal-section'), function (s) { io.observe(s); });
        } else {
          [].forEach.call(page.querySelectorAll('.reveal-section'), function (s) { s.classList.add('seen'); });
        }
        if (pio) {
          [].forEach.call(page.querySelectorAll('#pair1, #pair2'), function (s) { pio.observe(s); });
        } else {
          [].forEach.call(page.querySelectorAll('#pair1, #pair2'), function (s) { s.classList.add('photo-seen'); });
        }
      }"""

html = html.replace(old_observer, new_observer)

# Call setupObservers() inside enterPage after the page is shown
html = html.replace(
    "page.classList.add('shown');",
    "page.classList.add('shown');\n          setupObservers();"
)

# Remove the duplicate standalone observer script at the bottom (from prototype)
# Find and remove the prototype's observer script
import re
proto_script = re.search(r'<script>\s*\(function \(\) \{\s*if \(!.*?IntersectionObserver.*?photo-seen.*?\}\)\(\);\s*</script>', html, re.DOTALL)
if proto_script:
    html = html.replace(proto_script.group(0), '')
    print('Removed duplicate prototype observer script')

with open('index.html', 'w') as f:
    f.write(html)
print('Observer fix applied')
