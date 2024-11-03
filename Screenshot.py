import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.orangehrm.com/")
time.sleep(20)

driver.save_screenshot("D:\Python\python-selenium\seleniumPavan\homepage.png")
driver.save_screenshot(os.getcwd()+"\hopage.png")
driver.get_screenshot_as_file(os.getcwd()+"\orangehome.txt")