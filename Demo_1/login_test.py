from playwright.sync_api import sync_playwright

   # Fuction/Method to perform login test we use text def
def test_login():
    with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto("https://www.saucedemo.com/")
                page.fill("#user-name","standard_user")
                page.fill("#password","secret_sauce")
                page.click("#login-button")
                assert page.locator(".title").inner_text()=="Products"
                page.screenshot(path="Demo_1/screenshots/login_screenshot.png")
                print("Login test passed")
            # This line prints success message in console
                browser.close()                 #this line is for closing the browser



        #     for running this test case we can use this command- python -m pytest Demo_1/login_test.py





