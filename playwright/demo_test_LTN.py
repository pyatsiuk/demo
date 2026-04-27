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



    # Натискаю New Option
    page.locator("awr-button").filter(has_text="New Option").click()
    page.wait_for_timeout(1500)
    # Option 2 — це другий div.route-option на сторінці
    option2 = page.locator("div.route-option").nth(1)
    page.wait_for_timeout(1500)

    def fill_date_time(datepicker, date_str, hours, minutes):
        date_input = datepicker.locator("input.awr-control-date")
        time_input = datepicker.locator("input.awr-control-time")
        
        date_input.click()
        date_input.press("Control+a")
        date_input.press_sequentially(date_str, delay=100)
        date_input.press("Tab")
        
        page.wait_for_timeout(500)  # збільшили з 800 до 1500
        
        time_input.click()
        page.wait_for_timeout(200)   # додали паузу після кліку
        time_input.press("ArrowLeft")
        page.wait_for_timeout(200)
        time_input.press("ArrowLeft")
        page.wait_for_timeout(200)
        time_input.press_sequentially(hours, delay=300)    # збільшили з 150 до 300
        page.wait_for_timeout(300)
        time_input.press_sequentially(minutes, delay=300)  # збільшили з 150 до 300
        page.wait_for_timeout(300)
        time_input.press("Tab")
        page.wait_for_timeout(500)

    fill_date_time(option2.locator("awr-datepicker").nth(0), "27/05/2026", "23", "05")
    fill_date_time(option2.locator("awr-datepicker").nth(1), "28/05/2026", "02", "35")
    fill_date_time(option2.locator("awr-datepicker").nth(2), "28/05/2026", "05", "10")
    
    fill_date_time(option2.locator("awr-datepicker").nth(3), "28/05/2026", "08", "30")
    fill_date_time(option2.locator("awr-datepicker").nth(4), "28/05/2026", "23", "50")
    fill_date_time(option2.locator("awr-datepicker").nth(5), "29/05/2026", "00", "45")
    option2.locator("awr-datepicker").nth(2).click()
    option2.locator("label").filter(has_text="Departure Block Date").nth(2).click()
   

    # page.locator("label").filter(has_text="Requirements of LEG (Internal").nth(3).click()

    page.locator("awr-button").filter(has_text="Create Enquiry").click()
    page.wait_for_timeout(5500)   

    print("Enquiry has been created!")

    expect(page.locator(".awr-tab-text").filter(has_text="1. LTN-MAD-BER-LTN")).to_be_visible()

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
    
    page.locator("#cdk-drop-list-5").get_by_text("2. ").click()

    expect(page.locator(".awr-tab-text").filter(has_text="2. ")).to_be_visible()
    expect(page.get_by_role("row", name="LTN, EGGW,").first).to_be_visible()

    # Перший рядок — Flight No
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").first.locator("input.awr-control-input").nth(2).click()
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").first.locator("input.awr-control-input").nth(2).fill("MA2802")
    # Другий рядок — Flight No
    page.get_by_role("row", name="BER, EDDB, Berlin/Brandenburg Intl, Berlin, Germany").first.locator("input.awr-control-input").nth(2).click()
    page.get_by_role("row", name="BER, EDDB, Berlin/Brandenburg Intl, Berlin, Germany").first.locator("input.awr-control-input").nth(2).fill("MA2802")
    # Третій рядок — Flight No
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").nth(1).locator("input.awr-control-input").nth(2).click()
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").nth(1).locator("input.awr-control-input").nth(2).fill("MA2802")
    
    page.wait_for_timeout(100)
    
    page.locator("awr-button").filter(has_text="Update").click()
    page.wait_for_timeout(3000)
    page.locator(".fa-sharp-duotone.fa-solid.fa-tag").click()
    
    page.pause()

    # # page.wait_for_timeout(3000)
    browser.close()
    