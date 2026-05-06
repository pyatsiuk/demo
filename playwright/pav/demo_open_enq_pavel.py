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

    # page.pause()

    page.get_by_role("textbox", name="Enquiry No").click()
    page.get_by_role("textbox", name="Enquiry No").fill("10058")
    page.get_by_role("textbox", name="Enquiry No").press("Enter")
    page.wait_for_timeout(1000)
    page.get_by_text("10058").click()
    page.get_by_text("10058").click()
    page.wait_for_timeout(2000)   

    expect(page.locator("app-enquiry-info").get_by_text("Quote ID")).to_be_visible()

    page.locator(".fa-route").click()
    expect(page.get_by_role("row", name="LTN, EGGW,").first).to_be_visible()
  
    page.wait_for_timeout(100)
    page.pause()
    
    page.locator(".fa-sharp-duotone.fa-solid.fa-tower-control").click()
    page.get_by_label("Operator").click()
    page.get_by_label("Operator").fill("2Excel")
    page.wait_for_timeout(1000)
    page.get_by_text("2Excel").first.click()
    page.locator(".col-sm-3 > .flex-row > .awr-sm").first.click()
    expect(page.get_by_role("row", name="LTN-MAD-BER-LTN Operator 2Excel BroadSword, EXC, United Kingdom, 0, (Aircraft:")).to_be_visible()

    page.locator("tbody:nth-child(2) > tr > td:nth-child(5) > .awr-td > div > div > .flex-row > .flex-shrink-item > .awr-control > .awr-control-actions > .awr-open-icon").click()
    page.locator("#awr-control-324").click()
    page.locator("#awr-control-324").fill("Dornier")
    page.locator("#awr-control-324").press("Enter")
    expect(page.get_by_role("row", name="LTN-MAD-BER-LTN Operator 2Excel BroadSword, EXC, United Kingdom, 0, (Aircraft:")).to_be_visible()

    page.locator("tbody:nth-child(2) > tr > td:nth-child(6) > .awr-td > div > div > .flex-row > .flex-shrink-item > .awr-control > .awr-control-actions > .awr-open-icon").click()
    page.locator("#awr-control-325").click()
    page.locator("#awr-control-325").fill("c")
    page.locator("#awr-control-325").press("Enter")
    expect(page.get_by_role("row", name="LTN-MAD-BER-LTN Operator 2Excel BroadSword, EXC, United Kingdom, 0, (Aircraft:")).to_be_visible()

    page.locator("#awr-control-325").click()
    page.locator("#awr-control-325").fill("c-gs")
    page.locator("#awr-control-325").press("Enter")
    expect(page.get_by_role("row", name="LTN-MAD-BER-LTN Operator 2Excel BroadSword, EXC, United Kingdom, 0, (Aircraft:")).to_be_visible()

    page.locator("awr-button").filter(has_text="Update").click()
    expect(page.get_by_role("row", name="LTN-MAD-BER-LTN Operator 2Excel BroadSword, EXC, United Kingdom, 0, (Aircraft:")).to_be_visible()

    page.locator(".fa-sharp-duotone.fa-solid.fa-tag").click()

    
    # page.locator("awr-button").filter(has_text="Update").click()
    # page.wait_for_timeout(3000)

    page.locator(".fa-sharp-duotone.fa-solid.fa-tag").click()
    page.wait_for_timeout(1500)

    page.pause()
    # Знаходимо всі Type інпути в таблиці цін
    type_inputs = page.locator("awr-virtual-scroll.body").nth(1).locator("input.awr-autocomplete")

    # Перший рядок
    type_inputs.nth(0).click()
    type_inputs.nth(0).press("Control+a")
    type_inputs.nth(0).fill("Airport Taxes")
    page.wait_for_timeout(1000)
    page.get_by_text("Airport Taxes").first.click()
    page.wait_for_timeout(500)
    # type_inputs.nth(8).click()
    # type_inputs.nth(8).fill("Pav Operator, United Kingdom, 0,  (Aircraft: 2)")
    # page.wait_for_timeout(1000)
    # page.get_by_text("Pav Operator, United Kingdom, 0,  (Aircraft: 2)").first.click()

    # Другий рядок
    type_inputs.nth(9).click()
    type_inputs.nth(9).press("Control+a")
    type_inputs.nth(9).fill("Documentation")
    c
    page.wait_for_timeout(500)
    # type_inputs.nth(17).click()
    # type_inputs.nth(17).fill("Pav Operator, United Kingdom, 0,  (Aircraft: 2)")
    # page.wait_for_timeout(1000)
    # page.get_by_text("Pav Operator, United Kingdom, 0,  (Aircraft: 2)").first.click()

    # Додаємо новий рядок
    page.locator("awr-button").filter(has_text="New").click()
    page.wait_for_timeout(1000)
    type_inputs.nth(18).scroll_into_view_if_needed()

    # Третій рядок
    type_inputs.nth(18).click()
    type_inputs.nth(18).press("Control+a")
    type_inputs.nth(18).fill("OBC fee")
    page.wait_for_timeout(1000)
    page.get_by_text("OBC fee").first.click()
    page.wait_for_timeout(500)
    # type_inputs.nth(26).click()
    # type_inputs.nth(26).fill("Pav Operator, United Kingdom, 0,  (Aircraft: 2)")
    # page.wait_for_timeout(1000)
    # page.get_by_text("Pav Operator, United Kingdom, 0,  (Aircraft: 2)").first.click()

    page.pause()
    page.locator('awr-number input.awr-control-input').nth(1).fill("250")
    page.wait_for_timeout(3000)
    page.locator('awr-number input.awr-control-input').nth(7).fill("380")
    page.wait_for_timeout(3000)
    # page.locator("awr-virtual-scroll.body").evaluate("el => el.scrollTop += 300")
    page.locator('awr-number input.awr-control-input').nth(13).fill("954")
    page.wait_for_timeout(3000)

    # page.locator("awr-button").filter(has_text="Update").click()
    # page.wait_for_timeout(3000)




    # # page.get_by_role("textbox", name="Type", exact=True).fill("Airport Taxes")
    # # page.wait_for_timeout(1000)
    # # page.get_by_text("Airport Taxes").first.click()
    # # page.pause()
    # # # page.wait_for_timeout(3000)
    browser.close()

    
    