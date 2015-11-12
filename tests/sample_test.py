from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://localhost:8000")


assert "This is my home page" in browser.page_source


browser.quit()