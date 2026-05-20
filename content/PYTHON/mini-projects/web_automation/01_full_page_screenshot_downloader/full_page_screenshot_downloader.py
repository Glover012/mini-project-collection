from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://python.org")
driver.maximize_window()

fullXpath = "/html/body/div/header/div/div[2]/div/form/fieldset/input"
xpath = '//*[@id="id-search-field"]'

searchInput = driver.find_element(By.XPATH, value=fullXpath)
searchInput.send_keys("django")

goButtonID = "submit" 
driver.find_element(By.TAG_NAME, value="body").screenshot("python.org.1.png")
goButton = driver.find_element(By.ID, value=goButtonID)
goButton.click()

driver.save_screenshot("python.org.2.png")

func = lambda arg: driver.execute_script(f"return document.body.parentNode.scroll{arg}")

driver.set_window_size(width=func("Width"), height=func("Height"))

driver.find_element(By.TAG_NAME, value="body").screenshot("python.org.3.png")

driver.quit()
