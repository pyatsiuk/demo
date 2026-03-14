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
    page.wait_for_timeout(1500)

    page.locator("awr-button:nth-child(10)").click()
    expect(page.get_by_role("textbox", name="Speech Language")).to_be_visible(timeout=15000)
    page.wait_for_timeout(1500)

    page.locator(".awr-equal.awr-toggled").click()
    page.wait_for_timeout(1500)

    # Input Customer
    page.locator(".flex-shrink-item > .ng-untouched > .awr-control > .awr-control-actions > .awr-open-icon").first.click()
    page.get_by_role("textbox", name="Customer").fill("_QA Pavel Customer, 29029029029555, 60193040019, Awery Demo Company, United Kingdom, London, customer, 29, 987, PL7272445205")
    page.get_by_role("textbox", name="Customer").press("Enter")
    page.get_by_text("Reparse TextCreate Enquiry").click()

    page.locator("autocomplete-airports > .ng-untouched > .awr-control > .awr-control-actions > .awr-open-icon").first.click()
   
    # Input the first airport From
    page.get_by_role("textbox", name="From", exact=True).fill("MIA")
    page.wait_for_timeout(1000)
    page.get_by_text("MIA").first.click()
    
     # Input the first airport To
    page.get_by_role("textbox", name="To", exact=True).fill("LAX")
    page.wait_for_timeout(1000)
    page.get_by_text("LAX").first.click()

    # Add new sector
    page.locator(".route-modification-buttons > awr-button:nth-child(2)").click()
    page.wait_for_timeout(1000)

    # I take last (second) row of routing and field its 'To' field
    # Use nth(-1) or last() — always last row
    
    page.locator("autocomplete-airports").last.locator(".awr-open-icon").click()
    page.wait_for_timeout(1000)

    page.locator("autocomplete-airports").last.locator("input").fill("NGS")
    page.wait_for_timeout(1000)
    page.get_by_text("NGS").first.click()

    # page.pause()

    

    # page.locator("autocomplete-airports")
    # page.get_by_text("Reparse TextCreate Enquiry").click()
    page.locator("awr-button").filter(has_text="Create Enquiry").click()
    page.wait_for_timeout(3500)   

    print("Enquiry has been created!")
    

    # page.get_by_role("textbox", name="To", exact=True).fill("LAX, KLAX, Los Angeles International, Los Angeles, United States of America")
    # page.get_by_role("textbox", name="Contact Name").click()
    # page.get_by_role("textbox", name="Contact Name").fill("Tom")

    browser.close()