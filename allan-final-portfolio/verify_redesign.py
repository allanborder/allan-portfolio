import urllib.request

with urllib.request.urlopen('http://localhost:8099/index.html') as response:
    html = response.read().decode('utf-8')

checks = [
    ('SmartPark image src', 'src="smartpark_cover.png"' in html),
    ('Editorial list class', 'featured-projects-list' in html),
    ('Alternating rows', 'row-reverse' in html),
    ('RJ Project present', 'RJ — Personal AI Assistant' in html and 'data-project="rj"' in html),
    ('RJ Status badge', 'Core System Built' in html),
    ('SmartPark Project present', 'data-project="smartpark"' in html),
    ('NeuroAI Project present', 'data-project="neuroai"' in html),
    ('BodyBlueprint Pro present', 'data-project="bodybp"' in html),
    ('DermaSense Project present', 'DermaSense' in html and 'data-project="dermasense"' in html),
    ('DermaSense status', 'In Development' in html),
    ('Nexora Project present', 'Nexora AI System' in html and 'data-project="nexora"' in html),
    ('Glanceable System Flow in HTML', 'System Flow' in html and 'Wake Word / Voice' in html),
    ('What I personally engineered blocks', 'What I Personally Engineered' in html),
    ('Case Study builder data for RJ', 'rj:{' in html and "coverImage:'ai_desk.png'" in html),
    ('Case Study builder data for DermaSense', 'dermasense:{' in html),
    ('Case study next chain connects RJ', "nextKey:'smartpark'" in html),
]

print('=== EDITORIAL REDESIGN VALIDATION ===')
all_passed = True
for name, passed in checks:
    status = 'PASS' if passed else 'FAIL'
    print(f'[{status}] {name}')
    if not passed:
        all_passed = False

if all_passed:
    print('\nALL REDESIGN VERIFICATION CHECKS PASSED!')
