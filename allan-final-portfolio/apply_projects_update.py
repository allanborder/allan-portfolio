with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update works-count
old_count = '''<div class="works-count">2024 – 2026 · 4 selected works</div>'''
new_count = '''<div class="works-count">2024 – 2026 · 5 selected works</div>'''
assert old_count in content, 'old_count not found'
content = content.replace(old_count, new_count, 1)

# 2. Add Project 05: Nexora Hackathon in the HTML projects-grid
old_proj_end = '''        <!-- PROJECT 04: IndPopHub -->
        <div class="proj-card" data-project="indpophub">
          <div class="pc-thumb">
            <div class="pc-thumb-inner">
              <img class="pc-thumb-img" src="indpophub_cover.png" alt="IndPopHub" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" loading="lazy"/>
              <div class="pc-thumb-bg" style="display:none;background:linear-gradient(140deg,#0D1B2A,#1B3A5C);">
                <svg width="260" height="160" viewBox="0 0 260 160" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <rect x="20" y="100" width="28" height="45" fill="rgba(99,179,237,.7)" rx="3"/>
                  <rect x="60" y="70" width="28" height="75" fill="rgba(99,179,237,.9)" rx="3"/>
                  <rect x="100" y="50" width="28" height="95" fill="rgba(99,179,237,1)" rx="3"/>
                  <rect x="140" y="80" width="28" height="65" fill="rgba(99,179,237,.75)" rx="3"/>
                  <rect x="180" y="35" width="28" height="110" fill="rgba(99,179,237,.95)" rx="3"/>
                  <rect x="220" y="60" width="28" height="85" fill="rgba(99,179,237,.8)" rx="3"/>
                </svg>
              </div>
            </div>
            <div class="pc-thumb-overlay"><div class="pc-pill">Open Case Study</div></div>
            <div class="pc-num-badge">04</div><div class="pc-year-badge">2025 · Live</div>
          </div>
          <div class="pc-body">
            <div class="pc-category">Data Viz · Analytics Dashboard</div>
            <div class="pc-title">IndPopHub</div>
            <p class="pc-desc">India Population Intelligence — an interactive real-time analytics dashboard with choropleth maps, Pearson correlation heatmaps, Pareto analysis, and live demographic counters.</p>
            <div class="pc-tags"><span class="pc-tag">Vanilla JS</span><span class="pc-tag">Chart.js</span><span class="pc-tag">SVG Maps</span><span class="pc-tag">Statistics</span><span class="pc-tag">CSV Upload</span></div>
            <div class="pc-footer">
              <a href="javascript:void(0)" class="pc-cta open-case" data-project="indpophub">View Case Study <span class="pc-arrow"><i class="fas fa-arrow-right"></i></span></a>
              <span class="pc-meta-txt">12 Chart Types · Live Counters</span>
            </div>
          </div>
        </div>
      </div>'''

