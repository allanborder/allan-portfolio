// @ts-check
const { test, expect } = require('@playwright/test');

test.describe('Allan Paulraj Portfolio E2E Test Suite', () => {

  test('Page loads with title and core structure', async ({ page }) => {
    await page.goto('http://localhost:3000/#/home');
    await expect(page).toHaveTitle(/Allan Paulraj/i);

    // Verify navigation links exist
    const navHome = page.locator('#nav-home');
    const navProjects = page.locator('#nav-works');
    const navAbout = page.locator('#nav-about');
    const navContact = page.locator('#nav-contact');

    await expect(navHome).toBeVisible();
    await expect(navProjects).toBeVisible();
    await expect(navAbout).toBeVisible();
    await expect(navContact).toBeVisible();
  });

  test('Central Routing: Navigate to About section and verify 2D LEGO character shader', async ({ page }) => {
    await page.goto('http://localhost:3000/#/about');

    // Verify About view is displayed
    const viewAbout = page.locator('#view-about');
    await expect(viewAbout).toBeVisible();

    // Verify 2D LEGO stage and canvas are present
    const legoStage = page.locator('#abLegoStage');
    const ditherCanvas = page.locator('#ditherVeilCanvas');
    await expect(legoStage).toBeVisible();
    await expect(ditherCanvas).toBeVisible();

    // Verify canvas has non-zero dimensions
    const box = await ditherCanvas.boundingBox();
    expect(box).not.toBeNull();
    expect(box.width).toBeGreaterThan(50);
    expect(box.height).toBeGreaterThan(50);
  });

  test('React Bits Masonry: Verify 29 gallery frames and filter pills', async ({ page }) => {
    await page.goto('http://localhost:3000/#/about');

    // Scroll to the physique section
    const physiqueSec = page.locator('#ab-sec-physique');
    await physiqueSec.scrollIntoViewIfNeeded();

    // Verify filter pills
    const filterPills = page.locator('#masonryFilterPills');
    await expect(filterPills).toBeVisible();

    // Verify Masonry container
    const masonryList = page.locator('#physiqueMasonry');
    await expect(masonryList).toBeVisible();

    // Verify all 29 frame items are rendered
    const items = masonryList.locator('.item-wrapper');
    await expect(items).toHaveCount(29);

    // Test filtering: click "PHYSIQUE & CONDITIONING"
    const physiqueBtn = page.locator('.masonry-filter-btn[data-filter="physique"]');
    await physiqueBtn.click();
    await expect(physiqueBtn).toHaveClass(/active/);
  });

  test('Contact Form: Verify presence and interactive submission elements', async ({ page }) => {
    await page.goto('http://localhost:3000/#/contact');

    const viewContact = page.locator('#view-contact');
    await expect(viewContact).toBeVisible();

    const nameInput = page.locator('#ctName');
    const emailInput = page.locator('#ctEmail');
    const msgInput = page.locator('#ctMsg');
    const submitBtn = page.locator('#ctSubmitBtn');

    await expect(nameInput).toBeVisible();
    await expect(emailInput).toBeVisible();
    await expect(msgInput).toBeVisible();
    await expect(submitBtn).toBeVisible();
  });

  test('Experience Section: Timeline milestones ordering', async ({ page }) => {
    await page.goto('http://localhost:3000/#/experience');

    const viewExp = page.locator('#view-experience');
    await expect(viewExp).toBeVisible();

    // Check first timeline milestone (2026 Lysa Solutions)
    const firstMilestone = page.locator('.exp-timeline-item').first();
    await expect(firstMilestone).toContainText('LYSA SOLUTIONS');
  });

});
