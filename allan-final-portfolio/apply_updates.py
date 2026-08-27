import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Navigation Styling to center nav-links
old_nav_css = '''.nav-inner{max-width:1400px;margin:0 auto;height:100%;padding:0 48px;display:flex;align-items:center;justify-content:space-between;}
    .nav-logo{font-family:var(--sans);font-size:1.35rem;font-weight:900;color:var(--text);text-decoration:none;letter-spacing:-2px;}
    .nav-links{display:flex;gap:32px;list-style:none;}'''

new_nav_css = '''.nav-inner{max-width:1400px;margin:0 auto;height:100%;padding:0 48px;display:flex;align-items:center;justify-content:space-between;position:relative;}
    .nav-logo{font-family:var(--sans);font-size:1.35rem;font-weight:900;color:var(--text);text-decoration:none;letter-spacing:-2px;z-index:2;}
    .nav-links{display:flex;gap:32px;list-style:none;position:absolute;left:50%;transform:translateX(-50%);}'''

assert old_nav_css in content, 'old_nav_css not found'
content = content.replace(old_nav_css, new_nav_css, 1)

# 2. Update Hero Meta Row & Pills
old_hero_meta = '''      <div class="hero-pills" id="heroPills">
        <span class="hero-pill">React</span>
        <span class="hero-pill">Python</span>
        <span class="hero-pill">Node.js</span>
        <span class="hero-pill">TensorFlow</span>
        <span class="hero-pill">FastAPI</span>
      </div>
      <div class="hero-meta-row" id="heroMeta">
        <span class="hero-meta-item">📍 Coimbatore, India</span>
        <span class="hero-meta-dot"></span>
        <span class="hero-meta-item">Sophomore AIML · Karunya University</span>
      </div>'''

new_hero_meta = '''      <div class="hero-pills" id="heroPills">
        <span class="hero-pill">AI / Machine Learning</span>
        <span class="hero-pill">Python</span>
        <span class="hero-pill">Java</span>
        <span class="hero-pill">Web Development</span>
        <span class="hero-pill">Computer Vision</span>
        <span class="hero-pill">APIs / Backend</span>
        <span class="hero-pill">Cloud &amp; DevOps</span>
        <span class="hero-pill">Git / GitHub</span>
      </div>
      <div class="hero-meta-row" id="heroMeta">
        <span class="hero-meta-item"><i class="fas fa-location-dot" style="font-size:.75rem;margin-right:4px;color:var(--text-sec);"></i> Coimbatore, India</span>
        <span class="hero-meta-dot"></span>
        <span class="hero-meta-item"><i class="fas fa-graduation-cap" style="font-size:.8rem;margin-right:4px;color:var(--text-sec);"></i> Pre-final year student (CSE AI/ML)</span>
        <span class="hero-meta-dot"></span>
        <span class="hero-meta-item"><i class="fas fa-university" style="font-size:.75rem;margin-right:4px;color:var(--text-sec);"></i> Karunya University</span>
      </div>'''

assert old_hero_meta in content, 'old_hero_meta not found'
content = content.replace(old_hero_meta, new_hero_meta, 1)

# 3. Mobile menu experience link cleanup
old_mob_menu = '''<div class="mobile-menu" id="mobileMenu">
  <a href="javascript:void(0)" onclick="closeMob()">Home</a>
  <a href="javascript:void(0)" onclick="closeMob();document.getElementById('nav-works').click();return false;">Projects</a>
  <a href="javascript:void(0)" onclick="closeMob();showAbout();">About</a>
  <a href="javascript:void(0)" onclick="closeMob();if(currentView!=='main'){document.getElementById('nav-home').click();setTimeout(function(){var el=document.getElementById('experience');if(el)el.scrollIntoView({behavior:'smooth',block:'start'});},600);}else{var el=document.getElementById('experience');if(el)el.scrollIntoView({behavior:'smooth',block:'start'});}return false;">Experience</a>
  <a href="javascript:void(0)" onclick="closeMob();showContact();">Contact</a>
  <a href="Allan_Resume_2026.pdf" target="_blank">Resume ↗</a>
</div>'''

