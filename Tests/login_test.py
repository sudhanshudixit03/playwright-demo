from playwright.sync_api import sync_playwright

def test_login():

    with sync_playwright() as p:

        # Launch browser
        browser = p.chromium.launch(headless=False)

        # Create page
        page = browser.new_page()

        # Open application
        page.goto("https://www.saucedemo.com/")

        # Enter username
        page.fill("#user-name", "standard_user")

        # Enter password
        page.fill("#password", "secret_sauce")

        # Click login
        page.click("#login-button")

        # Validation
        assert page.locator(".title").inner_text() == "Products"

        print("Login Test Passed")

        # Close browser
        browser.close()