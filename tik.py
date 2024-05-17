import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")

driver = webdriver.ChromeOptions(options=options)

url = 'https://www.tiktok.com/en/'
driver.get(url)
time.sleep(15)
# skip = driver.find_element(By.CLASS_NAME, 'css-txolmk-DivGuestModeContainer exd0a435')
# time.sleep(5)
# skip.send_keys(Keys.ENTER)
time.sleep(5)
driver.maximize_window()
window = driver.find_element(By.TAG_NAME, 'html')
driver.execute_script(
        "window.scrollTo(0, document.documentElement.scrollHeight);")
time.sleep(2)
while True:
    page_down = 5
    for item in range(page_down):
        driver.maximize_window()
    window.send_keys(Keys.ARROW_DOWN, item)
    time.sleep(5)