new_mob_menu = '''<div class="mobile-menu" id="mobileMenu">
  <a href="javascript:void(0)" onclick="closeMob();document.getElementById('nav-home').click();return false;">Home</a>
  <a href="javascript:void(0)" onclick="closeMob();document.getElementById('nav-works').click();return false;">Projects</a>
  <a href="javascript:void(0)" onclick="closeMob();showAbout();">About</a>
  <a href="javascript:void(0)" onclick="closeMob();showAbout();setTimeout(function(){var el=document.getElementById('exp-timeline');if(el)el.scrollIntoView({behavior:'smooth',block:'start'});},450);return false;">Experience</a>
  <a href="javascript:void(0)" onclick="closeMob();showContact();">Contact</a>
  <a href="Allan_Resume_2026.pdf" target="_blank">Resume ↗</a>
</div>'''

assert old_mob_menu in content, 'old_mob_menu not found'
content = content.replace(old_mob_menu, new_mob_menu, 1)

# 4. Remove experience section from Home page & streamline impact section
old_home_lower = '''    <section id="impact" class="page-section">
      <div class="section-eyebrow">By the Numbers</div>
      <h2 class="section-title"><span class="tl"><span class="tli">My Impact</span></span></h2>
      <div class="impact-grid">
        <div class="impact-stat">
          <div class="impact-num"><span class="cnt" data-to="3" data-suf="+">0</span></div>
          <div><div class="impact-label">Years Learning</div><p class="impact-desc">Full-stack systems, AI models, and real-world software — relentlessly since 2023.</p></div>
        </div>
        <div class="impact-stat">
          <div class="impact-num"><span class="cnt" data-to="15" data-suf="+">0</span></div>
          <div><div class="impact-label">Projects Built</div><p class="impact-desc">End-to-end systems spanning medical AI, parking, fitness, and beyond.</p></div>
        </div>
        <div class="ach-grid">
          <!-- CARD 1: AI/ML Developer — uses ai_desk.png (uploaded: 1780856504992_aiml-ten_llm_dash.png) -->
          <div class="ach-card photo-card">
            <div class="ach-photo-wrap">
              <img src="ai_desk.png" alt="AI/ML Developer" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
              <div class="ach-photo-fallback" style="display:none;"><div class="ach-photo-fallback-em">🤖</div><div class="ach-photo-fallback-label">AI / ML Dev</div></div>
              <div class="ach-photo-badge">🤖 AI / ML Dev</div>
            </div>
          </div>
          <!-- CARD 2: Open For Work — uses open_dash.png (uploaded: 1780856382850_open_dash.png) -->
          <div class="ach-card photo-card">
            <div class="ach-photo-wrap">
              <img src="open_dash.png" alt="Open For Work" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
              <div class="ach-photo-fallback" style="display:none;"><div class="ach-photo-fallback-em">💼</div><div class="ach-photo-fallback-label">Open For Work</div></div>
              <div class="ach-photo-badge">💼 Open For Work</div>
            </div>
          </div>
          <div class="ach-card"><div class="ach-em">🤖</div><div class="ach-t">AI/ML Developer</div><div class="ach-s">TensorFlow · EfficientNetB0 · LLMs</div></div>
          <div class="ach-card"><div class="ach-em">💼</div><div class="ach-t">Open For Work</div><div class="ach-s">Internships · Full-time · Freelance</div></div>
        </div>
        <div class="impact-cta">
          <div class="impact-cta-heading">Let's Build Something Worth Shipping.</div>
          <a href="javascript:void(0)" class="impact-cta-link" id="impactContactBtn">Start a Conversation →</a>
        </div>
        <div class="impact-stat-r">
          <div class="impact-stat">
            <div class="impact-num"><span class="cnt" data-to="10" data-suf="+">0</span></div>
            <div><div class="impact-label">Technologies Used</div><p class="impact-desc">Python, React, TensorFlow, FastAPI, Node.js, Firebase, MongoDB, and more.</p></div>
          </div>
          <div class="impact-stat">
            <div class="impact-num"><span class="cnt" data-to="5" data-suf="+">0</span></div>
            <div><div class="impact-label">Hackathons & Competitions</div><p class="impact-desc">Mindkraft 2025 (Winner × 2) · Mindkraft 2026 Runners-Up (National).</p></div>
          </div>
        </div>
      </div>
    </section>

    <div class="section-flow-rule"></div>

    <section id="experience" class="page-section">
      <div class="section-eyebrow">Work History</div>
      <h2 class="section-title"><span class="tl"><span class="tli">Experience</span></span></h2>
      <table class="exp-table">
        <tr>
          <td class="exp-year">Jun – Aug 2025</td>
          <td>
            <div class="exp-co-cell">
              <img class="exp-logo" src="image_f2e263.png" alt="Fuzionest" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
              <div class="exp-logo-ph" style="display:none;">F</div>
              <div><div class="exp-co">Fuzionest</div><div class="exp-role">Software Developer Intern</div></div>
            </div>
          </td>
          <td class="exp-detail">Maintained analytical paradigms and programming outputs inside team pipelines. Delivered data processing modules under active industrial deadlines.
            <div class="exp-chips"><span class="exp-chip">Data Engineering</span><span class="exp-chip">Python</span><span class="exp-chip">System Analytics</span></div>
            <a href="URK24CS7129-ALLANPAULRAJV.pdf" target="_blank" class="exp-link"><i class="fas fa-file-pdf"></i> Certificate</a>
          </td>
        </tr>
        <tr>
          <td class="exp-year">Oct 2025 – Present</td>
          <td>
            <div class="exp-co-cell">
              <img class="exp-logo" src="image_f2da29.png" alt="GDG Karunya" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
              <div class="exp-logo-ph" style="display:none;">G</div>
              <div><div class="exp-co">GDG Karunya</div><div class="exp-role">Media &amp; Content Production Lead</div></div>
            </div>
          </td>
          <td class="exp-detail">Core leadership governing visual asset architectures, cross-platform media production, and brand layouts across community-wide developer interactions.
            <div class="exp-chips"><span class="exp-chip">Asset Strategy</span><span class="exp-chip">Media Systems</span><span class="exp-chip">Google Developer Groups</span></div>
          </td>
        </tr>
        <tr>
          <td class="exp-year">Jun – Aug 2026</td>
          <td>
            <div class="exp-co-cell">
              <img class="exp-logo" src="lysa_logo.png" alt="Lysa Solutions" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
              <div class="exp-logo-ph" style="display:none;">L</div>
              <div><div class="exp-co">Lysa Solutions</div><div class="exp-role">Full Stack Developer Intern</div></div>
            </div>
          </td>
          <td class="exp-detail">Engineered backend logic, deployed responsive components, maintained collaborative on-site codebases during a 3-month offline deployment in Coimbatore.
            <div class="exp-chips"><span class="exp-chip">Full-Stack</span><span class="exp-chip">Offline Frameworks</span><span class="exp-chip">3 Months · On-Site</span></div>
            <a href="Allan_Paulraj_offer_letter.pdf" target="_blank" class="exp-link"><i class="fas fa-file-pdf"></i> Offer Letter</a>
          </td>
        </tr>
        <tr>
          <td class="exp-year">Jun 2026</td>
          <td>
            <div class="exp-co-cell">
              <img class="exp-logo" src="oasis_logo.png" alt="Oasis Infobyte" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
              <div class="exp-logo-ph" style="display:none;">O</div>
              <div><div class="exp-co">Oasis Infobyte</div><div class="exp-role">Data Science Intern</div></div>
            </div>
          </td>
          <td class="exp-detail">Fellowship-based data science internship focused on hands-on application of data analysis and machine learning concepts in an industrial setting.
            <div class="exp-chips"><span class="exp-chip">Data Science</span><span class="exp-chip">Machine Learning</span><span class="exp-chip">Python</span></div>
            <a href="oasis_offer_letter.pdf" target="_blank" class="exp-link"><i class="fas fa-file-pdf"></i> Offer Letter</a>
          </td>
        </tr>
      </table>
    </section>'''

