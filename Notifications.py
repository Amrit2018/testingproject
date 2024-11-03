import time

from selenium import webdriver

'''ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=ops)'''
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://whatmylocation.com/")
time.sleep(10)
