with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS for Projects / Editorial Showcase
old_proj_css = '''.works-header{max-width:1300px;margin:0 auto;padding:0 60px 56px;display:flex;align-items:flex-end;justify-content:space-between;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:24px;}
    .works-count{font-family:var(--serif);font-size:.85rem;font-style:italic;color:var(--text-muted);margin-top:8px;}
    .projects-grid{max-width:1300px;margin:0 auto;padding:48px 60px 0;display:grid;grid-template-columns:1fr 1fr;gap:24px;}
    .proj-card{background:var(--white);border-radius:20px;border:1px solid var(--border);overflow:hidden;cursor:none;transition:box-shadow .4s cubic-bezier(.16,1,.3,1),transform .4s cubic-bezier(.16,1,.3,1);opacity:0;transform:translateY(40px);}
    .proj-card.pc-visible{opacity:1;transform:translateY(0);}
    .proj-card:hover{box-shadow:0 20px 56px rgba(0,0,0,.11);transform:translateY(-5px);}
    .proj-card:last-child:nth-child(odd){grid-column:1/span 2;}
    .pc-thumb{position:relative;width:100%;height:260px;overflow:hidden;}
    .pc-thumb-inner{position:absolute;inset:0;transition:transform .65s cubic-bezier(.16,1,.3,1);}
    .proj-card:hover .pc-thumb-inner{transform:scale(1.05);}
    .pc-thumb-bg{width:100%;height:100%;display:flex;align-items:center;justify-content:center;}
    .pc-thumb-img{width:100%;height:100%;object-fit:cover;display:block;}
    .pc-thumb-overlay{position:absolute;inset:0;background:rgba(0,0,0,0);display:flex;align-items:center;justify-content:center;transition:background .35s;z-index:2;}
    .proj-card:hover .pc-thumb-overlay{background:rgba(0,0,0,.4);}
    .pc-pill{font-size:.72rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#fff;background:rgba(255,255,255,.15);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.3);padding:10px 24px;border-radius:999px;opacity:0;transform:scale(.9);transition:opacity .3s,transform .3s;}
    .proj-card:hover .pc-pill{opacity:1;transform:scale(1);}
    .pc-num-badge{position:absolute;top:16px;left:16px;z-index:3;font-family:var(--serif);font-size:1rem;font-weight:700;color:rgba(255,255,255,.8);background:rgba(0,0,0,.45);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.15);padding:4px 12px;border-radius:999px;}
    .pc-year-badge{position:absolute;top:16px;right:16px;z-index:3;font-size:.68rem;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:rgba(255,255,255,.7);background:rgba(0,0,0,.38);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.15);padding:4px 12px;border-radius:999px;}
    .pc-body{padding:24px 28px 28px;}
    .pc-category{font-size:.7rem;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:var(--text-muted);margin-bottom:8px;}
    .pc-title{font-family:var(--serif);font-size:clamp(22px,2.2vw,30px);font-weight:700;letter-spacing:-.8px;color:var(--text);margin-bottom:10px;line-height:1.1;}
    .pc-desc{font-size:.88rem;color:var(--text-sec);line-height:1.65;margin-bottom:20px;}
    .pc-tags{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:22px;}
    .pc-tag{font-size:.66rem;font-weight:600;letter-spacing:1.5px;text-transform:uppercase;color:var(--text-sec);background:var(--surface);border:1px solid var(--border);padding:5px 12px;border-radius:999px;}
    .pc-footer{display:flex;align-items:center;justify-content:space-between;border-top:1px solid var(--border);padding-top:18px;}
    .pc-cta{display:inline-flex;align-items:center;gap:8px;font-size:.78rem;font-weight:700;color:var(--text);text-decoration:none;transition:gap .25s;cursor:none;}
    .pc-cta:hover{gap:12px;}
    .pc-arrow{width:32px;height:32px;border-radius:50%;border:1px solid var(--border-strong);display:flex;align-items:center;justify-content:center;font-size:.75rem;background:var(--white);transition:background .2s,color .2s,border-color .2s,transform .3s;}
    .pc-cta:hover .pc-arrow{background:var(--dark);color:#fff;border-color:var(--dark);transform:rotate(45deg);}
    .pc-meta-txt{font-size:.72rem;color:var(--text-muted);}'''