new_home_lower = '''    <section id="impact" class="page-section">
      <div class="section-eyebrow">By the Numbers</div>
      <h2 class="section-title"><span class="tl"><span class="tli">My Impact</span></span></h2>
      <div class="impact-grid">
        <div class="impact-stat">
          <div class="impact-num"><span class="cnt" data-to="3" data-suf="+">0</span></div>
          <div><div class="impact-label">Years of Development</div><p class="impact-desc">Full-stack architectures, AI models, and real-world software — engineered rigorously since 2023.</p></div>
        </div>
        <div class="impact-stat">
          <div class="impact-num"><span class="cnt" data-to="6" data-suf="+">0</span></div>
          <div><div class="impact-label">Projects Shipped</div><p class="impact-desc">End-to-end applications spanning medical computer vision, real-time systems, and visual analytics.</p></div>
        </div>
        <div class="ach-grid">
          <div class="ach-card">
            <div class="ach-em">⚡</div>
            <div class="ach-t">Technical Focus</div>
            <div class="ach-s">High-performance AI pipelines, clean backend microservices &amp; responsive modern interfaces.</div>
          </div>
          <div class="ach-card">
            <div class="ach-em">🎯</div>
            <div class="ach-t">Core Philosophy</div>
            <div class="ach-s">Building robust, production-grade tools that solve concrete real-world workflows without bloat.</div>
          </div>
        </div>
        <div class="impact-cta">
          <div class="impact-cta-heading">Let's Build Something Worth Shipping.</div>
          <a href="javascript:void(0)" class="impact-cta-link" id="impactContactBtn">Start a Conversation →</a>
        </div>
        <div class="impact-stat-r">
          <div class="impact-stat">
            <div class="impact-num"><span class="cnt" data-to="10" data-suf="+">0</span></div>
            <div><div class="impact-label">Core Technologies</div><p class="impact-desc">Python, React, TensorFlow, FastAPI, Node.js, SQLite, and modern deployment tools.</p></div>
          </div>
          <div class="impact-stat">
            <div class="impact-num"><span class="cnt" data-to="2" data-suf="+">0</span></div>
            <div><div class="impact-label">Hackathons &amp; Events</div><p class="impact-desc">Mindkraft 2026 National Runners-Up (Switch &amp; Glitch IoT) · Nexora Hackathon.</p></div>
          </div>
        </div>
      </div>
    </section>'''

