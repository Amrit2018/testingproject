import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.nopcommerce.com/en")
driver.implicitly_wait(10)

reglink = Keys.CONTROL+Keys.ENTER
driver.find_element(By.LINK_TEXT, "Get started").send_keys(reglink)
time.sleep(5)


