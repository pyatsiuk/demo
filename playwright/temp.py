from playwright.sync_api import sync_playwright, expect


def run(playwright):
    browser = playwright.chromium.launch(headless=False)

    # Add token from venv/playwright/.auth/storage_state.json
    context = browser.new_context(
        storage_state="playwright/.auth/storage_state.json"
    )
    page = context.new_page()
    page.goto("https://demo.awery.com.ua/apps/dev/")

    page.locator("span.menu-item-name", has_text="Office Enquiries").click()

    expect(page.locator("awr-table.ng-star-inserted")).to_be_visible()

    page.pause()

    # click Create OBC
    obc_button = page.locator("awr-button:nth-child(10)")
    obc_button.click()

    expect(page.locator("div.summary")).to_be_visible()

    # Видалити всі можливі overlay елементи
    page.evaluate("""
    () => {
        document.querySelectorAll('*').forEach(el => {
            const style = window.getComputedStyle(el);
            if ((style.position === 'fixed' || style.position === 'absolute') && 
                parseInt(style.zIndex) > 100) {
                el.remove();
            }
        });
    }
    """)

    page.locator("#awr-control-92").fill("3")

    browser.close()


with sync_playwright() as playwright:
    run(playwright)