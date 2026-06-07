#!/usr/bin/env python3
"""
fix_smartpark_arch.py
Replaces the custom SmartPark architecture diagram with the standard
node-flow style, and removes the smartpark_pricing.png screenshot slot.
Run: python3 fix_smartpark_arch.py
"""
import shutil, sys, os, re

SRC = 'index.html'
BAK = 'index.html.bak2'

if not os.path.exists(SRC):
    print(f"ERROR: {SRC} not found.")
    sys.exit(1)

shutil.copy2(SRC, BAK)
print(f"Backed up → {BAK}")

with open(SRC, 'r', encoding='utf-8') as f:
    html = f.read()

# ── 1. Replace buildSmartParkArch() with standard node-flow ──────────────────
OLD_ARCH_FN = '''function buildSmartParkArch() {
  return '<div class="cs-arch-diagram">' +
    '<div class="cs-arch-header">' +
      '<div class="cs-arch-header-dot" style="background:#ff5f56;"></div>' +
      '<div class="cs-arch-header-dot" style="background:#ffbd2e;"></div>' +
      '<div class="cs-arch-header-dot" style="background:#27c93f;"></div>' +
      '<span class="cs-arch-header-title">SmartPark · System Architecture</span>' +
    '</div>' +
    '<div class="cs-arch-body">' +
      '<div class="cs-arch-flow">' +
        '<div class="cs-arch-node"><div class="cs-arch-node-icon">🌐</div><div class="cs-arch-node-label">Browser<br>Frontend</div><div class="cs-arch-node-sub">Vanilla JS · Chart.js</div></div>' +
        '<div class="cs-arch-arrow">→</div>' +
        '<div class="cs-arch-node highlight"><div class="cs-arch-node-icon">⚡</div><div class="cs-arch-node-label">Express.js<br>REST API</div><div class="cs-arch-node-sub">Node.js · MVC</div></div>' +
        '<div class="cs-arch-arrow">→</div>' +
        '<div class="cs-arch-node"><div class="cs-arch-node-icon">🗄️</div><div class="cs-arch-node-label">SQLite<br>Database</div><div class="cs-arch-node-sub">Embedded · Local</div></div>' +
        '<div class="cs-arch-arrow">→</div>' +
        '<div class="cs-arch-node"><div class="cs-arch-node-icon">💸</div><div class="cs-arch-node-label">Pricing<br>Engine</div><div class="cs-arch-node-sub">Peak · Off-Peak</div></div>' +
        '<div class="cs-arch-arrow">→</div>' +
        '<div class="cs-arch-node"><div class="cs-arch-node-icon">🧾</div><div class="cs-arch-node-label">GST Billing<br>Generator</div><div class="cs-arch-node-sub">18% GST · PDF</div></div>' +
        '<div class="cs-arch-arrow">→</div>' +
        '<div class="cs-arch-node"><div class="cs-arch-node-icon">📊</div><div class="cs-arch-node-label">Analytics<br>Charts</div><div class="cs-arch-node-sub">Chart.js · CSV</div></div>' +
      '</div>' +
      '<div class="cs-arch-screenshots">' +
        '<div class="cs-arch-screenshot"><img src="smartpark_dashboard_shot.png" alt="Dashboard" onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\';"><div style="display:none;min-height:160px;background:linear-gradient(140deg,#0A1628,#1A2B4A);align-items:center;justify-content:center;flex-direction:column;gap:8px;"><span style="font-size:2rem;">🅿️</span><span style="font-size:.7rem;color:rgba(255,255,255,.5);font-family:var(--mono);letter-spacing:2px;text-transform:uppercase;">Dashboard</span></div><div class="cs-arch-screenshot-label">Live Dashboard</div></div>' +
        '<div class="cs-arch-screenshot"><img src="smartpark_receipt_shot.png" alt="Receipt" onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\';"><div style="display:none;min-height:160px;background:linear-gradient(140deg,#1A2B4A,#0A1628);align-items:center;justify-content:center;flex-direction:column;gap:8px;"><span style="font-size:2rem;">🧾</span><span style="font-size:.7rem;color:rgba(255,255,255,.5);font-family:var(--mono);letter-spacing:2px;text-transform:uppercase;">GST Receipt</span></div><div class="cs-arch-screenshot-label">GST Receipt</div></div>' +
        '<div class="cs-arch-screenshot"><img src="smartpark_floormap_shot.png" alt="Floor Map" onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\';"><div style="display:none;min-height:160px;background:linear-gradient(140deg,#0D1B2A,#1A3040);align-items:center;justify-content:center;flex-direction:column;gap:8px;"><span style="font-size:2rem;">🗺️</span><span style="font-size:.7rem;color:rgba(255,255,255,.5);font-family:var(--mono);letter-spacing:2px;text-transform:uppercase;">Floor Map</span></div><div class="cs-arch-screenshot-label">Floor Capacity</div></div>' +
        '<div class="cs-arch-screenshot"><img src="smartpark_revenue_shot.png" alt="Revenue" onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\';"><div style="display:none;min-height:160px;background:linear-gradient(140deg,#1A2B4A,#0C2240);align-items:center;justify-content:center;flex-direction:column;gap:8px;"><span style="font-size:2rem;">📈</span><span style="font-size:.7rem;color:rgba(255,255,255,.5);font-family:var(--mono);letter-spacing:2px;text-transform:uppercase;">Revenue</span></div><div class="cs-arch-screenshot-label">Revenue Analytics</div></div>' +
      '</div>' +
    '</div>' +
  '</div>';
}'''

