from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    # Add token from venv/playwright/.auth/storage_state.json
    context = browser.new_context(
            storage_state="playwright/.auth/storage_state.json"
        )
    page = context.new_page()  
    page.goto("https://demo.awery.com.ua/apps/dev/")


    # page.get_by_text("Office Enquiries").nth(1).click()
    page.locator("span.menu-item-name", has_text="Office Enquiries").click()

    # expect(page.get_by_role("row", name="ID Ref No. Broker Status")).to_be_visible()
    expect(page.locator("awr-table.ng-star-inserted")).to_be_visible()

    page.pause()
    obc_button = page.locator('awr-button.awr-equal[style="color: rgb(128, 0, 0);"]')
    obc_button.highlight()
    
    obc_button.click()

    # page.locator("awr-button:nth-child(10)").click()
    page.pause()
    
    browser.close()