new_proj_end = '''        <!-- PROJECT 04: IndPopHub -->
        <div class="proj-card" data-project="indpophub">
          <div class="pc-thumb">
            <div class="pc-thumb-inner">
              <img class="pc-thumb-img" src="indpophub_cover.png" alt="IndPopHub" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" loading="lazy"/>
              <div class="pc-thumb-bg" style="display:none;background:linear-gradient(140deg,#0D1B2A,#1B3A5C);">
                <svg width="260" height="160" viewBox="0 0 260 160" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <rect x="20" y="100" width="28" height="45" fill="rgba(99,179,237,.7)" rx="3"/>
                  <rect x="60" y="70" width="28" height="75" fill="rgba(99,179,237,.9)" rx="3"/>
                  <rect x="100" y="50" width="28" height="95" fill="rgba(99,179,237,1)" rx="3"/>
                  <rect x="140" y="80" width="28" height="65" fill="rgba(99,179,237,.75)" rx="3"/>
                  <rect x="180" y="35" width="28" height="110" fill="rgba(99,179,237,.95)" rx="3"/>
                  <rect x="220" y="60" width="28" height="85" fill="rgba(99,179,237,.8)" rx="3"/>
                </svg>
              </div>
            </div>
            <div class="pc-thumb-overlay"><div class="pc-pill">Open Case Study</div></div>
            <div class="pc-num-badge">04</div><div class="pc-year-badge">2025 · Live</div>
          </div>
          <div class="pc-body">
            <div class="pc-category">Data Viz · Analytics Dashboard</div>
            <div class="pc-title">IndPopHub</div>
            <p class="pc-desc">India Population Intelligence — an interactive real-time analytics dashboard with choropleth maps, Pearson correlation heatmaps, Pareto analysis, and live demographic counters.</p>
            <div class="pc-tags"><span class="pc-tag">Vanilla JS</span><span class="pc-tag">Chart.js</span><span class="pc-tag">SVG Maps</span><span class="pc-tag">Statistics</span><span class="pc-tag">CSV Upload</span></div>
            <div class="pc-footer">
              <a href="javascript:void(0)" class="pc-cta open-case" data-project="indpophub">View Case Study <span class="pc-arrow"><i class="fas fa-arrow-right"></i></span></a>
              <span class="pc-meta-txt">12 Chart Types · Live Counters</span>
            </div>
          </div>
        </div>
        <!-- PROJECT 05: Nexora Hackathon System -->
        <div class="proj-card" data-project="nexora">
          <div class="pc-thumb">
            <div class="pc-thumb-inner">
              <img class="pc-thumb-img" src="new_photo_2.jpg" alt="Nexora Project" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" loading="lazy"/>
              <div class="pc-thumb-bg" style="display:none;background:linear-gradient(140deg,#1e1e24,#2d3142);"><span style="font-size:3rem;">⚡</span></div>
            </div>
            <div class="pc-thumb-overlay"><div class="pc-pill">Open Case Study</div></div>
            <div class="pc-num-badge">05</div><div class="pc-year-badge">Hackathon · 2025</div>
          </div>
          <div class="pc-body">
            <div class="pc-category">Rapid Prototype · Hackathon</div>
            <div class="pc-title">Nexora AI System</div>
            <p class="pc-desc">Rapidly engineered real-time software pipeline built under 24-hour sprint conditions at the Nexora Hackathon with modular architecture.</p>
            <div class="pc-tags"><span class="pc-tag">Python</span><span class="pc-tag">FastAPI</span><span class="pc-tag">AI Pipeline</span><span class="pc-tag">REST API</span><span class="pc-tag">Git</span></div>
            <div class="pc-footer">
              <a href="javascript:void(0)" class="pc-cta open-case" data-project="nexora">View Case Study <span class="pc-arrow"><i class="fas fa-arrow-right"></i></span></a>
              <span class="pc-meta-txt">24h Sprint · Team Pipeline</span>
            </div>
          </div>
        </div>
      </div>'''

assert old_proj_end in content, 'old_proj_end not found'
content = content.replace(old_proj_end, new_proj_end, 1)

