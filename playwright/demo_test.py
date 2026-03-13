from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        storage_state="/Users/app55/Projects/awery/playwright/.auth/storage_state.json"
    )

    page = context.new_page()

    page.goto("https://demo.awery.com.ua/apps/dev/")

    print("Current URL:", page.url)

    page.get_by_text("Office Enquiries").nth(1).click()
    expect(page.get_by_role("row", name="ID Ref No. Broker Status")).to_be_visible(timeout=15000)
    page.wait_for_timeout(2000)

    page.locator("awr-button:nth-child(10)").click()
    expect(page.get_by_role("textbox", name="Speech Language")).to_be_visible(timeout=15000)
    page.wait_for_timeout(2000)

    page.locator(".awr-equal.awr-toggled").click()
    page.wait_for_timeout(2000)

    page.locator(".flex-shrink-item > .ng-untouched > .awr-control > .awr-control-actions > .awr-open-icon").first.click()
    page.get_by_role("textbox", name="Customer").fill("_QA Pavel Customer, 29029029029555, 60193040019, Awery Demo Company, United Kingdom, London, customer, 29, 987, PL7272445205")
    page.get_by_role("textbox", name="Customer").press("Enter")
    page.get_by_text("Reparse TextCreate Enquiry").click()

    page.locator("autocomplete-airports > .ng-untouched > .awr-control > .awr-control-actions > .awr-open-icon").first.click()
    
    page.get_by_role("textbox", name="From").fill("MIA, KMIA, Miami International, Miami, United States of America")
    # page.get_by_role("textbox", name="From", placeholder="MIA, KMIA, Miami International, Miami, United States of America")
    # page.get_by_role("textbox", name="From").fill("MIA, KMIA, Miami International, Miami, United States of America")
    page.get_by_role("textbox", name="From").press("Enter")
    page.get_by_role("textbox", name="From").click()
   
    page.get_by_role("textbox", name="To", exact=True).fill("LAX, KLAX, Los Angeles International, Los Angeles, United States of America")
    # page.get_by_role("textbox", name="To", exact=True).press("Enter")
    
    page.get_by_role("textbox", name="Contact Name").click()
    page.get_by_role("textbox", name="Contact Name").fill("Tom")
    # page.get_by_role("textbox", name="Customer").click()
    # page.get_by_role("textbox", name="Customer").fill("qa")
    # page.get_by_role("textbox", name="From").click()

    page.pause()

    browser.close()