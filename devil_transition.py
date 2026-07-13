with open('index.html', 'r') as f:
    html = f.read()

# 1. Add the transition devil element (fixed position, hidden initially)
# It uses the same devil image from the h1
# Place it right before <div id="page">

# First, get the devil image src from the existing h1
import re
devil_src_match = re.search(r'<img src="(data:image/png;base64,[^"]+)" alt="" class="absolute pointer-events-none hidden md:block"', html)
if not devil_src_match:
    print("Devil image not found!")
    exit()
devil_src = devil_src_match.group(1)
print(f"Found devil src ({len(devil_src)} chars)")

# Add the transition element
transition_el = f'''
  <!-- Devil kid transition element — starts where portrait was, slides to final position -->
  <img id="devil-transit" src="{devil_src}" alt=""
       style="position:fixed; z-index:100; pointer-events:none; opacity:0;
              top:50%; left:50%; transform:translate(-50%, calc(-50% - 6.5rem)) rotate(0deg);
              width: clamp(180px, 22vw, 280px);
              transition: all 1.8s cubic-bezier(0.4, 0, 0.2, 1);
              -webkit-mask-image: linear-gradient(to bottom, black 50%, transparent 95%);
              mask-image: linear-gradient(to bottom, black 50%, transparent 95%);">
'''

html = html.replace('  <div id="page"', transition_el + '\n  <div id="page"')

# 2. Hide the real devil kid in the h1 initially (it will be shown after transition)
html = html.replace(
    'class="absolute pointer-events-none hidden md:block"',
    'class="absolute pointer-events-none hidden md:block" id="devil-final"'
)

# 3. Modify enterPage() to trigger the animation
# After the portrait starts fading, show the devil kid at center, then animate it to final position

old_enter = '''          document.body.classList.add('reading');
          document.getElementById('invert').style.display = 'none';
          document.getElementById('sound').style.display = 'none';
          var sk = document.getElementById('skip'); if(sk) sk.style.display = 'none';'''

new_enter = '''          document.body.classList.add('reading');
          document.getElementById('invert').style.display = 'none';
          document.getElementById('sound').style.display = 'none';
          var sk = document.getElementById('skip'); if(sk) sk.style.display = 'none';

          // Devil kid transition: appear at center (where portrait was), then slide to final spot
          var dt = document.getElementById('devil-transit');
          var df = document.getElementById('devil-final');
          if (dt && df) {
            // Hide the final devil kid during transition
            df.style.opacity = '0';
            // Show the transition devil at center after portrait starts fading
            setTimeout(function() {
              dt.style.opacity = '1';
            }, 600);
            // After a beat, animate to final position
            setTimeout(function() {
              // Get the final devil's position on screen
              var rect = df.getBoundingClientRect();
              var finalTop = rect.top + rect.height / 2;
              var finalLeft = rect.left + rect.width / 2;
              dt.style.top = finalTop + 'px';
              dt.style.left = finalLeft + 'px';
              dt.style.transform = 'translate(-50%, -50%) rotate(22deg) scale(0.35)';
            }, 1800);
            // After animation completes, show real devil and hide transition one
            setTimeout(function() {
              df.style.opacity = '1';
              dt.style.display = 'none';
            }, 3800);
          }'''

html = html.replace(old_enter, new_enter)

with open('index.html', 'w') as f:
    f.write(html)
print('Devil transition animation added')
