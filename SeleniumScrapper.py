from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
DRIVER_path = "chromedriver_win32/chromedriver"

driver = webdriver.Chrome(options=options,executable_path= DRIVER_path)

driver.get("https://www.nintendo.com/")
print(driver.page_source)
driver.quit()