const { chromium } = require('@playwright/test');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ channel: 'chrome' });
  const viewports = [
    { name: '320x568', width: 320, height: 568 },
    { name: '375x667', width: 375, height: 667 },
    { name: '390x844', width: 390, height: 844 },
    { name: '430x932', width: 430, height: 932 },
    { name: '768x1024', width: 768, height: 1024 },
    { name: '1024x768', width: 1024, height: 768 },
    { name: '1440x900', width: 1440, height: 900 }
  ];
  const routes = [
    '#/home',
    '#/projects',
    '#/experience',
    '#/about',
    '#/contact',
    '#/project/rj',
    '#/project/neuroai',
    '#/project/bodybp',
    '#/project/patchwise'
  ];

  const results = [];
  if (!fs.existsSync('audit_screens')) fs.mkdirSync('audit_screens');

  for (const vp of viewports) {
    const page = await browser.newPage({ viewport: { width: vp.width, height: vp.height } });
    for (const r of routes) {
      await page.goto('http://localhost:3000/' + r, { waitUntil: 'domcontentloaded' });
      await page.waitForTimeout(400);

      const overflowData = await page.evaluate(() => {
        const docW = document.documentElement.clientWidth;
        const all = document.querySelectorAll('*');
        const overflowing = [];
        for (const el of all) {
          const rect = el.getBoundingClientRect();
          if (rect.right > docW + 2) {
            overflowing.push({
              tag: el.tagName,
              id: el.id || '',
              cls: typeof el.className === 'string' ? el.className.slice(0, 50) : '',
              right: Math.round(rect.right),
              docW: docW
            });
          }
        }
        return {
          scrollWidth: document.documentElement.scrollWidth,
          clientWidth: docW,
          hasDocOverflow: document.documentElement.scrollWidth > docW,
          overflowCount: overflowing.length,
          topElements: overflowing.slice(0, 5)
        };
      });

      const cleanRoute = r.replace(/[^a-zA-Z0-9]/g, '_');
      const filename = `audit_screens/${vp.name}_${cleanRoute}.png`;
      if (['320x568', '390x844', '768x1024', '1440x900'].includes(vp.name) && ['#/home', '#/about', '#/experience', '#/contact', '#/project/patchwise'].includes(r)) {
        await page.screenshot({ path: filename, fullPage: false });
      }

      results.push({ vp: vp.name, route: r, overflow: overflowData });
    }
    await page.close();
  }

  await browser.close();
  fs.writeFileSync('audit_screens/audit_results.json', JSON.stringify(results, null, 2));
  console.log('Mobile audit visual pass complete. Evaluated ' + results.length + ' configurations.');
})();