assert old_home_lower in content, 'old_home_lower not found'
content = content.replace(old_home_lower, new_home_lower, 1)

# 5. Fix Navigation return to Home from Project Detail
old_nav_home = '''/* ─── Navbar event listeners ─── */
document.getElementById('nav-home').addEventListener('click',function(e){
  e.preventDefault();
  if(currentView!=='main'){showMain(currentView);}
  else{window.scrollTo({top:0,behavior:'smooth'});}
});'''

new_nav_home = '''/* ─── Navbar event listeners ─── */
document.getElementById('nav-home').addEventListener('click',function(e){
  e.preventDefault();
  var caseView = document.getElementById('view-case');
  if(caseView && caseView.style.display !== 'none' && caseView.style.display !== '') {
    document.getElementById('page-home-sections').style.display = '';
    document.getElementById('page-lower-sections').style.display = '';
    document.getElementById('view-case').style.display = 'none';
    document.getElementById('view-listing').style.display = 'block';
  }
  if(currentView!=='main'){showMain(currentView);}
  else{window.scrollTo({top:0,behavior:'smooth'});}
});'''

assert old_nav_home in content, 'old_nav_home not found'
content = content.replace(old_nav_home, new_nav_home, 1)

# 6. Fix logoBtn return to Home as well
old_logo_btn = '''document.getElementById('logoBtn').addEventListener('click',function(e){e.preventDefault();if(currentView!=='main')showMain(currentView);else window.scrollTo({top:0,behavior:'smooth'});});'''

new_logo_btn = '''document.getElementById('logoBtn').addEventListener('click',function(e){
  e.preventDefault();
  var caseView = document.getElementById('view-case');
  if(caseView && caseView.style.display !== 'none' && caseView.style.display !== '') {
    document.getElementById('page-home-sections').style.display = '';
    document.getElementById('page-lower-sections').style.display = '';
    document.getElementById('view-case').style.display = 'none';
    document.getElementById('view-listing').style.display = 'block';
  }
  if(currentView!=='main')showMain(currentView);
  else window.scrollTo({top:0,behavior:'smooth'});
});'''

assert old_logo_btn in content, 'old_logo_btn not found'
content = content.replace(old_logo_btn, new_logo_btn, 1)

