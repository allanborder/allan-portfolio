const fs = require('fs');
const path = require('path');

const targetStrings = [
  'lego-allan.glb',
  'lego-allan.jpg',
  'lego-allan-transparent',
  'profile.jpg',
  'profilee.webp',
  'rj_hud',
  'rj_showcase',
  'neuroai_cover',
  'neuroai_dash',
  'bodybp_cover',
  'bodybp_dash',
  'patchwise_dash',
  'smartpark',
  'dermasense',
  'assets/vendor',
  'ogl.umd',
  'ogl.mjs',
  'fluid-glass.js',
  'glass-surface.js',
  'IMG_CARDS',
  'imgMarqueeTrack',
  'assets/gallery/photo_2.jpg',
  'assets/gallery/photo_3.jpg',
  'assets/gallery/photo_7.jpg',
  'Allan_Paulraj_offer_letter.pdf',
  'oasis_internship_certificate.pdf',
  'URK24CS7129-ALLANPAULRAJV.pdf',
  'image_f34022.jpg',
  'image_f346ca.png'
];

function getFiles(dir, list = []) {
  if (!fs.existsSync(dir)) return list;
  fs.readdirSync(dir, { withFileTypes: true }).forEach(e => {
    if (e.name === 'node_modules' || e.name === '.git' || e.name === '.gemini' || e.name === 'playwright-report' || e.name === 'test-results') return;
    const full = path.join(dir, e.name);
    if (e.isDirectory()) getFiles(full, list);
    else if (/\.(html|js|json|css|md)$/i.test(e.name)) {
      // Don't scan the test file itself
      if (!full.includes('regression_audit.js')) list.push(full);
    }
  });
  return list;
}

const files = getFiles('.');
console.log('Scanning files:', files.length);

let totalIssues = 0;
files.forEach(f => {
  const content = fs.readFileSync(f, 'utf8');
  targetStrings.forEach(s => {
    if (content.includes(s)) {
      console.log('[STALE REFERENCE FOUND] "' + s + '" in file: ' + f);
      totalIssues++;
    }
  });
});

console.log('Total stale references found:', totalIssues);
if (totalIssues > 0) {
  process.exit(1);
} else {
  console.log('Codebase is 100% clean of stale references!');
}
