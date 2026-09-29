// @ts-check
const { test, expect } = require('@playwright/test');

test.describe('Custom Galaxy Cursor Validation Suite', () => {

  test('1. Desktop 1440x900: Global Cursor, Hotspot (2 2), and Asset Loading', async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });

    const failedRequests = [];
    page.on('requestfailed', req => failedRequests.push(req.url()));

    await page.goto('http://localhost:3000/#/home', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(500);

    // Verify no failed requests for cursor assets
    expect(failedRequests.filter(url => url.includes('galaxy-cursor'))).toHaveLength(0);

    // 1. Body default cursor
    const bodyCursor = await page.evaluate(() => getComputedStyle(document.body).cursor);
    expect(bodyCursor).toContain('galaxy-cursor');
    expect(bodyCursor).toContain('2 2');

    // 2. Interactive elements (nav links, buttons) use hover cursor
    const navLink = page.locator('#nav-works');
    await expect(navLink).toBeVisible();
    const navCursor = await navLink.evaluate(el => getComputedStyle(el).cursor);
    expect(navCursor).toContain('galaxy-cursor-hover');
    expect(navCursor).toContain('2 2');

    // 3. Project rows use hover cursor
    const workRow = page.locator('.project-list-row').first();
    if (await workRow.count() > 0) {
      const workCursor = await workRow.evaluate(el => getComputedStyle(el).cursor);
      expect(workCursor).toContain('galaxy-cursor-hover');
    }

    // 4. Input fields retain text cursor
    const emailInput = page.locator('input[type="text"], input[type="email"], textarea').first();
    if (await emailInput.count() > 0) {
      const inputCursor = await emailInput.evaluate(el => getComputedStyle(el).cursor);
      expect(inputCursor).toBe('text');
    }
  });

  test('2. Desktop 1920x1080: Route Navigation & Interactive Elements Clickability', async ({ page }) => {
    await page.setViewportSize({ width: 1920, height: 1080 });
    await page.goto('http://localhost:3000/#/home', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(500);

    // Test clicking navigation tabs with custom cursor active
    const navExperience = page.locator('#nav-experience');
    await expect(navExperience).toBeVisible();
    await navExperience.click();
    await page.waitForTimeout(500);

    // Verify Experience view is active
    const expView = page.locator('#view-experience');
    await expect(expView).toBeVisible();

    // Verify Experience filter buttons have hover cursor
    const filterBtn = page.locator('.exp-filter-btn').first();
    if (await filterBtn.count() > 0) {
      const filterCursor = await filterBtn.evaluate(el => getComputedStyle(el).cursor);
      expect(filterCursor).toContain('galaxy-cursor-hover');
    }

    // Return to Projects
    const navProjects = page.locator('#nav-works');
    await navProjects.click();
    await page.waitForTimeout(500);
    await expect(page.locator('#view-listing')).toBeVisible();
  });

  test('3. High-DPI Context (deviceScaleFactor: 2): Resolves @2x Asset', async ({ browser }) => {
    const context = await browser.newContext({
      viewport: { width: 1440, height: 900 },
      deviceScaleFactor: 2,
    });
    const page = await context.newPage();

    let fetched2x = false;
    page.on('response', res => {
      if (res.url().includes('galaxy-cursor@2x.png') && res.status() === 200) {
        fetched2x = true;
      }
    });

    await page.goto('http://localhost:3000/#/home', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(500);

    const bodyCursor = await page.evaluate(() => getComputedStyle(document.body).cursor);
    expect(bodyCursor).toContain('galaxy-cursor');
    expect(fetched2x).toBe(true);

    await context.close();
  });

  test('4. Keyboard Accessibility: Tab Focus and Selection Unimpeded', async ({ page }) => {
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.goto('http://localhost:3000/#/home', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(500);

    // Press Tab multiple times to verify keyboard accessibility
    await page.keyboard.press('Tab');
    const focusedTag = await page.evaluate(() => document.activeElement ? document.activeElement.tagName : null);
    expect(focusedTag).not.toBeNull();

    // Verify user-select is NOT disabled globally
    const userSelect = await page.evaluate(() => getComputedStyle(document.body).userSelect);
    expect(userSelect).not.toBe('none');
  });

  test('5. Mobile Viewport Check (320x568, 390x844, 768x1024): No Custom Cursor on Touch', async ({ browser }) => {
    const viewports = [
      { name: 'iPhone SE', width: 320, height: 568 },
      { name: 'iPhone 14', width: 390, height: 844 },
      { name: 'iPad Portrait', width: 768, height: 1024 },
    ];

    for (const vp of viewports) {
      const context = await browser.newContext({
        viewport: { width: vp.width, height: vp.height },
        hasTouch: true,
        isMobile: true,
      });
      const page = await context.newPage();
      await page.goto('http://localhost:3000/#/home', { waitUntil: 'domcontentloaded' });
      await page.waitForTimeout(400);

      // Verify custom cursor is NOT active on touch devices
      const bodyCursor = await page.evaluate(() => getComputedStyle(document.body).cursor);
      expect(bodyCursor).not.toContain('galaxy-cursor');

      await context.close();
    }
  });

});