# 7. Update certData: fix scaler_java.png, keep hack_mind.png, and add Saylor / HP / Nexora certificates
old_cert_data = '''var certData=[
  {file:'image_f347de.png',ph:'📊',issuer:'HP LIFE Foundation',name:'Data Science and Analytics',date:'Jun 2025'},
  {file:'image_f3475f.png',ph:'🤖',issuer:'Saylor University',name:'CS205: Building with AI',date:'Jun 2025'},
  {file:'image_f34723.png',ph:'🔐',issuer:'Saylor University',name:'CS260: Cryptography & Network Sec',date:'Jun 2025'},
  {file:'image_f343fd.png',ph:'🧠',issuer:'IBM',name:'AI Fundamentals',date:'Oct 2025'},
  {file:'image_f343a2.png',ph:'☕',issuer:'Scaler',name:'Java – Mastering the Fundamentals',date:'Oct 2025'},
  {file:'Screenshot 2025-06-27 160331.png',ph:'🗄️',issuer:'MongoDB',name:'Building AI Agents with MongoDB',date:'Oct 2025'},
  {file:'Screenshot 2025-06-27 160352.png',ph:'🗃️',issuer:'Scaler',name:'DBMS – Fundamentals & Concepts',date:'Apr 2026'},
  {file:'image_f34b20.png',ph:'✨',issuer:'Simplilearn',name:'Introduction to Generative AI',date:'Apr 2026'},
  {file:'hack_mind.png',ph:'🏆',issuer:'Mindkraft 2026 · National',name:'Runners-Up — Switch & Glitch IoT',date:'2026'},
];'''

new_cert_data = '''var certData=[
  {file:'hack_mind.png',ph:'🏆',issuer:'Mindkraft 2026 · National',name:'Runners-Up — Switch & Glitch IoT',date:'2026'},
  {file:'scaler_java.png',ph:'☕',issuer:'Scaler',name:'Java – Mastering the Fundamentals',date:'Oct 2025'},
  {file:'Screenshot 2025-06-27 160352.png',ph:'🗃️',issuer:'Scaler',name:'DBMS – Fundamentals & Concepts',date:'Apr 2026'},
  {file:'image_f347de.png',ph:'📊',issuer:'HP LIFE Foundation',name:'Data Science and Analytics',date:'Jun 2025'},
  {file:'image_f3475f.png',ph:'🤖',issuer:'Saylor University',name:'CS205: Building with AI',date:'Jun 2025'},
  {file:'image_f34723.png',ph:'🔐',issuer:'Saylor University',name:'CS260: Cryptography & Network Sec',date:'Jun 2025'},
  {file:'image_f343fd.png',ph:'🧠',issuer:'IBM',name:'AI Fundamentals',date:'Oct 2025'},
  {file:'Screenshot 2025-06-27 160331.png',ph:'🗄️',issuer:'MongoDB',name:'Building AI Agents with MongoDB',date:'Oct 2025'},
  {file:'image_f34b20.png',ph:'✨',issuer:'Simplilearn',name:'Introduction to Generative AI',date:'Apr 2026'},
];'''

assert old_cert_data in content, 'old_cert_data not found'
content = content.replace(old_cert_data, new_cert_data, 1)

# 8. Update achievements table on About page to be accurate
old_ach_table = '''        <tbody>
          <tr class="ach-row"><td class="ach-num">01</td><td><div class="ach-name">First Place · TUF Brothers</div><div class="ach-org">Mindkraft 2025 Winner</div></td><td><span class="ach-category-badge">Winner</span></td><td class="ach-year">2025</td></tr>
          <tr class="ach-row"><td class="ach-num">02</td><td><div class="ach-name">First Place · Shooting Stars</div><div class="ach-org">Mindkraft 2025 Winner</div></td><td><span class="ach-category-badge">Winner</span></td><td class="ach-year">2025</td></tr>
          <tr class="ach-row"><td class="ach-num">03</td><td><div class="ach-name">Second Place · Switch &amp; Glitch</div><div class="ach-org">Mindkraft 2026 · National Level ECE · Team: Allan Paulraj V &amp; Tivin Elvis PJ</div></td><td><span class="ach-category-badge">Competition</span></td><td class="ach-year">2026</td></tr>
          <tr class="ach-row"><td class="ach-num">04</td><td><div class="ach-name">Software Developer Intern</div><div class="ach-org">Fuzionest — Data Engineering &amp; Analytics</div></td><td><span class="ach-category-badge">Internship</span></td><td class="ach-year">2025</td></tr>
          <tr class="ach-row"><td class="ach-num">05</td><td><div class="ach-name">Full Stack Developer Intern</div><div class="ach-org">Lysa Solutions · On-Site · Coimbatore</div></td><td><span class="ach-category-badge">Internship</span></td><td class="ach-year">2026</td></tr>
          <tr class="ach-row"><td class="ach-num">06</td><td><div class="ach-name">Data Science Intern</div><div class="ach-org">Oasis Infobyte · Fellowship · 1 Month</div></td><td><span class="ach-category-badge">Internship</span></td><td class="ach-year">2026</td></tr>
          <tr class="ach-row"><td class="ach-num">07</td><td><div class="ach-name">Media &amp; Content Production Lead</div><div class="ach-org">Google Developer Group On Campus · Karunya</div></td><td><span class="ach-category-badge">Leadership</span></td><td class="ach-year">2025–Now</td></tr>
        </tbody>'''