new_proj_css = '''.works-header{max-width:1300px;margin:0 auto;padding:0 60px 64px;display:flex;align-items:flex-end;justify-content:space-between;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:24px;}
    .works-count{font-family:var(--serif);font-size:.85rem;font-style:italic;color:var(--text-muted);margin-top:8px;}
    
    .featured-projects-list{max-width:1300px;margin:0 auto;padding:0 60px;}
    .feat-project-row{padding:88px 0;border-bottom:1px solid var(--border);position:relative;display:grid;grid-template-columns:1.05fr 1fr;gap:64px;align-items:center;opacity:0;transform:translateY(40px);transition:transform .8s cubic-bezier(.16,1,.3,1),opacity .8s cubic-bezier(.16,1,.3,1);}
    .feat-project-row.row-reverse{grid-template-columns:1fr 1.05fr;}
    .feat-project-row.pc-visible{opacity:1;transform:translateY(0);}
    .feat-project-row:last-child{border-bottom:none;}
    
    .feat-proj-visual{position:relative;width:100%;height:400px;border-radius:24px;overflow:hidden;background:var(--surface);border:1px solid var(--border);cursor:none;transition:box-shadow .5s cubic-bezier(.16,1,.3,1),transform .5s cubic-bezier(.16,1,.3,1);}
    .feat-proj-visual:hover{box-shadow:0 32px 70px rgba(0,0,0,.13);transform:translateY(-4px);}
    .feat-proj-img{width:100%;height:100%;object-fit:cover;display:block;transition:transform .7s cubic-bezier(.16,1,.3,1);}
    .feat-proj-visual:hover .feat-proj-img{transform:scale(1.04);}
    .feat-proj-fallback{width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;background:linear-gradient(140deg,#121316,#22252a);color:#fff;}
    .feat-proj-fallback-icon{font-size:3.5rem;}
    .feat-proj-fallback-text{font-family:var(--mono);font-size:.72rem;letter-spacing:3px;text-transform:uppercase;color:rgba(255,255,255,.6);}
    .feat-proj-overlay{position:absolute;inset:0;background:rgba(0,0,0,0);display:flex;align-items:center;justify-content:center;transition:background .35s;z-index:2;}
    .feat-proj-visual:hover .feat-proj-overlay{background:rgba(0,0,0,.45);}
    .feat-proj-pill{font-size:.72rem;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#fff;background:rgba(255,255,255,.18);backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.35);padding:11px 26px;border-radius:999px;opacity:0;transform:scale(.9);transition:opacity .3s,transform .3s;}
    .feat-proj-visual:hover .feat-proj-pill{opacity:1;transform:scale(1);}
    .feat-proj-num-badge{position:absolute;top:20px;left:20px;z-index:3;font-family:var(--serif);font-size:1.1rem;font-weight:800;color:rgba(255,255,255,.9);background:rgba(0,0,0,.5);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.2);padding:4px 14px;border-radius:999px;}
    .feat-proj-status-badge{position:absolute;top:20px;right:20px;z-index:3;font-family:var(--mono);font-size:.65rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#fff;background:rgba(0,0,0,.55);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,.2);padding:5px 14px;border-radius:999px;display:flex;align-items:center;gap:6px;}
    
    .feat-proj-info{position:relative;display:flex;flex-direction:column;gap:18px;}
    .feat-proj-kicker{font-family:var(--mono);font-size:.68rem;font-weight:700;letter-spacing:3.5px;text-transform:uppercase;color:var(--text-muted);display:flex;align-items:center;gap:12px;}
    .feat-proj-kicker::before{content:'';display:block;width:24px;height:1px;background:var(--text-muted);}
    .feat-proj-title{font-family:var(--serif);font-size:clamp(32px,3.6vw,48px);font-weight:900;letter-spacing:-1.8px;line-height:.98;color:var(--text);}
    .feat-proj-tagline{font-size:1rem;font-weight:400;color:var(--text-sec);line-height:1.6;}
    
    .feat-proj-block{background:var(--white);border:1px solid var(--border);border-radius:14px;padding:16px 20px;}
    .feat-proj-block-label{font-family:var(--mono);font-size:.6rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--text-muted);margin-bottom:6px;display:flex;align-items:center;gap:6px;}
    .feat-proj-block-text{font-size:.84rem;color:var(--text-sec);line-height:1.6;}
    
    .feat-proj-flow{display:flex;align-items:center;gap:6px;flex-wrap:wrap;font-family:var(--mono);font-size:.68rem;font-weight:600;color:var(--text);margin-top:2px;}
    .feat-flow-step{background:var(--surface);border:1px solid var(--border);padding:4px 10px;border-radius:6px;white-space:nowrap;}
    .feat-flow-arrow{color:var(--text-muted);font-size:.7rem;}
    
    .feat-proj-tags{display:flex;gap:6px;flex-wrap:wrap;}
    .feat-proj-tag{font-family:var(--mono);font-size:.64rem;font-weight:600;letter-spacing:1px;text-transform:uppercase;color:var(--text-sec);background:var(--white);border:1px solid var(--border);padding:5px 12px;border-radius:999px;}
    
    .feat-proj-actions{display:flex;align-items:center;gap:16px;margin-top:6px;}
    .feat-proj-btn{display:inline-flex;align-items:center;gap:10px;background:var(--dark);color:#fff;font-size:.76rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;padding:12px 24px;border-radius:999px;text-decoration:none;transition:background .2s,transform .25s;cursor:none;}
    .feat-proj-btn:hover{background:#2a2a2a;transform:translateY(-2px);}
    .feat-proj-btn-ghost{display:inline-flex;align-items:center;gap:8px;font-size:.76rem;font-weight:700;color:var(--text-sec);text-decoration:none;padding:12px 18px;border-radius:999px;border:1px solid var(--border);transition:all .2s;cursor:none;}
    .feat-proj-btn-ghost:hover{color:var(--text);border-color:var(--dark);background:var(--white);}
    
    @media(max-width:960px){
      .featured-projects-list{padding:0 28px;}
      .feat-project-row,.feat-project-row.row-reverse{grid-template-columns:1fr;gap:36px;padding:64px 0;}
      .feat-proj-visual{height:280px;}
      .feat-project-row.row-reverse .feat-proj-visual{order:1;}
      .feat-project-row.row-reverse .feat-proj-info{order:2;}
    }'''

assert old_proj_css in content, 'old_proj_css not found'
content = content.replace(old_proj_css, new_proj_css, 1)

# 2. Replace HTML in #works: between `<div id="view-listing">` and `<!-- CASE STUDY -->`
idx_start = content.find('<div id="view-listing">')
idx_end = content.find('<!-- CASE STUDY -->')
assert idx_start != -1 and idx_end != -1, 'view-listing boundaries not found'