# 3. Update PROJECTS dictionary in JS
old_projects_dict = '''var PROJECTS={
  smartpark:{
    num:'01',badge:'Full-Stack · Web App · 2025',title:'SmartPark',
    heroDesc:'A real-time parking management platform handling multi-floor capacity, dynamic pricing algorithms, and automated GST billing — built from scratch with Node.js and Express.',
    coverImage:'smartpark_cover.png',coverBg:'linear-gradient(140deg,#0A1628,#1A2B4A)',coverIcon:'🅿️',
    meta:[{k:'Type',v:'Full-Stack Web App'},{k:'Year',v:'2025'},{k:'Stack',v:'Node.js + SQLite'},{k:'Status',v:'Completed'}],
    metrics:[{n:'3',l:'Floors Managed'},{n:'<1s',l:'API Response'},{n:'0',l:'External DBs'},{n:'100%',l:'Real-Time'}],
    sections:[
      {id:'problem',label:'The Problem',title:'What Needed Solving',content:'<p class="cs2-prose">Parking lots with multiple floors face a persistent challenge: no live visibility into capacity, pricing inconsistencies, and paper-based billing that slows everything down. Attendants work blind. Revenue leaks. Drivers wait.</p>'},
      {id:'solution',label:'The Solution',title:'How It Was Built',content:'<p class="cs2-prose">SmartPark solves all three in a single unified system: real-time slot tracking, algorithmic dynamic pricing, and one-click GST billing that any attendant can use from a browser — <strong>zero training required</strong>.</p>'},
      {id:'arch',label:'Architecture',title:'System Design',content:'<p class="cs2-prose">Node.js + Express REST API sits in front of a SQLite embedded database. A configurable pricing engine applies floor-level rate overrides and time-of-day multipliers automatically — peak hours trigger higher rates, off-peak falls back to base tariffs. Every checkout auto-generates a GST-itemized receipt.</p>',arch:{nodes:[{i:'🌐',l:'Browser',s:'Vanilla JS'},{i:'⚡',l:'Express API',s:'REST'},{i:'🗄️',l:'SQLite',s:'Embedded DB',hl:true},{i:'💸',l:'Pricing Engine',s:'Dynamic rates'},{i:'🧾',l:'GST Billing',s:'Auto-generated'}]}},
      {id:'features',label:'Features',title:'8 Core Capabilities',features:[{i:'⚡',t:'Real-Time Slot Tracking',d:'Live capacity across all 3 floors with instant updates on entry/exit.'},{i:'💸',t:'Dynamic Pricing Engine',d:'Configurable rate tables per floor with time-of-day multipliers.'},{i:'🧾',t:'One-Click GST Billing',d:'Auto-generated itemized receipts with full GST breakdown.'},{i:'📊',t:'Analytics Dashboard',d:'Chart.js visualizations showing occupancy trends and revenue.'},{i:'🔒',t:'Role-Based Access',d:'Separate attendant and admin views with controlled configuration.'},{i:'🗄️',t:'Embedded SQLite',d:'Lightweight local database with zero cloud dependencies.'},{i:'🔄',t:'Multi-Floor Coordination',d:'Centralized state prevents double-bookings across all floors.'},{i:'📱',t:'Responsive Interface',d:'Works cleanly on tablet or desktop for parking booth environments.'}]},
      {id:'quote',label:'',title:'',quote:{t:'The hardest part wasn\\'t the code — it was designing a 60-second workflow that felt effortless for someone standing at a parking gate.',a:'Allan Paulraj on SmartPark'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'Backend',tags:['Node.js','Express.js','SQLite','REST API']},{label:'Frontend',tags:['JavaScript ES6+','Chart.js','HTML/CSS']},{label:'Architecture',tags:['MVC Pattern','Role-Based Auth','Dynamic Config']}]},
      {id:'results',label:'Results',title:'What Was Achieved',results:[{n:'3',l:'Floor Levels',d:'Real-time tracking.'},{n:'<1s',l:'Response Time',d:'Sub-second APIs.'},{n:'0',l:'External Deps',d:'Fully embedded.'},{n:'100%',l:'Uptime Target',d:'Built for ops.'}]},
    ],
    github:'https://github.com/allanborder',live:null,nextKey:'neuroai'
  },
  neuroai:{
    num:'02',badge:'Computer Vision · AI/ML · 2025',title:'NeuroAI',
    heroDesc:'An AI-powered medical imaging platform classifying brain MRI scans into four tumor categories using EfficientNetB0, then generating natural-language diagnostic reports via a local Mistral LLM.',
    coverImage:'neuroai_cover.png',coverBg:'linear-gradient(140deg,#1A1A2E,#2D2D4A)',coverIcon:'🧠',
    meta:[{k:'Type',v:'Medical AI System'},{k:'Year',v:'2025'},{k:'Stack',v:'TensorFlow + FastAPI'},{k:'Privacy',v:'100% Local'}],
    metrics:[{n:'97%+',l:'Accuracy'},{n:'4',l:'Tumor Classes'},{n:'0',l:'Data Sent Out'},{n:'<3s',l:'Scan to Report'}],
    sections:[
      {id:'problem',label:'The Problem',title:'What Needed Solving',content:'<p class="cs2-prose">Brain tumor classification from MRI scans is slow and specialist-gated. Clinicians often wait days for a preliminary read — a problem that compounds in under-resourced hospitals where a radiologist may not be immediately available.</p>'},
      {id:'solution',label:'The Solution',title:'How It Was Built',content:'<p class="cs2-prose">NeuroAI accelerates initial triage — instantly classifying a scan as <strong>Glioma, Meningioma, Pituitary, or No Tumor</strong>, then generating a readable diagnostic summary using Mistral 7B running entirely on-device. No cloud. No patient data leaves the machine.</p>'},
      {id:'arch',label:'Architecture',title:'System Design',content:'<p class="cs2-prose">React frontend passes MRI images to a FastAPI async Python backend. The EfficientNetB0 inference pipeline classifies the scan, then the result is handed to an Ollama-hosted Mistral 7B for natural language report generation. The entire chain runs locally.</p>',arch:{nodes:[{i:'⚛️',l:'React UI',s:'Upload + Display'},{i:'⚡',l:'FastAPI',s:'Async Python'},{i:'🔬',l:'EfficientNetB0',s:'Classification',hl:true},{i:'🤖',l:'Mistral 7B',s:'LLM Report',hl:true}]}},
      {id:'features',label:'Features',title:'8 Core Capabilities',features:[{i:'🔬',t:'EfficientNetB0 Backbone',d:'Fine-tuned on augmented MRI datasets achieving >97% accuracy across all four types.'},{i:'🤖',t:'Mistral LLM Reports',d:'Local Ollama generates human-readable diagnostic summaries from classification outputs.'},{i:'⚡',t:'FastAPI Async Backend',d:'High-performance async Python handles upload, preprocessing, and inference without blocking.'},{i:'⚛️',t:'React Frontend',d:'Drag-and-drop MRI upload with real-time results and downloadable report display.'},{i:'🔒',t:'100% Local Inference',d:'Both CV model and LLM run on-device — no patient data ever leaves the machine.'},{i:'📁',t:'Multi-Format Support',d:'Accepts DICOM, PNG, and JPG MRI inputs with automatic preprocessing.'},{i:'📊',t:'Confidence Scores',d:'Returns per-class probability scores alongside the top prediction.'},{i:'🔄',t:'Batch Processing',d:'Queue multiple scans for sequential inference in a single session.'}]},
      {id:'quote',label:'',title:'',quote:{t:'Combining a fine-tuned CNN with a local LLM taught me that real intelligence isn\\'t in either model alone — it\\'s in the handoff between them.',a:'Allan Paulraj on NeuroAI'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'AI / ML',tags:['TensorFlow','EfficientNetB0','Ollama','Mistral 7B','NumPy','OpenCV']},{label:'Backend',tags:['Python','FastAPI','REST API']},{label:'Frontend',tags:['React','Recharts','Tailwind CSS']}]},
      {id:'results',label:'Results',title:'What Was Achieved',results:[{n:'97%+',l:'Accuracy',d:'All 4 classes.'},{n:'4',l:'Tumor Classes',d:'Full coverage.'},{n:'0',l:'Data Sent',d:'Full privacy.'},{n:'<3s',l:'End-to-End',d:'Scan to report.'}]},
    ],
    github:'https://github.com/allanborder',live:null,nextKey:'bodybp'
  },
  bodybp:{
    num:'03',badge:'React · Live · Vercel · 2025',title:'BodyBlueprint Pro',
    heroDesc:'A personal fitness performance tracker built in React — featuring timeline data visualization, personal record logging per exercise, AI coaching via Llama 3.3 70B, and a responsive UI deployed live on Vercel.',
    coverImage:'bodybp_cover.png',coverBg:'linear-gradient(140deg,#1C2A1A,#2A3D28)',coverIcon:'💪',
    meta:[{k:'Type',v:'React Web App'},{k:'Status',v:'Live on Vercel'},{k:'AI',v:'Llama 3.3 70B'},{k:'Privacy',v:'100% Client-Side'}],
    metrics:[{n:'Live',l:'Deployed'},{n:'14+',l:'Body Metrics'},{n:'~0ms',l:'Server Latency'},{n:'100%',l:'Privacy'}],
    sections:[
      {id:'problem',label:'The Problem',title:'What Needed Solving',content:'<p class="cs2-prose">Tracking gym performance over time is frustrating — spreadsheets are tedious, apps are overkill or locked behind subscriptions. There was no fast, private, zero-signup tracker that actually showed your progress visually.</p>'},
      {id:'solution',label:'The Solution',title:'How It Was Built',content:'<p class="cs2-prose">A focused, fast, privacy-first tracker: log exercises, weights, and reps — watch your progress charted over time with <strong>automatic PR detection</strong> and an AI coach powered by Groq API. No account. No server. Instant load.</p>'},
      {id:'arch',label:'Architecture',title:'System Design',content:'<p class="cs2-prose">Vite + React SPA with Recharts for visualization and LocalStorage for all persistence. Node.js proxy for Groq API calls. Deployed to Vercel CDN — no backend infrastructure costs, sub-second load times anywhere in the world.</p>',arch:{nodes:[{i:'⚛️',l:'React + Vite',s:'SPA'},{i:'📊',l:'Recharts',s:'Data viz'},{i:'🤖',l:'Groq API',s:'Llama 3.3 70B',hl:true},{i:'🚀',l:'Vercel CDN',s:'Global deploy'}]}},
      {id:'features',label:'Features',title:'8 Core Capabilities',features:[{i:'📈',t:'Timeline Visualization',d:'Recharts line graphs showing weight progression across all logged sessions.'},{i:'🏆',t:'Auto PR Detection',d:'Automatically detects and highlights new personal records on every log.'},{i:'🤖',t:'AI Fitness Coach',d:'Groq-powered Llama 3.3 70B provides personalised workout and nutrition advice.'},{i:'📏',t:'14+ Body Measurements',d:'Track chest, arms, waist, legs, and more with dedicated measurement logging.'},{i:'📱',t:'Fully Responsive',d:'Optimized for mobile (gym use) and desktop (home review) layouts.'},{i:'⚡',t:'Instant Load on Vercel',d:'CDN-deployed SPA loads in under a second on any connection.'},{i:'🔒',t:'LocalStorage Persistence',d:'All data lives in your browser — zero backend, zero account, zero privacy concerns.'},{i:'🎨',t:'Clean Dark Interface',d:'Gym-appropriate dark UI with high contrast — readable under any lighting.'}]},
      {id:'quote',label:'',title:'',quote:{t:'The goal was the app I wished existed: no accounts, no ads, no distractions — just your data, your progress, your results.',a:'Allan Paulraj on BodyBlueprint Pro'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'Frontend',tags:['React','Vite','Tailwind CSS','Recharts']},{label:'AI',tags:['Groq API','Llama 3.3 70B','Node.js Proxy']},{label:'Deployment',tags:['Vercel','CDN','LocalStorage API']}]},
      {id:'results',label:'Results',title:'What Was Achieved',results:[{n:'Live',l:'On Vercel',d:'Publicly accessible.'},{n:'14+',l:'Body Metrics',d:'Full tracking.'},{n:'~0ms',l:'Server Latency',d:'Client-side only.'},{n:'100%',l:'Privacy',d:'No tracking.'}]},
    ],
    github:'https://github.com/allanborder/body-blueprint-2',live:'https://body-blueprint-2.vercel.app/',nextKey:'indpophub'
  },
  indpophub:{
    num:'04',badge:'Data Analytics · Dashboard · 2025',title:'IndPopHub',
    heroDesc:'India Population Intelligence — a client-side SPA that transforms 1.4 billion data points into an interactive analytics platform with choropleth maps, statistical charts, and real-time demographic counters.',
    coverImage:'indpophub_cover.png',coverBg:'linear-gradient(140deg,#0D1B2A,#1B3A5C)',coverIcon:'🇮🇳',
    meta:[{k:'Type',v:'Analytics Dashboard'},{k:'Year',v:'2025'},{k:'Stack',v:'Vanilla JS + Chart.js'},{k:'Live',v:'indpophub-dashboard.vercel.app'}],
    metrics:[{n:'36',l:'States & UTs'},{n:'12+',l:'Chart Types'},{n:'0',l:'Server Deps'},{n:'Live',l:'On Vercel'}],
    sections:[
      {id:'problem',label:'The Problem',title:'What Needed Solving',content:'<p class="cs2-prose">Analyzing a population of over 1.4 billion people is a massive cognitive and computational challenge. India\\'s demographic datasets are locked in dense spreadsheets and government reports — obscuring regional nuances, distribution anomalies, and real-time growth trajectories.</p><p class="cs2-prose" style="margin-top:18px;">Extracting meaningful, multi-dimensional insights — like how urbanization correlates with sex ratios across 36 distinct States and Union Territories — requires <strong>tedious manual querying</strong> with zero visual feedback.</p>'},
      {id:'solution',label:'The Solution',title:'How It Was Built',content:'<p class="cs2-prose">IndPopHub bridges complex data and human comprehension: a real-time visual analytics dashboard that transforms static demographic records into a <strong>living, explorable intelligence platform</strong>.</p><p class="cs2-prose" style="margin-top:18px;">Instead of forcing users to query databases, the dashboard pre-computes and visualizes critical statistical relationships instantly — letting users discover insights, identify outliers, and forecast trends without writing a single line of code.</p>'},
      {id:'arch',label:'Architecture',title:'Client-Side SPA Design',content:'<p class="cs2-prose">Engineered as a highly optimized, zero-server Single-Page Application. Everything runs natively in the browser — maximizing portability and eliminating server overhead entirely.</p>',arch:{nodes:[{i:'📊',l:'Chart.js v4',s:'Canvas rendering'},{i:'🗺️',l:'Custom SVG Map',s:'India choropleth',hl:true},{i:'⚡',l:'Stats Engine',s:'Built from scratch',hl:true},{i:'🔄',l:'State Manager',s:'Client-side'},{i:'📁',l:'CSV Parser',s:'Local processing'}]}},
      {id:'features',label:'Features',title:'12 Analytical Views',features:[{i:'🗺️',t:'Interactive Choropleth Map',d:'Custom SVG map of India that recolors dynamically by Density, Population, Sex Ratio, or Urban %. Clicking a state opens a detailed demographic panel.'},{i:'⏱️',t:'Algorithmic Live Counters',d:'Real-time projection engine calibrated to UN growth methodologies — simulates live births, deaths, and net population growth down to the second.'},{i:'📊',t:'Pareto Analysis',d:'Visualizes the 80/20 rule of population concentration across all states and territories.'},{i:'📦',t:'Box Plots & Histograms',d:'Reveals quartiles, IQR, and regional outliers across all demographic metrics.'},{i:'🔥',t:'Pearson Correlation Heatmaps',d:'Computes and visualizes statistical correlation coefficients between all demographic variables in real-time.'},{i:'📤',t:'CSV Upload & Export',d:'Users securely upload their own .csv files to override dashboard data entirely — parsed and rendered locally.'},{i:'🧮',t:'Statistical Engine',d:'Built from scratch: calculates means, standard deviations, medians, skewness, and Pearson coefficients across thousands of data points locally.'},{i:'♻️',t:'Custom Viz-Panel Lifecycle',d:'Dynamic chart instance management — systematically destroys old canvas contexts and mounts new ones, preventing memory leaks.'}]},
      {id:'quote',label:'',title:'',quote:{t:'Every chart on this dashboard exists because I built the statistical engine behind it from scratch — no libraries, no shortcuts.',a:'Allan Paulraj on IndPopHub'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'Frontend',tags:['HTML5','CSS3','Vanilla JavaScript ES6+']},{label:'Data Visualization',tags:['Chart.js v4.4.1','Custom SVG Choropleth','Canvas 2D API']},{label:'Statistics',tags:['Pearson Correlation','Box Plots','Pareto Analysis','Standard Deviation','Skewness']}]},
      {id:'results',label:'Results',title:'What Was Achieved',results:[{n:'36',l:'States & UTs',d:'Full coverage.'},{n:'12+',l:'Chart Types',d:'Statistical views.'},{n:'0',l:'Server Deps',d:'Fully client-side.'},{n:'Live',l:'On Vercel',d:'Publicly accessible.'}]},
    ],
    github:'https://github.com/allanborder',live:'https://indpophub-dashboard.vercel.app/',nextKey:'smartpark'
  }
};'''