new_ach_table = '''        <tbody>
          <tr class="ach-row"><td class="ach-num">01</td><td><div class="ach-name">National Runners-Up · Switch &amp; Glitch IoT</div><div class="ach-org">Mindkraft 2026 · National Level Technical Fest · Team: Allan Paulraj V &amp; Tivin Elvis PJ</div></td><td><span class="ach-category-badge">Hackathon</span></td><td class="ach-year">2026</td></tr>
          <tr class="ach-row"><td class="ach-num">02</td><td><div class="ach-name">Nexora Hackathon Finalist &amp; Project Builder</div><div class="ach-org">Nexora Hackathon · Rapid Prototyping &amp; Real-Time Systems</div></td><td><span class="ach-category-badge">Hackathon</span></td><td class="ach-year">2025</td></tr>
          <tr class="ach-row"><td class="ach-num">03</td><td><div class="ach-name">Mastering the Fundamentals of Java</div><div class="ach-org">Scaler Academy Certification</div></td><td><span class="ach-category-badge">Certification</span></td><td class="ach-year">2025</td></tr>
          <tr class="ach-row"><td class="ach-num">04</td><td><div class="ach-name">Software Developer Intern</div><div class="ach-org">Fuzionest — Data Engineering &amp; Analytics</div></td><td><span class="ach-category-badge">Internship</span></td><td class="ach-year">2025</td></tr>
          <tr class="ach-row"><td class="ach-num">05</td><td><div class="ach-name">Full Stack Developer Intern</div><div class="ach-org">Lysa Solutions · On-Site · Coimbatore</div></td><td><span class="ach-category-badge">Internship</span></td><td class="ach-year">2026</td></tr>
          <tr class="ach-row"><td class="ach-num">06</td><td><div class="ach-name">Data Science Intern</div><div class="ach-org">Oasis Infobyte · Fellowship · 1 Month</div></td><td><span class="ach-category-badge">Internship</span></td><td class="ach-year">2026</td></tr>
          <tr class="ach-row"><td class="ach-num">07</td><td><div class="ach-name">Media &amp; Content Production Lead</div><div class="ach-org">Google Developer Group On Campus · Karunya</div></td><td><span class="ach-category-badge">Leadership</span></td><td class="ach-year">2025–Now</td></tr>
        </tbody>'''

assert old_ach_table in content, 'old_ach_table not found'
content = content.replace(old_ach_table, new_ach_table, 1)

# 9. Update Photo Gallery with all photos including uploaded photos
old_img_cards = '''var IMG_CARDS=[{src:'photo_1.jpg',caption:'Allan'},{src:'photo_2.jpg',caption:'Allan'},{src:'photo_3.jpg',caption:'Allan'},{src:'photo_4.jpg',caption:'Allan'},{src:'photo_5.jpg',caption:'Allan'},{src:'photo_6.jpg',caption:'Allan'},{src:'photo_7.jpg',caption:'Allan'},{src:'photo_8.jpg',caption:'Allan'},{src:'photo_9.jpg',caption:'Allan'},{src:'photo_10.jpg',caption:'Allan'}];'''

new_img_cards = '''var IMG_CARDS=[
  {src:'new_photo_5.jpg',caption:'Allan Paulraj'},
  {src:'new_photo_2.jpg',caption:'Focused Building'},
  {src:'new_photo_3.jpg',caption:'Problem Solving'},
  {src:'new_photo_4.jpg',caption:'Training & Discipline'},
  {src:'new_photo_1.jpg',caption:'Fitness Journey'},
  {src:'photo_1.jpg',caption:'Allan'},
  {src:'photo_2.jpg',caption:'Moments'},
  {src:'photo_3.jpg',caption:'Campus Life'},
  {src:'photo_4.jpg',caption:'Explorer'},
  {src:'photo_5.jpg',caption:'Karunya'},
  {src:'photo_6.jpg',caption:'Allan'},
  {src:'photo_7.jpg',caption:'Story'},
  {src:'photo_8.jpg',caption:'Visuals'},
  {src:'photo_9.jpg',caption:'Perspective'},
  {src:'photo_10.jpg',caption:'Gallery'}
];'''

