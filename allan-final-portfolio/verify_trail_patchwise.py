import urllib.request

with urllib.request.urlopen('http://localhost:8099/index.html') as response:
    html = response.read().decode('utf-8')

checks = [
    ('Patchwise in featured heading', 'Patchwise' in html and '<h3 class="feat-proj-title">Patchwise</h3>' in html),
    ('Patchwise in PROJECTS dictionary', "title:'Patchwise'" in html),
    ('Patchwise in Terminal', 'Patchwise' in html and 'Nexora Hackathon Finalist Prototype' in html),
    ('Trail dimension IMG_W=110', 'IMG_W=110' in html),
    ('Trail dimension IMG_H=138', 'IMG_H=138' in html),
    ('Snappy cursor lerp 0.26', 'cx+=(mx-cx)*.26' in html),
    ('Event delegation for hover states', 'target.closest' in html),
]

print('=== PATCHWISE & TRAIL VALIDATION ===')
all_passed = True
for name, passed in checks:
    status = 'PASS' if passed else 'FAIL'
    print(f'[{status}] {name}')
    if not passed:
        all_passed = False

if all_passed:
    print('\nALL CHECKS PASSED SUCCESSFULLY!')
