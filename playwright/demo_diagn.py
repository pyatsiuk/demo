from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        storage_state="/Users/app55/Projects/awery/playwright/.auth/storage_state.json"
    )

    page = context.new_page()

    page.goto("https://demo.awery.com.ua/apps/dev/")

    print("Current URL:", page.url)

    # page.wait_for_load_state("networkidle")

    # чекати поки з'явиться меню
    # expect(page.get_by_text("All Companies")).to_be_visible(timeout=15000)

    # menu = page.get_by_text("Office Enquiries")

    # expect(menu).to_be_visible(timeout=15000)

    # menu.click()

    page.pause()