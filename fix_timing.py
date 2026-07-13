with open('index.html', 'r') as f:
    html = f.read()

# 1. Devil appears earlier — 0ms instead of 600ms (same time as portrait starts fading)
html = html.replace(
    "setTimeout(function() {\n              dt.style.opacity = '1';\n            }, 600);",
    "setTimeout(function() {\n              dt.style.opacity = '1';\n            }, 100);"
)

# 2. Starts moving sooner — 1200ms instead of 1800ms
html = html.replace(
    "setTimeout(function() {\n              // Get the final devil", 
    "setTimeout(function() {\n              // Get the final devil"
)
html = html.replace("}, 1800);", "}, 1000);", 1)

# 3. Faster transition — 1.2s instead of 1.8s
html = html.replace(
    "transition: all 1.8s cubic-bezier(0.4, 0, 0.2, 1);",
    "transition: all 1.2s cubic-bezier(0.25, 0.1, 0.25, 1);"
)

# 4. Final swap happens sooner — 2400ms instead of 3800ms
html = html.replace("}, 3800);", "}, 2400);")

with open('index.html', 'w') as f:
    f.write(html)
print('Timing fixed')
