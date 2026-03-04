from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(
            storage_state="playwright/.auth/storage_state.json"
        )
    page = context.new_page()  
    page.goto("https://demo.awery.com.ua/apps/dev/")

    page.locator("span.menu-item-name", has_text="Office Enquiries").click()
    expect(page.locator("awr-table.ng-star-inserted")).to_be_visible()

    obc_button = page.locator("awr-button:nth-child(10)")
    obc_button.click()

    expect(page.locator("div.summary")).to_be_visible()

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
    
    page.wait_for_timeout(1000)
    
    # Знаходимо Customer input
    customer_input = page.locator('input[placeholder="Customer"]')
    customer_input.wait_for(state="visible")
    
    # Клікаємо на input з force
    customer_input.click(force=True)
    
    # ПАУЗА ТУТ - подивись чи з'явився dropdown
    page.pause()
    
    # Продовжимо після того як побачимо що відбувається
    browser.close()