new_projects_dict = '''var PROJECTS={
  smartpark:{
    num:'01',badge:'Full-Stack · Web App · 2025',title:'SmartPark',
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
    num:'02',badge:'Computer Vision · AI/ML · 2025',title:'NeuroAI',
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
    num:'03',badge:'React · Live · Vercel · 2025',title:'BodyBlueprint Pro',
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
    github:'https://github.com/allanborder/body-blueprint-2',live:'https://body-blueprint-2.vercel.app/',nextKey:'indpophub'
  },
  indpophub:{
    num:'04',badge:'Data Analytics · Dashboard · 2025',title:'IndPopHub',
    heroDesc:'India Population Intelligence — a client-side SPA that transforms 1.4 billion data points into an interactive analytics platform with choropleth maps, statistical charts, and real-time demographic counters.',
    coverImage:'indpophub_cover.png',coverBg:'linear-gradient(140deg,#0D1B2A,#1B3A5C)',coverIcon:'🇮🇳',
    meta:[{k:'Type',v:'Analytics Dashboard'},{k:'Year',v:'2025'},{k:'Stack',v:'Vanilla JS + Chart.js'},{k:'Live',v:'indpophub-dashboard.vercel.app'}],
    metrics:[{n:'36',l:'States & UTs'},{n:'12+',l:'Chart Types'},{n:'0',l:'Server Deps'},{n:'Live',l:'On Vercel'}],
    sections:[
      {id:'problem',label:'The Problem',title:'What Needed Solving',content:'<p class="cs2-prose">Analyzing a population of over 1.4 billion people is a massive cognitive and computational challenge. India\\'s demographic datasets are locked in dense spreadsheets and government reports — obscuring regional nuances, distribution anomalies, and real-time growth trajectories.</p>'},
      {id:'solution',label:'The Solution',title:'How It Was Built',content:'<p class="cs2-prose">IndPopHub bridges complex data and human comprehension: a real-time visual analytics dashboard that transforms static demographic records into a <strong>living, explorable intelligence platform</strong>.</p>'},
      {id:'arch',label:'Architecture',title:'System Flow',content:'<p class="cs2-prose">High performance client architecture: parses statistical matrices and calculates demographic correlations on-the-fly, rendering interactive vector choropleths and canvas charts smoothly.</p>',arch:{nodes:[{i:'👤',l:'Data Analyst',s:'User'},{i:'🗺️',l:'Interactive Choropleth',s:'SVG Map UI'},{i:'⚡',l:'Statistical Engine',s:'Pearson Correlation',hl:true},{i:'📊',l:'Chart.js Engine',s:'12 Chart Views'},{i:'📁',l:'Local CSV Parser',s:'Zero Server'}]}},
      {id:'features',label:'Features',title:'Core Capabilities',features:[{i:'🗺️',t:'Interactive Choropleth Map',d:'Custom SVG map of India that recolors dynamically by Density, Population, Sex Ratio, or Urban %. Clicking a state opens a detailed demographic panel.'},{i:'⏱️',t:'Algorithmic Live Counters',d:'Real-time projection engine calibrated to UN growth methodologies — simulates live births, deaths, and net population growth down to the second.'},{i:'📊',t:'Pareto Analysis',d:'Visualizes the 80/20 rule of population concentration across all states and territories.'},{i:'📦',t:'Box Plots & Histograms',d:'Reveals quartiles, IQR, and regional outliers across all demographic metrics.'},{i:'🔥',t:'Pearson Correlation Heatmaps',d:'Computes and visualizes statistical correlation coefficients between all demographic variables in real-time.'},{i:'📤',t:'CSV Upload & Export',d:'Users securely upload their own .csv files to override dashboard data entirely — parsed and rendered locally.'},{i:'🧮',t:'Statistical Engine',d:'Calculates means, standard deviations, medians, skewness, and Pearson coefficients across thousands of data points locally.'},{i:'♻️',t:'Dynamic Viz Lifecycle',d:'Systematically cleans old canvas instances to prevent browser memory leaks.'}]},
      {id:'quote',label:'',title:'',quote:{t:'Every chart on this dashboard exists because I built the statistical algorithms behind it from scratch.',a:'Allan Paulraj on IndPopHub'}},
      {id:'stack',label:'Tech Stack',title:'Built With',techGroups:[{label:'Frontend',tags:['HTML5','CSS3','Vanilla JavaScript ES6+']},{label:'Data Visualization',tags:['Chart.js v4.4.1','Custom SVG Choropleth','Canvas 2D API']},{label:'Statistics',tags:['Pearson Correlation','Box Plots','Pareto Analysis','Standard Deviation','Skewness']}]},
      {id:'results',label:'Results',title:'What Was Achieved',results:[{n:'36',l:'States & UTs',d:'Full coverage.'},{n:'12+',l:'Chart Types',d:'Statistical views.'},{n:'0',l:'Server Deps',d:'Fully client-side.'},{n:'Live',l:'On Vercel',d:'Publicly accessible.'}]},
    ],
    github:'https://github.com/allanborder',live:'https://indpophub-dashboard.vercel.app/',nextKey:'nexora'
  },
  nexora:{
    num:'05',badge:'Hackathon · AI Pipeline · 2025',title:'Nexora AI System',
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
    github:'https://github.com/allanborder',live:null,nextKey:'smartpark'
  }
};'''

