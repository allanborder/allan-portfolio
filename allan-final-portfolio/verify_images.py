import urllib.request

with urllib.request.urlopen('http://localhost:8099/index.html') as r:
    html = r.read().decode('utf-8')

checks = [
    ('RJ uses rj_hud.jpg', 'rj_hud.jpg' in html),
    ('SmartPark uses smartpark_cover.png', 'smartpark_cover.png' in html),
    ('NeuroAI uses neuroai_dash.jpg', 'neuroai_dash.jpg' in html),
    ('BodyBlueprint uses bodybp_dash.jpg', 'bodybp_dash.jpg' in html),
    ('DermaSense uses aiml-ten_llm_dash.png', 'aiml-ten_llm_dash.png' in html),
    ('Patchwise uses patchwise_dash.jpg', 'patchwise_dash.jpg' in html),
    ('PROJECTS dict RJ coverImage', "coverImage:'rj_hud.jpg'" in html),
    ('PROJECTS dict NeuroAI coverImage', "coverImage:'neuroai_dash.jpg'" in html),
    ('PROJECTS dict BodyBP coverImage', "coverImage:'bodybp_dash.jpg'" in html),
    ('PROJECTS dict Patchwise coverImage', "coverImage:'patchwise_dash.jpg'" in html),
]

print('=== PROJECT IMAGE VALIDATION ===')
all_ok = True
for name, passed in checks:
    status = 'PASS' if passed else 'FAIL'
    print(f'[{status}] {name}')
    if not passed:
        all_ok = False

if all_ok:
    print('\nAll 6 project images verified!')
else:
    print('\nSome images need fixing.')
