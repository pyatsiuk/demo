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



    # Натискаємо New Option
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
        date_input.press_sequentially(date_str, delay=50)
        date_input.press("Tab")
        
        page.wait_for_timeout(500)  # збільшили з 800 до 1500
        
        time_input.click()
        page.wait_for_timeout(100)   # додали паузу після кліку
        time_input.press("ArrowLeft")
        page.wait_for_timeout(100)
        time_input.press("ArrowLeft")
        page.wait_for_timeout(100)
        time_input.press_sequentially(hours, delay=300)    # збільшили з 150 до 300
        page.wait_for_timeout(300)
        time_input.press_sequentially(minutes, delay=300)  # збільшили з 150 до 300
        page.wait_for_timeout(300)
        time_input.press("Tab")
        page.wait_for_timeout(500)
    # Створення Enquiry з невірним UTC часом для другого сектору Arrival при налаштуваннях Australia/Brisbane - Local у юзера
    fill_date_time(option2.locator("awr-datepicker").nth(0), "27/04/2026", "22", "05")
    fill_date_time(option2.locator("awr-datepicker").nth(1), "28/04/2026", "01", "10")
    fill_date_time(option2.locator("awr-datepicker").nth(2), "28/04/2026", "05", "05")
    fill_date_time(option2.locator("awr-datepicker").nth(3), "28/04/2026", "09", "20")





    # page.locator("autocomplete-airports")
    # page.get_by_text("Reparse TextCreate Enquiry").click()
    page.locator("awr-button").filter(has_text="Create Enquiry").click()
    page.wait_for_timeout(5500)   

    print("Enquiry has been created!")
    # page.pause()

    expect(page.locator("awr-button").filter(has_text="All Companies")).to_be_visible()

    page.locator(".fa-route").click()
    expect(page.get_by_role("row", name="MIA, KMIA, Miami")).to_be_visible()
    # Перший рядок — Flight No
    page.get_by_role("row", name="MIA, KMIA, Mi").locator("input.awr-control-input").nth(2).fill("AP2801")
    # Другий рядок — Flight No  
    page.get_by_role("row", name="LAX, KLAX, Lo").locator("input.awr-control-input").nth(2).fill("AP2801")

    # page.locator(".fa-sharp-duotone.fa-solid.fa-tag").click()
    
    page.pause()

    page.wait_for_timeout(3000)
    browser.close()