new_view_listing = '''<div id="view-listing">
      <div class="works-header">
        <div class="works-header-left">
          <div class="section-eyebrow">Featured Work &amp; Active Systems</div>
          <h2 class="section-title"><span class="tl"><span class="tli">Projects</span></span></h2>
          <div class="works-count">06 Featured Case Studies &amp; Real-World Systems</div>
        </div>
        <p style="font-size:.9rem;color:var(--text-muted);max-width:340px;line-height:1.65;">From autonomous voice AI to medical computer vision and distributed systems — built from scratch.</p>
      </div>

      <div class="featured-projects-list">

        <!-- 01 / RJ — PERSONAL AI ASSISTANT -->
        <article class="feat-project-row" data-project="rj">
          <div class="feat-proj-visual open-case" data-project="rj">
            <img class="feat-proj-img" src="ai_desk.png" alt="RJ Personal AI Assistant" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" loading="lazy"/>
            <div class="feat-proj-fallback" style="display:none;">
              <div class="feat-proj-fallback-icon">🎙️</div>
              <div class="feat-proj-fallback-text">RJ Personal AI HUD</div>
            </div>
            <div class="feat-proj-overlay"><div class="feat-proj-pill">Explore Case Study</div></div>
            <div class="feat-proj-num-badge">01</div>
            <div class="feat-proj-status-badge"><span class="green-dot" style="width:6px;height:6px;"></span> Core System Built</div>
          </div>
          <div class="feat-proj-info">
            <div class="feat-proj-kicker">Voice AI · System Automation · Active Dev</div>
            <h3 class="feat-proj-title">RJ — Personal AI Assistant</h3>
            <p class="feat-proj-tagline">RJ is my personal AI assistant built to interact with my system through voice, automate everyday tasks, maintain persistent memory, and provide an always-on intelligent interface.</p>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-microchip"></i> System Flow</div>
              <div class="feat-proj-flow">
                <span class="feat-flow-step">Wake Word / Voice</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Local Speech Engine</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Groq LLM Streaming</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">PC Automation / TTS</span>
              </div>
            </div>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-user-gear"></i> What I Personally Engineered</div>
              <p class="feat-proj-block-text">Built the low-latency wake-word pipeline, WebSocket streaming HUD, TTS audio caching, persistent SQLite context store, and OS automation scripts.</p>
            </div>
            <div class="feat-proj-tags">
              <span class="feat-proj-tag">Python</span>
              <span class="feat-proj-tag">Groq API</span>
              <span class="feat-proj-tag">FastAPI &amp; WebSockets</span>
              <span class="feat-proj-tag">PyAudio / TTS</span>
              <span class="feat-proj-tag">OS Automation</span>
            </div>
            <div class="feat-proj-actions">
              <a href="javascript:void(0)" class="feat-proj-btn open-case" data-project="rj">View Case Study <i class="fas fa-arrow-right"></i></a>
            </div>
          </div>
        </article>

        <!-- 02 / SMARTPARK -->
        <article class="feat-project-row row-reverse" data-project="smartpark">
          <div class="feat-proj-info">
            <div class="feat-proj-kicker">Full-Stack · Real-Time IoT / Web App</div>
            <h3 class="feat-proj-title">SmartPark</h3>
            <p class="feat-proj-tagline">Real-time multi-floor parking management platform with algorithmic dynamic pricing, automated GST billing, and live occupancy synchronization.</p>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-microchip"></i> System Flow</div>
              <div class="feat-proj-flow">
                <span class="feat-flow-step">Attendant UI</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Express REST Router</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Dynamic Tariff Engine</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">SQLite Database</span>
              </div>
            </div>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-user-gear"></i> What I Personally Engineered</div>
              <p class="feat-proj-block-text">Architected the entire MVC backend in Node.js, real-time floor coordination logic, automated GST invoice PDF generation, and Chart.js analytics.</p>
            </div>
            <div class="feat-proj-tags">
              <span class="feat-proj-tag">Node.js</span>
              <span class="feat-proj-tag">Express.js</span>
              <span class="feat-proj-tag">SQLite</span>
              <span class="feat-proj-tag">Chart.js</span>
              <span class="feat-proj-tag">REST API</span>
            </div>
            <div class="feat-proj-actions">
              <a href="javascript:void(0)" class="feat-proj-btn open-case" data-project="smartpark">View Case Study <i class="fas fa-arrow-right"></i></a>
              <a href="https://github.com/allanborder" target="_blank" class="feat-proj-btn-ghost"><i class="fab fa-github"></i> GitHub</a>
            </div>
          </div>
          <div class="feat-proj-visual open-case" data-project="smartpark">
            <img class="feat-proj-img" src="smartpark_cover.png" alt="SmartPark Real-Time Dashboard" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" loading="lazy"/>
            <div class="feat-proj-fallback" style="display:none;">
              <div class="feat-proj-fallback-icon">🅿️</div>
              <div class="feat-proj-fallback-text">SmartPark Dashboard</div>
            </div>
            <div class="feat-proj-overlay"><div class="feat-proj-pill">Explore Case Study</div></div>
            <div class="feat-proj-num-badge">02</div>
            <div class="feat-proj-status-badge"><span class="green-dot" style="width:6px;height:6px;"></span> Completed</div>
          </div>
        </article>

        <!-- 03 / NEUROAI -->
        <article class="feat-project-row" data-project="neuroai">
          <div class="feat-proj-visual open-case" data-project="neuroai">
            <img class="feat-proj-img" src="neuroai_cover.png" alt="NeuroAI Medical Imaging System" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" loading="lazy"/>
            <div class="feat-proj-fallback" style="display:none;">
              <div class="feat-proj-fallback-icon">🧠</div>
              <div class="feat-proj-fallback-text">NeuroAI Medical CV</div>
            </div>
            <div class="feat-proj-overlay"><div class="feat-proj-pill">Explore Case Study</div></div>
            <div class="feat-proj-num-badge">03</div>
            <div class="feat-proj-status-badge"><span class="green-dot" style="width:6px;height:6px;"></span> 97%+ Accuracy</div>
          </div>
          <div class="feat-proj-info">
            <div class="feat-proj-kicker">Computer Vision · Medical AI · Local LLM</div>
            <h3 class="feat-proj-title">NeuroAI</h3>
            <p class="feat-proj-tagline">Brain MRI classification platform diagnosing four tumor categories using EfficientNetB0, paired with an on-device Mistral 7B LLM for clinical report synthesis.</p>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-microchip"></i> System Flow</div>
              <div class="feat-proj-flow">
                <span class="feat-flow-step">MRI Scan Upload</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">FastAPI Async API</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">EfficientNetB0 (CV)</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Mistral 7B (Ollama)</span>
              </div>
            </div>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-user-gear"></i> What I Personally Engineered</div>
              <p class="feat-proj-block-text">Fine-tuned EfficientNetB0 weights, configured image tensor augmentation pipelines, and integrated asynchronous local LLM diagnostic prompt handlers.</p>
            </div>
            <div class="feat-proj-tags">
              <span class="feat-proj-tag">TensorFlow</span>
              <span class="feat-proj-tag">EfficientNetB0</span>
              <span class="feat-proj-tag">FastAPI</span>
              <span class="feat-proj-tag">Ollama &amp; Mistral</span>
              <span class="feat-proj-tag">React</span>
            </div>
            <div class="feat-proj-actions">
              <a href="javascript:void(0)" class="feat-proj-btn open-case" data-project="neuroai">View Case Study <i class="fas fa-arrow-right"></i></a>
              <a href="https://github.com/allanborder" target="_blank" class="feat-proj-btn-ghost"><i class="fab fa-github"></i> GitHub</a>
            </div>
          </div>
        </article>

        <!-- 04 / BODYBLUEPRINT PRO -->
        <article class="feat-project-row row-reverse" data-project="bodybp">
          <div class="feat-proj-info">
            <div class="feat-proj-kicker">React SPA · AI Coaching · Live on Vercel</div>
            <h3 class="feat-proj-title">BodyBlueprint Pro</h3>
            <p class="feat-proj-tagline">Privacy-first fitness progression platform featuring timeline data visualization, automatic personal record detection, and Groq-powered AI workout coaching.</p>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-microchip"></i> System Flow</div>
              <div class="feat-proj-flow">
                <span class="feat-flow-step">Workout Entry</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Recharts Viz Engine</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">PR Calculation Algorithm</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Llama 3.3 Guidance</span>
              </div>
            </div>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-user-gear"></i> What I Personally Engineered</div>
              <p class="feat-proj-block-text">Developed the modular React state layer with 100% client persistence in LocalStorage, chart rendering hooks, and AI advisory endpoints.</p>
            </div>
            <div class="feat-proj-tags">
              <span class="feat-proj-tag">React</span>
              <span class="feat-proj-tag">Vite</span>
              <span class="feat-proj-tag">Recharts</span>
              <span class="feat-proj-tag">Groq API</span>
              <span class="feat-proj-tag">Vercel CDN</span>
            </div>
            <div class="feat-proj-actions">
              <a href="javascript:void(0)" class="feat-proj-btn open-case" data-project="bodybp">View Case Study <i class="fas fa-arrow-right"></i></a>
              <a href="https://body-blueprint-2.vercel.app/" target="_blank" class="feat-proj-btn-ghost"><i class="fas fa-external-link-alt"></i> Live Demo</a>
            </div>
          </div>
          <div class="feat-proj-visual open-case" data-project="bodybp">
            <img class="feat-proj-img" src="bodybp_cover.png" alt="BodyBlueprint Pro Fitness App" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" loading="lazy"/>
            <div class="feat-proj-fallback" style="display:none;">
              <div class="feat-proj-fallback-icon">💪</div>
              <div class="feat-proj-fallback-text">BodyBlueprint Pro</div>
            </div>
            <div class="feat-proj-overlay"><div class="feat-proj-pill">Explore Case Study</div></div>
            <div class="feat-proj-num-badge">04</div>
            <div class="feat-proj-status-badge"><span class="green-dot" style="width:6px;height:6px;"></span> Live Deployed</div>
          </div>
        </article>

        <!-- 05 / DERMASENSE -->
        <article class="feat-project-row" data-project="dermasense">
          <div class="feat-proj-visual open-case" data-project="dermasense">
            <img class="feat-proj-img" src="aiml-ten_llm_dash.png" alt="DermaSense AI Diagnostics" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" loading="lazy"/>
            <div class="feat-proj-fallback" style="display:none;">
              <div class="feat-proj-fallback-icon">🔬</div>
              <div class="feat-proj-fallback-text">DermaSense Diagnostics</div>
            </div>
            <div class="feat-proj-overlay"><div class="feat-proj-pill">Explore Case Study</div></div>
            <div class="feat-proj-num-badge">05</div>
            <div class="feat-proj-status-badge">◐ In Development</div>
          </div>
          <div class="feat-proj-info">
            <div class="feat-proj-kicker">Dermatology AI · Deep Learning · In Development</div>
            <h3 class="feat-proj-title">DermaSense</h3>
            <p class="feat-proj-tagline">AI-assisted dermatological analysis pipeline for non-invasive skin lesion screening and risk stratification through deep neural networks.</p>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-microchip"></i> System Flow</div>
              <div class="feat-proj-flow">
                <span class="feat-flow-step">Dermoscopic Image</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Pre-Processing &amp; Normalization</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">CNN Feature Extraction</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Risk Assessment Output</span>
              </div>
            </div>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-user-gear"></i> What I Personally Engineered</div>
              <p class="feat-proj-block-text">Structuring the deep learning transfer learning model architecture, dataset augmentation routines, and clinical guidance score algorithms.</p>
            </div>
            <div class="feat-proj-tags">
              <span class="feat-proj-tag">Deep Learning</span>
              <span class="feat-proj-tag">Python</span>
              <span class="feat-proj-tag">PyTorch / TensorFlow</span>
              <span class="feat-proj-tag">Computer Vision</span>
              <span class="feat-proj-tag">FastAPI</span>
            </div>
            <div class="feat-proj-actions">
              <a href="javascript:void(0)" class="feat-proj-btn open-case" data-project="dermasense">View Case Study <i class="fas fa-arrow-right"></i></a>
            </div>
          </div>
        </article>

        <!-- 06 / NEXORA HACKATHON -->
        <article class="feat-project-row row-reverse" data-project="nexora">
          <div class="feat-proj-info">
            <div class="feat-proj-kicker">Rapid Prototype · 24h Hackathon Finalist</div>
            <h3 class="feat-proj-title">Nexora AI System</h3>
            <p class="feat-proj-tagline">Real-time modular software pipeline engineered under intense 24-hour hackathon conditions at Nexora — built for high throughput and rapid processing.</p>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-microchip"></i> System Flow</div>
              <div class="feat-proj-flow">
                <span class="feat-flow-step">Live Input Stream</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Async Router</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Micro-Inference Engine</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Real-Time State Store</span>
              </div>
            </div>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-user-gear"></i> What I Personally Engineered</div>
              <p class="feat-proj-block-text">Led the rapid backend architecture, connecting live asynchronous data pipelines with sub-second response times during hackathon evaluation rounds.</p>
            </div>
            <div class="feat-proj-tags">
              <span class="feat-proj-tag">Python</span>
              <span class="feat-proj-tag">FastAPI</span>
              <span class="feat-proj-tag">AsyncIO</span>
              <span class="feat-proj-tag">Real-Time Systems</span>
              <span class="feat-proj-tag">Git</span>
            </div>
            <div class="feat-proj-actions">
              <a href="javascript:void(0)" class="feat-proj-btn open-case" data-project="nexora">View Case Study <i class="fas fa-arrow-right"></i></a>
              <a href="https://github.com/allanborder" target="_blank" class="feat-proj-btn-ghost"><i class="fab fa-github"></i> GitHub</a>
            </div>
          </div>
          <div class="feat-proj-visual open-case" data-project="nexora">
            <img class="feat-proj-img" src="new_photo_2.jpg" alt="Nexora Hackathon Project" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" loading="lazy"/>
            <div class="feat-proj-fallback" style="display:none;">
              <div class="feat-proj-fallback-icon">⚡</div>
              <div class="feat-proj-fallback-text">Nexora Hackathon Build</div>
            </div>
            <div class="feat-proj-overlay"><div class="feat-proj-pill">Explore Case Study</div></div>
            <div class="feat-proj-num-badge">06</div>
            <div class="feat-proj-status-badge"><span class="green-dot" style="width:6px;height:6px;"></span> Hackathon Finalist</div>
          </div>
        </article>

      </div>

      <div class="works-footer">
        <span class="wf-text">More open-source repositories &amp; experiments on GitHub →</span>
        <a href="https://github.com/allanborder" target="_blank" class="wf-btn"><i class="fab fa-github"></i> github.com/allanborder</a>
      </div>
    </div>

    '''