assert old_projects_dict in content, 'old_projects_dict not found'
content = content.replace(old_projects_dict, new_projects_dict, 1)

# 4. Remove the large screenshot / what it looks like area if any residual styles or sections exist
# Ensure terminal commands list nexora as well
old_term_projects = "['<span class=\"t-o\">1. <span class=\"t-v\">SmartPark</span>         — Multi-floor parking (Node + SQLite)</span>','<span class=\"t-o\">2. <span class=\"t-v\">NeuroAI</span>           — Brain MRI classification (EfficientNetB0)</span>','<span class=\"t-o\">3. <span class=\"t-v\">BodyBlueprint Pro</span> — Fitness tracker (React + Vercel)</span>','<span class=\"t-o\">4. <span class=\"t-v\">IndPopHub</span>         — India population analytics dashboard</span>'];"
new_term_projects = "['<span class=\"t-o\">1. <span class=\"t-v\">SmartPark</span>         — Multi-floor parking (Node + SQLite)</span>','<span class=\"t-o\">2. <span class=\"t-v\">NeuroAI</span>           — Brain MRI classification (EfficientNetB0)</span>','<span class=\"t-o\">3. <span class=\"t-v\">BodyBlueprint Pro</span> — Fitness tracker (React + Vercel)</span>','<span class=\"t-o\">4. <span class=\"t-v\">IndPopHub</span>         — India population analytics dashboard</span>','<span class=\"t-o\">5. <span class=\"t-v\">Nexora AI</span>         — Hackathon prototype pipeline</span>'];"

assert old_term_projects in content, 'old_term_projects not found'
content = content.replace(old_term_projects, new_term_projects, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully integrated Nexora Hackathon, updated project layout, system flows, and project details!')
