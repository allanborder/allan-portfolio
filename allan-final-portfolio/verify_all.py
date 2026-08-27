import urllib.request

with urllib.request.urlopen('http://localhost:8099/index.html') as response:
    html = response.read().decode('utf-8')

checks = [
    ('Centering nav style', 'left:50%;transform:translateX(-50%);' in html),
    ('Pre-final year student', 'Pre-final year student (CSE AI/ML)' in html),
    ('3-part meta layout', 'hero-meta-row' in html and 'Coimbatore, India' in html and 'Karunya University' in html),
    ('Hero skill pills', 'AI / Machine Learning' in html and 'Computer Vision' in html and 'APIs / Backend' in html),
    ('Projects count 5', '5 selected works' in html and 'data-project="nexora"' in html),
    ('Nexora project in grid', 'Nexora AI System' in html),
    ('System flow in smartpark', 'Pricing Engine' in html and 'SQLite DB' in html and 'Express REST API' in html),
    ('Impact section 6+ projects', 'data-to="6"' in html and 'Projects Shipped' in html),
    ('Experience removed from Home', '<section id="experience" class="page-section">' not in html),
    ('Experience preserved in About', 'id="exp-timeline"' in html),
    ('Scaler Java cert path fixed', 'scaler_java.png' in html),
    ('Mindkraft cert image', 'hack_mind.png' in html),
    ('New photos in gallery', 'new_photo_1.jpg' in html and 'new_photo_5.jpg' in html),
    ('Categorized tech section', 'Languages' in html and 'AI / Machine Learning' in html and 'Web &amp; Backend' in html),
    ('Home return routing from case study', "document.getElementById('view-case')" in html)
]

print('=== PORTFOLIO CODE VALIDATION RESULTS ===')
all_passed = True
for name, passed in checks:
    status = "PASS" if passed else "FAIL"
    print(f'[{status}] {name}')
    if not passed:
        all_passed = False

if all_passed:
    print('\nALL 15 VALIDATION CHECKS PASSED!')
else:
    print('\nSome validation checks failed.')
