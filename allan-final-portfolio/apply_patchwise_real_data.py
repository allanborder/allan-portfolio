with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. Update featured project section tagline & kicker for Patchwise ───
old_p6_section = '''          <div class="feat-proj-info">
            <div class="feat-proj-kicker">Nexora Hackathon Finalist · Rapid Prototype</div>
            <h3 class="feat-proj-title">Patchwise</h3>
            <p class="feat-proj-tagline">Intelligent real-time pipeline engineered under intense 24-hour hackathon sprint conditions at Nexora — built for high throughput and rapid modular processing.</p>
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
          </div>'''

new_p6_section = '''          <div class="feat-proj-info">
            <div class="feat-proj-kicker">Nexora Hackathon Finalist · Cybersecurity AI · Live on Vercel</div>
            <h3 class="feat-proj-title">Patchwise</h3>
            <p class="feat-proj-tagline">AI-powered vulnerability triage platform that prioritises security flaws using business context — combining CVSS, EPSS, CISA KEV, and service criticality into an explainable 0–100 risk score.</p>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-microchip"></i> Scoring Pipeline</div>
              <div class="feat-proj-flow">
                <span class="feat-flow-step">CVSS + EPSS Signals</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">CISA KEV Check</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Org Context Engine</span>
                <span class="feat-flow-arrow">→</span>
                <span class="feat-flow-step">Priority Score (0–100)</span>
              </div>
            </div>
            <div class="feat-proj-block">
              <div class="feat-proj-block-label"><i class="fas fa-user-gear"></i> What I Personally Engineered</div>
              <p class="feat-proj-block-text">Built the deterministic multi-signal scoring engine, CISA KEV integration, AI-powered vulnerability explanation layer, and organisation-aware risk prioritisation — all under 24h sprint conditions.</p>
            </div>
            <div class="feat-proj-tags">
              <span class="feat-proj-tag">Python</span>
              <span class="feat-proj-tag">React + Vite</span>
              <span class="feat-proj-tag">CVSS / EPSS</span>
              <span class="feat-proj-tag">CISA KEV API</span>
              <span class="feat-proj-tag">AI Explanations</span>
            </div>
            <div class="feat-proj-actions">
              <a href="javascript:void(0)" class="feat-proj-btn open-case" data-project="nexora">View Case Study <i class="fas fa-arrow-right"></i></a>
              <a href="https://patchwise.vercel.app/" target="_blank" class="feat-proj-btn-ghost"><i class="fas fa-external-link-alt"></i> Live Demo</a>
              <a href="https://github.com/allanborder/PatchWise" target="_blank" class="feat-proj-btn-ghost"><i class="fab fa-github"></i> GitHub</a>
            </div>
          </div>'''

assert old_p6_section in content, 'old_p6_section not found'
content = content.replace(old_p6_section, new_p6_section, 1)

# ─── 2. Update PROJECTS dictionary for nexora/Patchwise ───
old_nexora_dict = '''  nexora:{
    num:'06',badge:'Nexora Hackathon Finalist · Rapid Prototype · 2025',title:'Patchwise',
    heroDesc:'An intelligent real-time processing solution engineered under intense 24-hour hackathon conditions at Nexora — featuring modular pipelines and sub-second execution.',

    coverImage:'patchwise_dash.jpg',coverBg:'linear-gradient(140deg,#1e1e24,#2d3142)',coverIcon:'⚡',
    meta:[{k:'Type',v:'Hackathon Prototype'},{k:'Year',v:'2025'},{k:'Stack',v:'Python + FastAPI'},{k:'Format',v:'24h Rapid Sprint'}],
    metrics:[{n:'24h',l:'Sprint Build'},{n:'<500ms',l:'Pipeline Latency'},{n:'100%',l:'Modular Flow'},{n:'Team',l:'Collaborative'}],
    sections:[
      {id:'problem',label:'The Problem',title:'Hackathon Challenge',content:'<p class="cs2-prose">During rapid competitive development, building a system that balances complex AI processing with immediate, predictable real-time response is notoriously difficult without compromising stability.</p>'},
      {id:'solution',label:'The Solution',title:'Our Solution',content:'<p class="cs2-prose">Built a clean modular processing pipeline that decouples ingestion from heavy compute routines, allowing rapid iteration, accurate inference, and seamless presentation during the evaluation rounds.</p>'},
      {id:'arch',label:'Architecture',title:'System Flow',content:'<p class="cs2-prose">Clean 5-tier architecture connecting the client input interface directly to asynchronous backend pipelines, local worker processing, and rapid data storage.</p>',arch:{nodes:[{i:'👥',l:'Hackathon Team',s:'Input & Ingestion'},{i:'🖥️',l:'Frontend View',s:'Real-Time UI'},{i:'⚡',l:'FastAPI Router',s:'Async Dispatch',hl:true},{i:'🧠',l:'Processing Engine',s:'AI / Model Pipeline',hl:true},{i:'🗄️',l:'Data Store',s:'Structured State'}]}},
      {id:'features',label:'Features',title:'Key Highlights',features:[{i:'⚡',t:'24-Hour Rapid Sprint',d:'Engineered, verified, and presented end-to-end within strict competition time limits.'},{i:'🔄',t:'Modular Async Pipeline',d:'Decoupled backend routing for maximum throughput and easy live tuning.'},{i:'🧠',t:'Intelligent Processing',d:'Integrated AI/ML logic handling automated data transformation and feature extraction.'},{i:'📊',t:'Real-Time Output Stream',d:'Immediate visual feedback allowing instant validation of model predictions.'}]},
      {id:'quote',label:'',title:'',quote:{t:'Hackathons test your instincts. You learn to make architectural decisions quickly and build what actually works.',a:'Allan Paulraj on Patchwise'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'Backend & AI',tags:['Python','FastAPI','NumPy','AsyncIO']},{label:'Tools & Collab',tags:['Git','GitHub','REST API Architecture']}]},
      {id:'results',label:'Results',title:'What Was Achieved',results:[{n:'24h',l:'Turnaround',d:'Rapidly built.'},{n:'<500ms',l:'Response',d:'High throughput.'},{n:'Finalist',l:'Recognition',d:'Evaluated live.'},{n:'100%',l:'Working Demo',d:'Shipped on time.'}]},
    ],
    github:'https://github.com/allanborder',live:null,nextKey:'rj'
  }'''

