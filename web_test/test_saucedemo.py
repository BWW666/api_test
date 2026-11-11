from playwright.sync_api import sync_playwright
import time # 导入时间库

def test_login_and_fill():
    # 加上 slow_mo=1000，意思是每一步操作停顿 1000 毫秒（1秒），让你看清楚
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000) 
        page = browser.new_page()
        
        page.goto("https://www.saucedemo.com/")
        
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        
        page.locator("#login-button").click()
        
        page.wait_for_url("**/inventory.html")
        title = page.locator(".title").inner_text()
        assert title == "Products"
        
        page.screenshot(path="reports/login_success.png")
        print("✅ UI 自动化测试通过，已截图！")
        
        # 强制停留 5 秒钟，让你看清楚登录后的页面
        time.sleep(5) 
        
        browser.close()

if __name__ == "__main__":
    test_login_and_fill()