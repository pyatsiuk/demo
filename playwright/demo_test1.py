from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=False,
        args=['--window-size=1920,1080']
    )

    context = browser.new_context(
        viewport={'width': 1920, 'height': 1080}
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
    
    # Отримуємо позицію input
    box = customer_input.bounding_box()
    print(f"Input position: {box}")
    
    # Клікаємо на ПРАВУ частину input (де знаходиться chevron)
    # Chevron зазвичай на відстані 10-30px від правого краю
    page.mouse.click(box['x'] + box['width'] - 20, box['y'] + box['height'] / 2)
    print("✓ Клікнули на chevron (через координати)")
    
    page.wait_for_timeout(1000)
    
    # Тепер вводимо текст
    customer_input.fill("_QA Pavel")
    page.wait_for_timeout(1000)
    
    # Вибираємо через keyboard
    page.keyboard.press("ArrowDown")
    page.wait_for_timeout(300)
    page.keyboard.press("Enter")
    
    page.wait_for_timeout(500)
    
    value = customer_input.input_value()
    print(f"Customer value: {value}")
    
    page.pause()
    browser.close()