new_nexora_dict = '''  nexora:{
    num:'06',badge:'Nexora Hackathon Finalist · Cybersecurity AI · 2025',title:'Patchwise',
    heroDesc:'An AI-powered vulnerability triage and risk prioritisation platform built at the Nexora 24-Hour Hackathon. Instead of treating every vulnerability equally, PatchWise combines CVSS, EPSS, CISA KEV, internet exposure, and service criticality into an explainable 0–100 priority score — giving security teams clarity on what actually matters to their organisation.',
    coverImage:'patchwise_dash.jpg',coverBg:'linear-gradient(140deg,#0f1923,#1a2436)',coverIcon:'🛡️',
    meta:[{k:'Type',v:'Cybersecurity AI Platform'},{k:'Year',v:'2025'},{k:'Stack',v:'React + Python'},{k:'Status',v:'Live on Vercel'}],
    metrics:[{n:'0–100',l:'Risk Score'},{n:'5+',l:'Security Signals'},{n:'24h',l:'Hackathon Build'},{n:'Live',l:'On Vercel'}],
    sections:[
      {id:'problem',label:'The Problem',title:'The Vulnerability Overload Crisis',content:'<p class="cs2-prose">Security teams face hundreds of vulnerabilities daily. Traditional tools rank them purely by global CVSS severity — leading to thousands of "Critical" alerts that cause alert fatigue, delayed response to real threats, and wasted time on irrelevant issues. What was missing: <strong>organisational context</strong>.</p>'},
      {id:'solution',label:'The Solution',title:'Business-Context Vulnerability Intelligence',content:'<p class="cs2-prose">PatchWise reframes the question from <em>"Which vulnerabilities are globally severe?"</em> to <em>"Which vulnerabilities matter most to THIS organisation?"</em> — combining multiple live security data sources with service criticality and internet exposure into a single explainable priority score. No black-box. Every factor is visible and weighted.</p>'},
      {id:'arch',label:'Architecture',title:'Scoring Pipeline',content:'<p class="cs2-prose">The scoring engine combines five independent signals into a deterministic, auditable priority score. Each contribution is individually weighted and fully explainable — no ML black-box.</p>',arch:{nodes:[{i:'🔍',l:'CVE Input',s:'Vulnerability ID'},{i:'📊',l:'CVSS + EPSS',s:'Severity Signals'},{i:'🏛️',l:'CISA KEV',s:'Known Exploited',hl:true},{i:'🏢',l:'Org Context',s:'Service Criticality',hl:true},{i:'🎯',l:'Priority Score',s:'0–100 Risk'}]}},
      {id:'features',label:'Features',title:'Core Capabilities',features:[
        {i:'📊',t:'Multi-Signal Scoring',d:'Combines CVSS severity, EPSS exploitation probability, CISA KEV status, internet exposure, and service importance into one score.'},
        {i:'🏛️',t:'CISA KEV Integration',d:'Real-time lookup against the CISA Known Exploited Vulnerabilities catalogue for known in-the-wild threats.'},
        {i:'🏢',t:'Organisation-Aware Prioritisation',d:'Weights vulnerabilities based on your specific service criticality — a vuln on a core payment API scores higher than the same vuln on a dev tool.'},
        {i:'🤖',t:'AI Vulnerability Explanations',d:'Each prioritised vulnerability includes an AI-generated plain-English explanation — what it is, why it matters, what to do.'},
        {i:'🔎',t:'Explainable 0–100 Risk Score',d:'Every score shows exactly which signals contributed and by how much. Full transparency, zero black-box.'},
        {i:'📋',t:'Audit Logging',d:'Full audit trail of all triage decisions and scoring events for compliance and incident review.'}
      ]},
      {id:'quote',label:'',title:'',quote:{t:'The insight that changed everything: a critical CVE on a test server is far less urgent than a medium CVE on a customer-facing payment API.',a:'Allan Paulraj on Patchwise'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[
        {label:'Frontend',tags:['React','Vite','Vercel']},
        {label:'Backend & APIs',tags:['Python','FastAPI','CISA KEV API','EPSS API','NVD / CVSS']},
        {label:'AI & Security',tags:['AI Explanation Engine','Deterministic Scoring','Audit Logger','Negative Testing']}
      ]},
      {id:'results',label:'Results',title:'What Was Achieved',results:[{n:'Live',l:'On Vercel',d:'Publicly deployed.'},{n:'5+',l:'Data Signals',d:'Multi-source scoring.'},{n:'Finalist',l:'Nexora Hackathon',d:'Evaluated live.'},{n:'0–100',l:'Explainable Score',d:'Full transparency.'}]},
    ],
    github:'https://github.com/allanborder/PatchWise',live:'https://patchwise.vercel.app/',nextKey:'rj'
  }'''

assert old_nexora_dict in content, 'old_nexora_dict not found'
content = content.replace(old_nexora_dict, new_nexora_dict, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Patchwise updated with real GitHub data + live Vercel link!')
