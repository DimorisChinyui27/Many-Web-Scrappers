from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://aitextpromptgenerator.com/builder?prompt=Kermit%20the%20frog%20muppet%20character%20jumping%20over%20a%20fence&rnd=1666185111347")

try:
   element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='col-md-3 col-12']/div[@class='d-flex align-center justify-center v-card v-card--link v-sheet v-sheet--outlined theme--dark']")))
   print("Element found succesfully")
   print(element)

except Exception as e:
   print(e)

elems = driver.find_element(by=By.XPATH, value="//div[@class='col-md-3 col-12']")

print(elems)
driver.quit()