NEW_ARCH_FN = """function buildSmartParkArch() { return ''; }"""

if OLD_ARCH_FN not in html:
    print("WARNING: buildSmartParkArch not found verbatim — trying regex strip")
    html = re.sub(
        r'function buildSmartParkArch\(\)\s*\{.*?^\}',
        "function buildSmartParkArch() { return ''; }",
        html, flags=re.DOTALL | re.MULTILINE
    )
    print("Regex strip applied")
else:
    html = html.replace(OLD_ARCH_FN, NEW_ARCH_FN, 1)
    print("buildSmartParkArch replaced ✓")

# ── 2. Switch smartpark from useCustomArch to standard archNodes ──────────────
OLD_ARCH_FLAG = "  useCustomArch:true,"
NEW_ARCH_FLAG = """  useCustomArch:false,
  archNodes:[{i:'🌐',l:'Browser Frontend'},{i:'→',l:''},{i:'⚡',l:'Express.js REST API'},{i:'→',l:''},{i:'🗄️',l:'SQLite Database'},{i:'→',l:''},{i:'💸',l:'Pricing Engine'},{i:'→',l:''},{i:'🧾',l:'GST Billing'},{i:'→',l:''},{i:'📊',l:'Analytics Charts'}],"""

if OLD_ARCH_FLAG in html:
    html = html.replace(OLD_ARCH_FLAG, NEW_ARCH_FLAG, 1)
    print("useCustomArch flag replaced ✓")
else:
    print("WARNING: useCustomArch:true not found — may already be patched")

# ── 3. Remove smartpark_pricing.png from screenshots array ───────────────────
OLD_SCREENSHOTS = """,{src:'smartpark_pricing.png',label:'Dynamic Pricing Panel',hint:'smartpark_pricing.png'}"""
if OLD_SCREENSHOTS in html:
    html = html.replace(OLD_SCREENSHOTS, '', 1)
    print("smartpark_pricing.png screenshot removed ✓")
else:
    print("WARNING: smartpark_pricing.png entry not found — may already be removed")

# ── 4. Write output ───────────────────────────────────────────────────────────
with open(SRC, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nDone! {SRC} updated ({len(html):,} chars)")