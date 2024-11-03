import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

#New Tab - Selenium 4: Opens a new window and switches to a new window
driver.get("https://www.nopcommerce.com/en")
driver.switch_to.new_window("window")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

time.sleep(5)


