import re
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
    # Use nth(-1) or last() - always last row

    page.locator("autocomplete-airports").last.locator("input").fill("BER")
    page.wait_for_timeout(1000)
    page.get_by_text("BER").first.click()

    # Add new sector
    page.locator(".route-modification-buttons > awr-button:nth-child(2)").click()
    page.wait_for_timeout(1000)

    # I take last (second) row of routing and field its 'To' field
    # Use nth(-1) or last() — always last row

    page.locator("autocomplete-airports").last.locator("input").fill("LTN")
    page.wait_for_timeout(1000)
    page.get_by_text("LTN").first.click()
    page.wait_for_timeout(2000)

    page.locator("awr-button").filter(has_text="Create Enquiry").click()
    page.wait_for_timeout(3000)   
    print("Enquiry has been created!")

    expect(page.locator("app-enquiry-info").get_by_text("Quote ID")).to_be_visible()

    page.locator(".fa-route").click()
    expect(page.get_by_role("row", name="LTN, EGGW,").first).to_be_visible()

    # Перший рядок — Flight No
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").first.locator("input.awr-control-input").nth(2).click()
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").first.locator("input.awr-control-input").nth(2).fill("MA0602")
    # Другий рядок — Flight No
    page.get_by_role("row", name="BER, EDDB, Berlin/Brandenburg Intl, Berlin, Germany").first.locator("input.awr-control-input").nth(2).click()
    page.get_by_role("row", name="BER, EDDB, Berlin/Brandenburg Intl, Berlin, Germany").first.locator("input.awr-control-input").nth(2).fill("MA0602")
    # Третій рядок — Flight No
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").nth(1).locator("input.awr-control-input").nth(2).click()
    page.get_by_role("row", name="LTN, EGGW, London Luton, London, United Kingdom").nth(1).locator("input.awr-control-input").nth(2).fill("MA0602")
    
    page.wait_for_timeout(100)

    page.locator("awr-button").filter(has_text="Update").click()
    page.wait_for_timeout(3000)

    # Operators page
    page.locator(".fa-sharp-duotone.fa-solid.fa-tower-control").click()
    page.get_by_label("Operator").click()
    page.get_by_label("Operator").fill("2Excel")
    page.wait_for_timeout(1000)
    page.get_by_text("2Excel").first.click()
    page.locator(".col-sm-3 > .flex-row > .awr-sm").first.click()
    expect(page.get_by_role("row", name="LTN-MAD-BER-LTN Operator 2Excel BroadSword, EXC, United Kingdom, 0, (Aircraft:")).to_be_visible()

    row_2excel = page.get_by_role("row", name="2Excel")

    # AC Type — перший autocomplete в рядку
    row_2excel.locator("input.awr-autocomplete").nth(2).click()
    row_2excel.locator("input.awr-autocomplete").nth(2).fill("Dornier")
    row_2excel.locator("input.awr-autocomplete").nth(2).press("Enter")

    # Реєстрація — другий autocomplete в рядку
    row_2excel.locator("input.awr-autocomplete").nth(3).click()
    row_2excel.locator("input.awr-autocomplete").nth(3).fill("C-GSAX")
    row_2excel.locator("input.awr-autocomplete").nth(3).press("Enter")

    page.locator("awr-button").filter(has_text="Update").click()
    page.wait_for_timeout(2000)

    # Pricing page
    # For the first operator
    page.locator(".fa-sharp-duotone.fa-solid.fa-tag").click()
    page.wait_for_timeout(1500)

    page.locator('awr-number input.awr-control-input').nth(1).fill("100")
    page.wait_for_timeout(1000)
    page.locator('awr-number input.awr-control-input').nth(7).fill("1000")
    page.wait_for_timeout(1000)

    page.locator(".scrollable-content").first.click()
    # page.get_by_role("textbox", name="General Margin %").click()
    # page.get_by_role("textbox", name="General Margin %").fill("50")
    # page.locator(".flex-display-row > div:nth-child(4) > .flex-row > .awr-sm").click()
    page.wait_for_timeout(1000)
    expect(page.get_by_role("row", name="Airport Taxes 1.00 100.00 100")).to_be_visible()
    page.wait_for_timeout(2000)

    page.locator("awr-button").filter(has_text="Update").click()
    expect(page.get_by_role("row", name="Airport Taxes 1.00 100.00 100")).to_be_visible()
    page.wait_for_timeout(3000)
    # page.locator(".app-toolbar-horizontal > awr-button").first.click()
    # page.locator("awr-button").filter(has_text="Update").click()

    # Second Operator Prices
    page.get_by_role("rowgroup").filter(has_text="2 2Excel BroadSword").click()
    page.wait_for_timeout(1000)

    # page.pause()
    page.locator('awr-number input.awr-control-input').nth(1).fill("200")
    page.wait_for_timeout(1000)
    page.locator('awr-number input.awr-control-input').nth(7).fill("3000")
    page.wait_for_timeout(1000)

    
    # page.pause()
    page.locator(".scrollable-content").first.click()
    page.get_by_role("textbox", name="General Margin %").click()
    page.get_by_role("textbox", name="General Margin %").fill("50")
    page.wait_for_timeout(1000)
    page.locator(".flex-display-row > div:nth-child(4) > .flex-row > .awr-sm").click()
    expect(page.get_by_role("row", name="Airport Taxes 1.00 200.00")).to_be_visible()
    page.wait_for_timeout(1000)

    page.locator("awr-button").filter(has_text="Update").click()
    expect(page.get_by_role("row", name="Airport Taxes 1.00 200.00")).to_be_visible()
    page.wait_for_timeout(1000)
    # WON
    page.get_by_role("rowgroup").filter(has_text="A220-300").click()
    page.locator("awr-button").filter(has_text="WON").click()
    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="Reason *").click()
    page.get_by_role("textbox", name="Reason *").fill("Better Aircraft")
    page.get_by_role("textbox", name="Reason *").press("Enter")
    page.get_by_role("textbox", name="Reason Comments").click()
    page.get_by_role("textbox", name="Reason Comments").fill("T001")
    page.get_by_role("textbox", name="Contractor Basis *").click()
    page.get_by_role("textbox", name="Contractor Basis *").fill("Agent")
    page.get_by_role("textbox", name="Contractor Basis *").press("Enter")
    page.locator("awr-button").filter(has_text="Save").click()
    # page.pause()

    # Create Flight
    page.locator("awr-button").filter(has_text="Create Flight").click()
    page.get_by_role("textbox", name="Flight Category").click()
    page.get_by_role("textbox", name="Flight Category").press("ControlOrMeta+a")
    page.get_by_role("textbox", name="Flight Category").fill("Flight")
    page.locator("div.awr-list-row-text").nth(3).click()
    page.wait_for_timeout(1000)

    page.locator("awr-button").filter(has_text=re.compile(r"^Create$")).click()
    page.wait_for_timeout(5000)
    # page.pause()
    browser.close()

    
    