content = content[:idx_start] + new_view_listing + content[idx_end:]

# 3. Replace the PROJECTS dictionary in JS: between `var PROJECTS={` and `/* ─── Case Study Builder ─── */`
p_start = content.find('var PROJECTS={')
p_end = content.find('/* ─── Case Study Builder ─── */')
assert p_start != -1 and p_end != -1, 'PROJECTS dictionary boundaries not found'

new_projects_dict = '''var PROJECTS={
  rj:{
    num:'01',badge:'Voice AI · Personal Assistant · Core System Built',title:'RJ — Personal AI Assistant',
    heroDesc:'RJ is my personal AI assistant built to interact with my system through voice, automate everyday tasks, maintain persistent memory, and provide an always-on intelligent interface.',
    coverImage:'ai_desk.png',coverBg:'linear-gradient(140deg,#111318,#20242c)',coverIcon:'🎙️',
    meta:[{k:'Type',v:'Personal Voice AI System'},{k:'Status',v:'Core System Built · Active Dev'},{k:'Stack',v:'Python + Groq + WebSockets'},{k:'Interface',v:'Voice & Live HUD'}],
    metrics:[{n:'Always-On',l:'Background Daemon'},{n:'<300ms',l:'Voice Stream Latency'},{n:'100%',l:'PC Automation'},{n:'Persistent',l:'Memory & Context'}],
    sections:[
      {id:'problem',label:'The Vision',title:'Why Build RJ',content:'<p class="cs2-prose">Most personal assistants are walled gardens — either locked inside commercial ecosystems or limited to basic text queries. I needed an assistant that truly lives on my machine, listens for its wake word without burning CPU, remembers past context, executes complex PC workflows, and talks back in real time.</p>'},
      {id:'solution',label:'The System',title:'How RJ Works',content:'<p class="cs2-prose">RJ operates as a persistent daemon with wake-word detection, multi-modal command parsing, and streaming audio synthesis. It bridges voice inputs with Groq-accelerated LLMs to handle mood detection, clipboard reading, application switching, system automation, and WebSocket terminal HUD synchronization.</p>'},
      {id:'arch',label:'Architecture',title:'System Flow',content:'<p class="cs2-prose">A continuous event loop coordinates hardware audio streams with cloud reasoning and native operating system controllers.</p>',arch:{nodes:[{i:'🎙️',l:'Voice / Wake Word',s:'PyAudio Listener'},{i:'🖥️',l:'WebSocket HUD',s:'Live Terminal UI'},{i:'⚡',l:'FastAPI / Async Engine',s:'Event Dispatcher',hl:true},{i:'🧠',l:'Groq LLM Pipeline',s:'Streaming Inference',hl:true},{i:'⚙️',l:'OS Controller & TTS',s:'Automation & Voice'}]}},
      {id:'features',label:'Features',title:'Core Capabilities',features:[{i:'🎙️',t:'Wake-Word Activation',d:'Lightweight background audio listener triggerable anytime hands-free.'},{i:'⚡',t:'Streaming LLM Responses',d:'Groq-accelerated inference providing conversational answers with low latency.'},{i:'🔊',t:'Optimized TTS Pipeline',d:'Fast text-to-speech engine with intelligent phrase caching for instant playback.'},{i:'🧠',t:'Persistent SQLite Memory',d:'Maintains interaction history, personal preferences, and context across sessions.'},{i:'💻',t:'Full PC & App Automation',d:'Launches/closes tools, manages browser tabs, manipulates clipboard, and controls media.'},{i:'📊',t:'Real-Time Terminal HUD',d:'WebSocket-synchronized HUD display visualizing system state, audio wave, and logs.'}]},
      {id:'quote',label:'',title:'',quote:{t:'RJ isn\\'t a generic chatbot. It is a genuine extension of my developer environment — built to automate what slows me down.',a:'Allan Paulraj on RJ'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'Core & Audio',tags:['Python 3.11+','PyAudio','SpeechRecognition','pyttsx3 / Edge-TTS']},{label:'AI & Reasoning',tags:['Groq Cloud API','Llama 3.3 / Mixtral','Context Store','Sentiment Parser']},{label:'Networking & UI',tags:['FastAPI','WebSockets','SQLite','AsyncIO','Terminal HUD']}]},
      {id:'results',label:'Results',title:'What Has Been Built',results:[{n:'Core',l:'System Built',d:'Actively expanding.'},{n:'<300ms',l:'Voice Latency',d:'Real-time stream.'},{n:'100%',l:'Local Automation',d:'Full OS hooks.'},{n:'Active',l:'Daily Use',d:'Personal workflow.'}]},
    ],
    github:'https://github.com/allanborder',live:null,nextKey:'smartpark'
  },
  smartpark:{
    num:'02',badge:'Full-Stack · Web App · 2025',title:'SmartPark',
    heroDesc:'A real-time parking management platform handling multi-floor capacity, dynamic pricing algorithms, and automated GST billing — built from scratch with Node.js and Express.',
    coverImage:'smartpark_cover.png',coverBg:'linear-gradient(140deg,#0A1628,#1A2B4A)',coverIcon:'🅿️',
    meta:[{k:'Type',v:'Full-Stack Web App'},{k:'Year',v:'2025'},{k:'Stack',v:'Node.js + SQLite'},{k:'Status',v:'Completed'}],
    metrics:[{n:'3',l:'Floors Managed'},{n:'<1s',l:'API Response'},{n:'0',l:'External DBs'},{n:'100%',l:'Real-Time'}],
    sections:[
      {id:'problem',label:'The Problem',title:'What Needed Solving',content:'<p class="cs2-prose">Parking lots with multiple floors face a persistent challenge: no live visibility into capacity, pricing inconsistencies, and paper-based billing that slows everything down. Attendants work blind. Revenue leaks. Drivers wait.</p>'},
      {id:'solution',label:'The Solution',title:'How It Was Built',content:'<p class="cs2-prose">SmartPark solves all three in a single unified system: real-time slot tracking, algorithmic dynamic pricing, and one-click GST billing that any attendant can use from a browser — <strong>zero training required</strong>.</p>'},
      {id:'arch',label:'Architecture',title:'System Flow',content:'<p class="cs2-prose">Engineered with a streamlined, modular architecture: client requests flow through Express REST routers, dynamically computing hourly tariffs before atomic commits to embedded SQLite.</p>',arch:{nodes:[{i:'👤',l:'User / Attendant',s:'Client'},{i:'🌐',l:'Web Interface',s:'Responsive UI'},{i:'⚡',l:'Express REST API',s:'Backend Routing',hl:true},{i:'💸',l:'Pricing Engine',s:'Tariffs & GST',hl:true},{i:'🗄️',l:'SQLite DB',s:'Local Persistence'}]}},
      {id:'features',label:'Features',title:'Core Capabilities',features:[{i:'⚡',t:'Real-Time Slot Tracking',d:'Live capacity across all 3 floors with instant updates on entry/exit.'},{i:'💸',t:'Dynamic Pricing Engine',d:'Configurable rate tables per floor with time-of-day multipliers.'},{i:'🧾',t:'One-Click GST Billing',d:'Auto-generated itemized receipts with full GST breakdown.'},{i:'📊',t:'Analytics Dashboard',d:'Chart.js visualizations showing occupancy trends and revenue.'},{i:'🔒',t:'Role-Based Access',d:'Separate attendant and admin views with controlled configuration.'},{i:'🗄️',t:'Embedded SQLite',d:'Lightweight local database with zero cloud dependencies.'},{i:'🔄',t:'Multi-Floor Coordination',d:'Centralized state prevents double-bookings across all floors.'},{i:'📱',t:'Responsive Interface',d:'Works cleanly on tablet or desktop for parking booth environments.'}]},
      {id:'quote',label:'',title:'',quote:{t:'The goal was designing a 60-second workflow that felt effortless for someone standing at a parking gate.',a:'Allan Paulraj on SmartPark'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'Backend',tags:['Node.js','Express.js','SQLite','REST API']},{label:'Frontend',tags:['JavaScript ES6+','Chart.js','HTML5 / CSS3']},{label:'Architecture',tags:['MVC Pattern','Role-Based Auth','Dynamic Pricing Algorithm']}]},
      {id:'results',label:'Results',title:'What Was Achieved',results:[{n:'3',l:'Floor Levels',d:'Real-time tracking.'},{n:'<1s',l:'Response Time',d:'Sub-second APIs.'},{n:'0',l:'External Deps',d:'Fully embedded.'},{n:'100%',l:'Uptime Target',d:'Built for ops.'}]},
    ],
    github:'https://github.com/allanborder',live:null,nextKey:'neuroai'
  },
  neuroai:{
    num:'03',badge:'Computer Vision · AI/ML · 2025',title:'NeuroAI',
    heroDesc:'An AI-powered medical imaging platform classifying brain MRI scans into four tumor categories using EfficientNetB0, then generating natural-language diagnostic reports via a local Mistral LLM.',
    coverImage:'neuroai_cover.png',coverBg:'linear-gradient(140deg,#1A1A2E,#2D2D4A)',coverIcon:'🧠',
    meta:[{k:'Type',v:'Medical AI System'},{k:'Year',v:'2025'},{k:'Stack',v:'TensorFlow + FastAPI'},{k:'Privacy',v:'100% Local'}],
    metrics:[{n:'97%+',l:'Accuracy'},{n:'4',l:'Tumor Classes'},{n:'0',l:'Data Sent Out'},{n:'<3s',l:'Scan to Report'}],
    sections:[
      {id:'problem',label:'The Problem',title:'What Needed Solving',content:'<p class="cs2-prose">Brain tumor classification from MRI scans is slow and specialist-gated. Clinicians often wait days for a preliminary read — a problem that compounds in under-resourced hospitals where a radiologist may not be immediately available.</p>'},
      {id:'solution',label:'The Solution',title:'How It Was Built',content:'<p class="cs2-prose">NeuroAI accelerates initial triage — instantly classifying a scan as <strong>Glioma, Meningioma, Pituitary, or No Tumor</strong>, then generating a readable diagnostic summary using Mistral 7B running entirely on-device. No cloud. No patient data leaves the machine.</p>'},
      {id:'arch',label:'Architecture',title:'System Flow',content:'<p class="cs2-prose">The complete diagnostic pipeline runs on-device without remote calls: user uploads MRI image, FastAPI processes tensors, EfficientNetB0 generates class distributions, and Mistral LLM formats readable clinical summaries.</p>',arch:{nodes:[{i:'👨‍⚕️',l:'Clinician',s:'User'},{i:'⚛️',l:'React Frontend',s:'Scan Upload & UI'},{i:'⚡',l:'FastAPI Gateway',s:'Async Ingestion'},{i:'🔬',l:'EfficientNetB0',s:'CV Classification',hl:true},{i:'🤖',l:'Mistral 7B',s:'Local LLM Summary',hl:true}]}},
      {id:'features',label:'Features',title:'Core Capabilities',features:[{i:'🔬',t:'EfficientNetB0 Backbone',d:'Fine-tuned on augmented MRI datasets achieving >97% accuracy across all four types.'},{i:'🤖',t:'Mistral LLM Reports',d:'Local Ollama generates human-readable diagnostic summaries from classification outputs.'},{i:'⚡',t:'FastAPI Async Backend',d:'High-performance async Python handles upload, preprocessing, and inference without blocking.'},{i:'⚛️',t:'React Frontend',d:'Drag-and-drop MRI upload with real-time results and downloadable report display.'},{i:'🔒',t:'100% Local Inference',d:'Both CV model and LLM run on-device — no patient data ever leaves the machine.'},{i:'📁',t:'Multi-Format Support',d:'Accepts DICOM, PNG, and JPG MRI inputs with automatic preprocessing.'},{i:'📊',t:'Confidence Scores',d:'Returns per-class probability scores alongside the top prediction.'},{i:'🔄',t:'Batch Processing',d:'Queue multiple scans for sequential inference in a single session.'}]},
      {id:'quote',label:'',title:'',quote:{t:'Real AI capability is not just about model weights, but about how cleanly the inference pipeline hands off results to human workflows.',a:'Allan Paulraj on NeuroAI'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'AI / ML',tags:['TensorFlow','EfficientNetB0','Ollama','Mistral 7B','NumPy','OpenCV']},{label:'Backend',tags:['Python','FastAPI','AsyncIO','REST API']},{label:'Frontend',tags:['React','Recharts','Tailwind CSS']}]},
      {id:'results',label:'Results',title:'What Was Achieved',results:[{n:'97%+',l:'Accuracy',d:'All 4 classes.'},{n:'4',l:'Tumor Classes',d:'Full coverage.'},{n:'0',l:'Data Sent',d:'Full privacy.'},{n:'<3s',l:'End-to-End',d:'Scan to report.'}]},
    ],
    github:'https://github.com/allanborder',live:null,nextKey:'bodybp'
  },
  bodybp:{
    num:'04',badge:'React · Live · Vercel · 2025',title:'BodyBlueprint Pro',
    heroDesc:'A personal fitness performance tracker built in React — featuring timeline data visualization, personal record logging per exercise, AI coaching via Llama 3.3 70B, and a responsive UI deployed live on Vercel.',
    coverImage:'bodybp_cover.png',coverBg:'linear-gradient(140deg,#1C2A1A,#2A3D28)',coverIcon:'💪',
    meta:[{k:'Type',v:'React Web App'},{k:'Status',v:'Live on Vercel'},{k:'AI',v:'Llama 3.3 70B'},{k:'Privacy',v:'100% Client-Side'}],
    metrics:[{n:'Live',l:'Deployed'},{n:'14+',l:'Body Metrics'},{n:'~0ms',l:'Server Latency'},{n:'100%',l:'Privacy'}],
    sections:[
      {id:'problem',label:'The Problem',title:'What Needed Solving',content:'<p class="cs2-prose">Tracking gym performance over time is frustrating — spreadsheets are tedious, apps are overkill or locked behind subscriptions. There was no fast, private, zero-signup tracker that actually showed your progress visually.</p>'},
      {id:'solution',label:'The Solution',title:'How It Was Built',content:'<p class="cs2-prose">A focused, fast, privacy-first tracker: log exercises, weights, and reps — watch your progress charted over time with <strong>automatic PR detection</strong> and an AI coach powered by Groq API. No account. No server. Instant load.</p>'},
      {id:'arch',label:'Architecture',title:'System Flow',content:'<p class="cs2-prose">Designed as a client-first Single Page Application where data operations occur immediately in local storage, querying AI guidance through serverless proxy routes only when requested.</p>',arch:{nodes:[{i:'🏋️',l:'User',s:'Athlete / Lifter'},{i:'⚛️',l:'React UI',s:'Vite SPA'},{i:'📊',l:'Viz Engine',s:'Recharts'},{i:'🤖',l:'AI Coach',s:'Groq API / Llama 3',hl:true},{i:'💾',l:'LocalStorage',s:'Zero Backend'}]}},
      {id:'features',label:'Features',title:'Core Capabilities',features:[{i:'📈',t:'Timeline Visualization',d:'Recharts line graphs showing weight progression across all logged sessions.'},{i:'🏆',t:'Auto PR Detection',d:'Automatically detects and highlights new personal records on every log.'},{i:'🤖',t:'AI Fitness Coach',d:'Groq-powered Llama 3.3 70B provides personalised workout and nutrition advice.'},{i:'📏',t:'14+ Body Measurements',d:'Track chest, arms, waist, legs, and more with dedicated measurement logging.'},{i:'📱',t:'Fully Responsive',d:'Optimized for mobile (gym use) and desktop (home review) layouts.'},{i:'⚡',t:'Instant Load on Vercel',d:'CDN-deployed SPA loads in under a second on any connection.'},{i:'🔒',t:'LocalStorage Persistence',d:'All data lives in your browser — zero backend, zero account, zero privacy concerns.'},{i:'🎨',t:'Clean Dark Interface',d:'Gym-appropriate dark UI with high contrast — readable under any lighting.'}]},
      {id:'quote',label:'',title:'',quote:{t:'No accounts, no ads, no paywalls — just your data, your progress, your results.',a:'Allan Paulraj on BodyBlueprint Pro'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'Frontend',tags:['React','Vite','Tailwind CSS','Recharts']},{label:'AI & API',tags:['Groq Cloud','Llama 3.3 70B','Proxy Endpoints']},{label:'Deployment',tags:['Vercel','Edge CDN','LocalStorage']}]},
      {id:'results',label:'Results',title:'What Was Achieved',results:[{n:'Live',l:'On Vercel',d:'Publicly accessible.'},{n:'14+',l:'Body Metrics',d:'Full tracking.'},{n:'~0ms',l:'Server Latency',d:'Client-side only.'},{n:'100%',l:'Privacy',d:'No tracking.'}]},
    ],
    github:'https://github.com/allanborder/body-blueprint-2',live:'https://body-blueprint-2.vercel.app/',nextKey:'dermasense'
  },
  dermasense:{
    num:'05',badge:'Dermatology AI · Diagnostics · In Development',title:'DermaSense',
    heroDesc:'An AI-assisted dermatological diagnostic pipeline designed for non-invasive skin lesion classification and automated risk factor analysis using deep convolutional networks.',
    coverImage:'aiml-ten_llm_dash.png',coverBg:'linear-gradient(140deg,#1c1b24,#282436)',coverIcon:'🔬',
    meta:[{k:'Type',v:'Medical AI Diagnostic System'},{k:'Status',v:'In Development · Model Training'},{k:'Stack',v:'PyTorch + FastAPI'},{k:'Focus',v:'Lesion Risk Scoring'}],
    metrics:[{n:'Active',l:'In Development'},{n:'Multi-Class',l:'Lesion Detection'},{n:'Fast',l:'Inference Target'},{n:'Local/Cloud',l:'Hybrid Architecture'}],
    sections:[
      {id:'problem',label:'The Challenge',title:'Dermatology Triage Gap',content:'<p class="cs2-prose">Dermatological evaluations frequently face access bottlenecks. Early screening of suspicious skin anomalies requires specialized dermoscopy tools that may not be readily available in primary care settings.</p>'},
      {id:'solution',label:'The Architecture',title:'How DermaSense Operates',content:'<p class="cs2-prose">Developing an automated vision pipeline that standardizes clinical dermoscopic imagery, applies deep convolutional feature extraction, and outputs probabilistic malignancy risk scores with explanatory heatmaps.</p>'},
      {id:'arch',label:'Architecture',title:'System Flow',content:'<p class="cs2-prose">Client uploads high-resolution dermoscopic image; backend preprocessing standardizes color space and lighting before executing neural feature extraction.</p>',arch:{nodes:[{i:'📸',l:'Dermoscopic Image',s:'Clinical Input'},{i:'⚡',l:'Preprocessing',s:'Color Normalization'},{i:'🔬',l:'CNN Backbone',s:'Feature Extractor',hl:true},{i:'📊',l:'Classifier Head',s:'Risk Probability',hl:true},{i:'📄',l:'Diagnostic Summary',s:'Clinical Output'}]}},
      {id:'features',label:'Features',title:'Core Development Goals',features:[{i:'🔬',t:'Deep Feature Extraction',d:'Transfer-learning neural network trained on standardized dermatological datasets.'},{i:'🎯',t:'Risk Stratification',d:'Provides calibrated risk scoring to help clinicians prioritize urgent cases.'},{i:'⚡',t:'High-Performance Backend',d:'FastAPI inference server capable of processing high-resolution images rapidly.'},{i:'🔒',t:'Privacy-Conscious Design',d:'Strict data handling protocols ensuring patient imagery is protected.'}]},
      {id:'quote',label:'',title:'',quote:{t:'The objective is building diagnostic tools that assist medical professionals with clear, calibrated predictions.',a:'Allan Paulraj on DermaSense'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'Deep Learning',tags:['PyTorch','TensorFlow','OpenCV','Albumentations']},{label:'Backend & Serving',tags:['Python','FastAPI','NumPy','Docker']}]},
      {id:'results',label:'Status',title:'Development Milestones',results:[{n:'Active',l:'Model Training',d:'Tuning neural weights.'},{n:'Pipeline',l:'Built',d:'FastAPI service.'},{n:'In Dev',l:'Status',d:'Continuous improvement.'},{n:'100%',l:'Targeted Focus',d:'Clinical precision.'}]},
    ],
    github:'https://github.com/allanborder',live:null,nextKey:'nexora'
  },
  nexora:{
    num:'06',badge:'Hackathon · AI Pipeline · 2025',title:'Nexora AI System',
    heroDesc:'A rapid-prototype real-time AI and data processing solution engineered under intense 24-hour hackathon conditions at Nexora — featuring modular pipelines and sub-second processing.',
    coverImage:'new_photo_2.jpg',coverBg:'linear-gradient(140deg,#1e1e24,#2d3142)',coverIcon:'⚡',
    meta:[{k:'Type',v:'Hackathon Prototype'},{k:'Year',v:'2025'},{k:'Stack',v:'Python + FastAPI'},{k:'Format',v:'24h Rapid Sprint'}],
    metrics:[{n:'24h',l:'Sprint Build'},{n:'<500ms',l:'Pipeline Latency'},{n:'100%',l:'Modular Flow'},{n:'Team',l:'Collaborative'}],
    sections:[
      {id:'problem',label:'The Problem',title:'Hackathon Challenge',content:'<p class="cs2-prose">During rapid competitive development, building a system that balances complex AI processing with immediate, predictable real-time response is notoriously difficult without compromising stability.</p>'},
      {id:'solution',label:'The Solution',title:'Our Solution',content:'<p class="cs2-prose">Built a clean modular processing pipeline that decouples ingestion from heavy compute routines, allowing rapid iteration, accurate inference, and seamless presentation during the evaluation rounds.</p>'},
      {id:'arch',label:'Architecture',title:'System Flow',content:'<p class="cs2-prose">Clean 5-tier architecture connecting the client input interface directly to asynchronous backend pipelines, local worker processing, and rapid data storage.</p>',arch:{nodes:[{i:'👥',l:'Hackathon Team',s:'Input & Ingestion'},{i:'🖥️',l:'Frontend View',s:'Real-Time UI'},{i:'⚡',l:'FastAPI Router',s:'Async Dispatch',hl:true},{i:'🧠',l:'Processing Engine',s:'AI / Model Pipeline',hl:true},{i:'🗄️',l:'Data Store',s:'Structured State'}]}},
      {id:'features',label:'Features',title:'Key Highlights',features:[{i:'⚡',t:'24-Hour Rapid Sprint',d:'Engineered, verified, and presented end-to-end within strict competition time limits.'},{i:'🔄',t:'Modular Async Pipeline',d:'Decoupled backend routing for maximum throughput and easy live tuning.'},{i:'🧠',t:'Intelligent Processing',d:'Integrated AI/ML logic handling automated data transformation and feature extraction.'},{i:'📊',t:'Real-Time Output Stream',d:'Immediate visual feedback allowing instant validation of model predictions.'}]},
      {id:'quote',label:'',title:'',quote:{t:'Hackathons test your instincts. You learn to make architectural decisions quickly and build what actually works.',a:'Allan Paulraj on Nexora'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'Backend & AI',tags:['Python','FastAPI','NumPy','AsyncIO']},{label:'Tools & Collab',tags:['Git','GitHub','REST API Architecture']}]},
      {id:'results',label:'Results',title:'What Was Achieved',results:[{n:'24h',l:'Turnaround',d:'Rapidly built.'},{n:'<500ms',l:'Response',d:'High throughput.'},{n:'Finalist',l:'Recognition',d:'Evaluated live.'},{n:'100%',l:'Working Demo',d:'Shipped on time.'}]},
    ],
    github:'https://github.com/allanborder',live:null,nextKey:'rj'
  }
};
'''