assert old_img_cards in content, 'old_img_cards not found'
content = content.replace(old_img_cards, new_img_cards, 1)

# 10. Update Tech Used Section on About page with clean organized categories
old_about_brands = '''  <section id="about-brands">
    <!-- tech_used.png (uploaded: 1780856766680_tech_used.png) displayed above pill marquee -->
    <div class="brands-eyebrow" id="brandsEyebrow">Technologies · Tools · Platforms</div>
    <div style="text-align:center;margin-bottom:48px;">
      <img src="tech_used.png" alt="Technologies Used" style="max-width:900px;width:100%;border-radius:20px;border:1px solid var(--border);" loading="lazy"/>
    </div>
    <div class="tech-marquee-wrap" id="techMarqueeWrap">
      <div class="tech-marquee-track" id="techMarqueeTrack"></div>
    </div>
  </section>'''

new_about_brands = '''  <section id="about-brands">
    <div class="brands-eyebrow" id="brandsEyebrow">Technologies · Tools · Ecosystem</div>
    <div style="max-width:1100px;margin:0 auto 48px;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px;padding:0 24px;">
      <div style="background:var(--white);border:1px solid var(--border);border-radius:16px;padding:28px 24px;">
        <div style="font-family:var(--mono);font-size:.64rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--text-muted);margin-bottom:12px;"><i class="fas fa-code" style="margin-right:6px;"></i> Languages</div>
        <div style="display:flex;flex-wrap:wrap;gap:8px;">
          <span class="pc-tag">Python</span>
          <span class="pc-tag">Java</span>
          <span class="pc-tag">JavaScript (ES6+)</span>
          <span class="pc-tag">C</span>
          <span class="pc-tag">SQL</span>
        </div>
      </div>
      <div style="background:var(--white);border:1px solid var(--border);border-radius:16px;padding:28px 24px;">
        <div style="font-family:var(--mono);font-size:.64rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--text-muted);margin-bottom:12px;"><i class="fas fa-brain" style="margin-right:6px;"></i> AI / Machine Learning</div>
        <div style="display:flex;flex-wrap:wrap;gap:8px;">
          <span class="pc-tag">TensorFlow</span>
          <span class="pc-tag">EfficientNetB0</span>
          <span class="pc-tag">Computer Vision</span>
          <span class="pc-tag">Ollama / Mistral</span>
          <span class="pc-tag">NumPy &amp; OpenCV</span>
        </div>
      </div>
      <div style="background:var(--white);border:1px solid var(--border);border-radius:16px;padding:28px 24px;">
        <div style="font-family:var(--mono);font-size:.64rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--text-muted);margin-bottom:12px;"><i class="fas fa-layer-group" style="margin-right:6px;"></i> Web &amp; Backend</div>
        <div style="display:flex;flex-wrap:wrap;gap:8px;">
          <span class="pc-tag">React</span>
          <span class="pc-tag">FastAPI</span>
          <span class="pc-tag">Node.js</span>
          <span class="pc-tag">Express.js</span>
          <span class="pc-tag">REST APIs</span>
          <span class="pc-tag">Chart.js</span>
        </div>
      </div>
      <div style="background:var(--white);border:1px solid var(--border);border-radius:16px;padding:28px 24px;">
        <div style="font-family:var(--mono);font-size:.64rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:var(--text-muted);margin-bottom:12px;"><i class="fas fa-screwdriver-wrench" style="margin-right:6px;"></i> Tools &amp; Data</div>
        <div style="display:flex;flex-wrap:wrap;gap:8px;">
          <span class="pc-tag">Git / GitHub</span>
          <span class="pc-tag">Docker</span>
          <span class="pc-tag">SQLite</span>
          <span class="pc-tag">MongoDB</span>
          <span class="pc-tag">Firebase</span>
          <span class="pc-tag">Vercel CDN</span>
        </div>
      </div>
    </div>
    <div class="tech-marquee-wrap" id="techMarqueeWrap">
      <div class="tech-marquee-track" id="techMarqueeTrack"></div>
    </div>
  </section>'''

assert old_about_brands in content, 'old_about_brands not found'
content = content.replace(old_about_brands, new_about_brands, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html with Phase 1 & 2 fixes successfully!')
