# import time
# from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver

driver = webdriver.Chrome()
print(111111)
driver.get("https://www.baidu.com")
print(driver.requests)
for request in driver.requests:
    if request.response:
        print("Url:", request.url)
        print("Code:", request.response.status_code)
        print("Content-Type:", request.response.headers['Content-Type'])
driver.quit()