content = content[:p_start] + new_projects_dict + content[p_end:]

# 4. Update Terminal Projects command list
old_term_p = "['<span class=\"t-o\">1. <span class=\"t-v\">SmartPark</span>         — Multi-floor parking (Node + SQLite)</span>','<span class=\"t-o\">2. <span class=\"t-v\">NeuroAI</span>           — Brain MRI classification (EfficientNetB0)</span>','<span class=\"t-o\">3. <span class=\"t-v\">BodyBlueprint Pro</span> — Fitness tracker (React + Vercel)</span>','<span class=\"t-o\">4. <span class=\"t-v\">IndPopHub</span>         — India population analytics dashboard</span>','<span class=\"t-o\">5. <span class=\"t-v\">Nexora AI</span>         — Hackathon prototype pipeline</span>'];"
new_term_p = "['<span class=\"t-o\">1. <span class=\"t-v\">RJ</span>                — Personal AI Assistant (Voice + Automation)</span>','<span class=\"t-o\">2. <span class=\"t-v\">SmartPark</span>         — Real-Time Parking Platform (Node + SQLite)</span>','<span class=\"t-o\">3. <span class=\"t-v\">NeuroAI</span>           — Brain MRI Classification (EfficientNetB0)</span>','<span class=\"t-o\">4. <span class=\"t-v\">BodyBlueprint Pro</span> — Fitness &amp; PR Tracker (React + Groq)</span>','<span class=\"t-o\">5. <span class=\"t-v\">DermaSense</span>        — Dermatology AI Diagnostics (In Dev)</span>','<span class=\"t-o\">6. <span class=\"t-v\">Nexora AI</span>         — Rapid Hackathon Pipeline</span>'];"

