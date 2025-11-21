from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://demo.awery.com.ua/apps/dev/login")
    page.get_by_placeholder("Enter User Name").fill("ray")
    page.get_by_placeholder("Enter Password").fill("123")

    login_button = page.locator("awr-button", has_text="Log In")
    login_button.click(force=True)  

    # 👇 важливо — дочекатися переходу на головну
    page.wait_for_url("**/apps/dev/**", timeout=15000)

    context.storage_state(path="/Users/app55/Projects/awery/playwright/.auth/storage_state.json")
    print("✅ Auth state saved")

    browser.close()
