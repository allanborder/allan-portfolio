with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update HTML featured project visual image sources
old_p1_img = '<img class="feat-proj-img" src="ai_desk.png" alt="RJ Personal AI Assistant"'
new_p1_img = '<img class="feat-proj-img" src="rj_hud.jpg" alt="RJ Personal AI Assistant"'

old_p3_img = '<img class="feat-proj-img" src="neuroai_cover.png" alt="NeuroAI Medical Imaging System"'
new_p3_img = '<img class="feat-proj-img" src="neuroai_dash.jpg" alt="NeuroAI Medical Imaging System"'

old_p4_img = '<img class="feat-proj-img" src="bodybp_cover.png" alt="BodyBlueprint Pro Fitness App"'
new_p4_img = '<img class="feat-proj-img" src="bodybp_dash.jpg" alt="BodyBlueprint Pro Fitness App"'

old_p6_img = '<img class="feat-proj-img" src="new_photo_2.jpg" alt="Nexora Hackathon Project"'
new_p6_img = '<img class="feat-proj-img" src="patchwise_dash.jpg" alt="Patchwise AI System"'

assert old_p1_img in content, 'old_p1_img not found'
assert old_p3_img in content, 'old_p3_img not found'
assert old_p4_img in content, 'old_p4_img not found'
assert old_p6_img in content, 'old_p6_img not found'

content = content.replace(old_p1_img, new_p1_img, 1)
content = content.replace(old_p3_img, new_p3_img, 1)
content = content.replace(old_p4_img, new_p4_img, 1)
content = content.replace(old_p6_img, new_p6_img, 1)

# 2. Update coverImage in PROJECTS dictionary
old_dict_p1 = "coverImage:'ai_desk.png'"
new_dict_p1 = "coverImage:'rj_hud.jpg'"

old_dict_p3 = "coverImage:'neuroai_cover.png'"
new_dict_p3 = "coverImage:'neuroai_dash.jpg'"

old_dict_p4 = "coverImage:'bodybp_cover.png'"
new_dict_p4 = "coverImage:'bodybp_dash.jpg'"

old_dict_p6 = "coverImage:'new_photo_2.jpg'"
new_dict_p6 = "coverImage:'patchwise_dash.jpg'"

assert old_dict_p1 in content, 'old_dict_p1 not found'
assert old_dict_p3 in content, 'old_dict_p3 not found'
assert old_dict_p4 in content, 'old_dict_p4 not found'
assert old_dict_p6 in content, 'old_dict_p6 not found'

content = content.replace(old_dict_p1, new_dict_p1, 1)
content = content.replace(old_dict_p3, new_dict_p3, 1)
content = content.replace(old_dict_p4, new_dict_p4, 1)
content = content.replace(old_dict_p6, new_dict_p6, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully applied high-tech dark UI dashboard visuals across ALL 6 projects!')