if old_term_p in content:
    content = content.replace(old_term_p, new_term_p, 1)

# 5. Update Intersection Observer and event handlers
old_obs_part = "document.querySelectorAll('.proj-card').forEach(function(el,i){el.style.transition='opacity .9s cubic-bezier(.16,1,.3,1) '+(i*.1)+'s,transform .9s cubic-bezier(.16,1,.3,1) '+(i*.1)+'s';obs.observe(el);});"
new_obs_part = "document.querySelectorAll('.feat-project-row').forEach(function(el,i){el.style.transition='opacity .8s cubic-bezier(.16,1,.3,1) '+(i*.08)+'s,transform .8s cubic-bezier(.16,1,.3,1) '+(i*.08)+'s';obs.observe(el);});"
if old_obs_part in content:
    content = content.replace(old_obs_part, new_obs_part, 1)

old_cur_p = "document.querySelectorAll('.proj-card,.cs2-next-card').forEach(function(el){el.addEventListener('mouseenter',function(){c.classList.remove('link');c.classList.add('card');c.dataset.text='OPEN';});el.addEventListener('mouseleave',function(){c.classList.remove('card');c.dataset.text='VIEW';});});"
new_cur_p = "document.querySelectorAll('.feat-proj-visual,.cs2-next-card').forEach(function(el){el.addEventListener('mouseenter',function(){c.classList.remove('link');c.classList.add('card');c.dataset.text='OPEN';});el.addEventListener('mouseleave',function(){c.classList.remove('card');c.dataset.text='VIEW';});});"
if old_cur_p in content:
    content = content.replace(old_cur_p, new_cur_p, 1)

# 6. Make sure open-case listener binds properly to all new buttons and visual cards
old_open_case_bindings = """document.querySelectorAll('.proj-card').forEach(function(card){
  card.addEventListener('click',function(e){if(e.target.closest('.pc-cta'))return;showCase(this.dataset.project);});
});
document.querySelectorAll('.open-case').forEach(function(btn){
  btn.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();showCase(this.dataset.project);});
});"""

new_open_case_bindings = """document.querySelectorAll('.open-case').forEach(function(btn){
  btn.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();showCase(this.dataset.project);});
});"""

if old_open_case_bindings in content:
    content = content.replace(old_open_case_bindings, new_open_case_bindings, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated index.html directly and cleanly!')
