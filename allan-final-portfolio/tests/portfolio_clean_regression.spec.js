const { test, expect } = require('@playwright/test');

test.describe('Allan Paulraj Portfolio Clean-State Regression Suite', () => {

  test('1. Core Layout, Accessibility Skip Link, and Zero Console/Network Errors', async ({ page }) => {
    const consoleErrors = [];
    const networkFailures = [];

    page.on('console', msg => {
      if (msg.type() === 'error') consoleErrors.push(msg.text());
    });
    page.on('pageerror', err => consoleErrors.push(err.toString()));
    page.on('response', res => {
      if (res.status() >= 400) networkFailures.push({ url: res.url(), status: res.status() });
    });

    await page.goto('http://localhost:3000/#/home', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(500);

    // Title and branding
    const title = await page.title();
    expect(title).toContain('Allan Paulraj');

    // Accessibility skip link
    const skipLink = page.locator('.skip-link');
    await expect(skipLink).toBeAttached();
    expect(await skipLink.getAttribute('href')).toBe('#main');

    // Profile photo alt attribute in DOM
    const profileAlt = await page.evaluate(() => {
      const img = document.querySelector('img[src*="profile-photo-4.jpg"]');
      return img ? img.getAttribute('alt') : null;
    });
    expect(profileAlt).toBeTruthy();

    expect(consoleErrors).toHaveLength(0);
    expect(networkFailures).toHaveLength(0);
  });

  test('2. Central Routing: All 5 Views Transition Cleanly', async ({ page }) => {
    await page.goto('http://localhost:3000/#/home', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(400);

    const routes = [
      { hash: '#/projects', selector: '#view-listing' },
      { hash: '#/experience', selector: '#view-experience' },
      { hash: '#/about', selector: '#view-about' },
      { hash: '#/contact', selector: '#view-contact' },
      { hash: '#/home', selector: '#view-main' }
    ];

    for (const r of routes) {
      await page.evaluate((targetHash) => { window.location.hash = targetHash; }, r.hash);
      await page.waitForTimeout(700);
      const isVisible = await page.evaluate((sel) => {
        const el = document.querySelector(sel);
        return el ? (el.style.display !== 'none' && el.offsetHeight > 0) : false;
      }, r.selector);
      expect(isVisible).toBe(true);
    }
  });

  test('3. Experience Section: Timeline, Reset on Re-Click, and 4 Approved Projects', async ({ page }) => {
    await page.goto('http://localhost:3000/#/experience', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(600);

    const expText = await page.locator('#view-experience').innerText();

    // Verification of entities
    expect(expText).toMatch(/fuzionest/i);
    expect(expText).toMatch(/oasis/i);
    expect(expText).not.toMatch(/\bQASIS\b/);

    // Selected Work verification
    expect(expText).toMatch(/NeuroAI/i);
    expect(expText).toMatch(/Body Blueprint Pro/i);
    expect(expText).toMatch(/RJ/i);
    expect(expText).toMatch(/PatchWise/i);
    expect(expText).not.toMatch(/SmartPark/i);
    expect(expText).not.toMatch(/Personal Portfolio/i);

    // Re-clicking Experience resets scroll to top
    await page.evaluate(() => window.scrollTo(0, 600));
    await page.waitForTimeout(200);
    await page.click('#nav-experience');
    await page.waitForTimeout(400);
    const scrollY = await page.evaluate(() => window.scrollY);
    expect(scrollY).toBe(0);

    // Verify all 4 VIEW PROJECT buttons in Experience
    const viewButtons = page.locator('#view-experience .flip-card-action');
    await expect(viewButtons).toHaveCount(4);
    const hrefs = await viewButtons.evaluateAll(btns => btns.map(b => b.getAttribute('href')));
    expect(hrefs).toEqual([
      '#/project/neuroai',
      '#/project/bodybp',
      '#/project/rj',
      '#/project/patchwise'
    ]);
  });

  test('4. Canonical Project Case Studies and Loop Navigation', async ({ page }) => {
    await page.goto('http://localhost:3000/#/projects', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(500);

    // Check Projects listing has exactly 4 project rows
    const projectRows = page.locator('.projects-text-list .project-list-row');
    await expect(projectRows).toHaveCount(4);

    const projectKeys = ['rj', 'neuroai', 'bodybp', 'patchwise'];
    for (const key of projectKeys) {
      await page.evaluate((k) => { window.location.hash = '#/project/' + k; }, key);
      await expect(page.locator('#view-case')).toBeVisible({ timeout: 5000 });
    }

    // Projects -> PatchWise navigation
    await page.evaluate(() => { window.location.hash = '#/projects'; });
    await expect(page.locator('#view-listing')).toBeVisible();
    await page.waitForTimeout(600);
    const patchwiseLink = page.locator('a[data-project="patchwise"]');
    await patchwiseLink.scrollIntoViewIfNeeded();
    await patchwiseLink.click();
    await expect(page.locator('#view-case')).toBeVisible({ timeout: 5000 });
    await page.waitForTimeout(500);
    const patchwiseTitle = await page.locator('#csTitle').innerText();
    expect(patchwiseTitle.toUpperCase()).toContain('PATCHWISE');
  });

  test('5. About Section: 29-Frame Masonry Gallery & 2D LEGO Shader', async ({ page }) => {
    await page.goto('http://localhost:3000/#/about', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(600);

    // 29 gallery frames
    const frames = page.locator('#physiqueMasonry .item-wrapper');
    await expect(frames).toHaveCount(29);

    // 4 filter buttons
    const filterBtns = page.locator('.masonry-filter-btn');
    await expect(filterBtns).toHaveCount(4);

    // 2D LEGO canvas
    const legoCanvas = page.locator('#ditherVeilCanvas');
    await expect(legoCanvas).toBeAttached();
    const canvasDimensions = await legoCanvas.evaluate(c => ({ w: c.width, h: c.height }));
    expect(canvasDimensions.w).toBeGreaterThan(0);
    expect(canvasDimensions.h).toBeGreaterThan(0);
  });

  test('6. Real Document Verification', async ({ request }) => {
    const documents = [
      'assets/documents/Allan_Resume_2026.pdf',
      'assets/documents/oasis_offer_letter.pdf',
      'assets/documents/fuzionest_internship_certificate.pdf',
      'assets/documents/lysarq_internship_certificate.pdf'
    ];

    for (const doc of documents) {
      const res = await request.get('http://localhost:3000/' + doc);
      expect(res.status()).toBe(200);
    }
  });

  test('7. Responsive Viewport Check (Desktop, Tablet, Mobile)', async ({ page }) => {
    const viewports = [
      { name: 'Desktop', width: 1440, height: 900 },
      { name: 'Tablet', width: 768, height: 1024 },
      { name: 'Mobile', width: 375, height: 812 }
    ];

    for (const vp of viewports) {
      await page.setViewportSize({ width: vp.width, height: vp.height });
      await page.goto('http://localhost:3000/#/home', { waitUntil: 'domcontentloaded' });
      await page.waitForTimeout(400);

      const hasOverflow = await page.evaluate(() => {
        return document.documentElement.scrollWidth > document.documentElement.clientWidth;
      });
      expect(hasOverflow).toBe(false);
    }
  });

});
