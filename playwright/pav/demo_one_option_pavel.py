from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False)

    context = browser.new_context(
        storage_state="/Users/app55/Projects/awery/playwright/.auth/storage_state.json",
        viewport={"width": 1600, "height": 1000},
        device_scale_factor=1
    )

    page = context.new_page()

    page.goto("https://aaa-pavel-qa.git.awery.com.ua/apps/dev/")
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
    page.wait_for_timeout(1500)
    page.get_by_role("textbox", name="Customer").fill("_QA Pavel Customer, 29029029029555, 60193040019, Awery Demo Company, United Kingdom, London, customer, 29, 987, PL7272445205")
    page.get_by_role("textbox", name="Customer").press("Enter")
    page.get_by_text("Reparse TextCreate Enquiry").click()

    page.locator("autocomplete-airports > .ng-untouched > .awr-control > .awr-control-actions > .awr-open-icon").first.click()
    
    # Input the first airport From
    page.get_by_role("textbox", name="From", exact=True).fill("LTN")
    page.wait_for_timeout(1000)
    page.get_by_text("LTN").first.click()
    
     # Input the first airport To
    page.get_by_role("textbox", name="To", exact=True).fill("MAD")
    page.wait_for_timeout(1000)
    page.get_by_text("MAD").first.click()

    # Add new sector
    page.locator(".route-modification-buttons > awr-button:nth-child(2)").click()
    page.wait_for_timeout(1000)

    # I take last (second) row of routing and field its 'To' field
    # Use nth(-1) or last() — always last row
    
    # page.locator("autocomplete-airports").last.locator(".awr-open-icon").click()
    # page.wait_for_timeout(1000)

    page.locator("autocomplete-airports").last.locator("input").fill("BER")
    page.wait_for_timeout(1000)
    page.get_by_text("BER").first.click()

    # Add new sector
    page.locator(".route-modification-buttons > awr-button:nth-child(2)").click()
    page.wait_for_timeout(1000)

    # I take last (second) row of routing and field its 'To' field
    # Use nth(-1) or last() — always last row
    
    # page.locator("autocomplete-airports").last.locator(".awr-open-icon").click()
    # page.wait_for_timeout(1000)

    page.locator("autocomplete-airports").last.locator("input").fill("LTN")
    page.wait_for_timeout(1000)
    page.get_by_text("LTN").first.click()
    page.wait_for_timeout(2000)

    page.locator("awr-button").filter(has_text="Create Enquiry").click()
    page.wait_for_timeout(5500)   
    print("Enquiry has been created!")

    expect(page.locator("app-enquiry-info").get_by_text("Quote ID")).to_be_visible()

    page.locator(".fa-route").click()
    expect(page.get_by_role("row", name="LTN, EGGW,").first).to_be_visible()

    # Перший рядок — Flight No
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").first.locator("input.awr-control-input").nth(2).click()
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").first.locator("input.awr-control-input").nth(2).fill("MA2801")
    # Другий рядок — Flight No
    page.get_by_role("row", name="BER, EDDB, Berlin/Brandenburg Intl, Berlin, Germany").first.locator("input.awr-control-input").nth(2).click()
    page.get_by_role("row", name="BER, EDDB, Berlin/Brandenburg Intl, Berlin, Germany").first.locator("input.awr-control-input").nth(2).fill("MA2801")
    # Третій рядок — Flight No
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").nth(1).locator("input.awr-control-input").nth(2).click()
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").nth(1).locator("input.awr-control-input").nth(2).fill("MA2801")
    
    page.wait_for_timeout(100)

    
    page.locator("awr-button").filter(has_text="Update").click()
    page.wait_for_timeout(3000)
    page.locator(".fa-sharp-duotone.fa-solid.fa-tag").click()
    page.wait_for_timeout(1500)

    # Перший рядок — очищуємо і вводимо новий тип
    row1 = page.get_by_role("textbox", name="01. Repositioning flight 01.")
    row1.click()
    row1.press("Control+a")
    row1.fill("Airport Taxes")
    page.wait_for_timeout(1000)
    page.get_by_text("Airport Taxes").first.click()
    page.wait_for_timeout(500)

    # Другий рядок
    row2 = page.get_by_role("textbox", name="Catering")
    row2.click()
    row2.press("Control+a")
    row2.fill("Catering")
    page.wait_for_timeout(1000)
    page.get_by_text("Catering").first.click()
    page.wait_for_timeout(500)
    

    page.pause()
    page.locator('awr-number input.awr-control-input').nth(1).fill("250")
    page.wait_for_timeout(3000)
    page.locator('awr-number input.awr-control-input').nth(7).fill("380")
    page.wait_for_timeout(3000)

    page.locator("awr-button").filter(has_text="Update").click()
    page.wait_for_timeout(3000)
    
    browser.close()

    
    