from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("")
driver.find_element(By.XPATH, "").send_keys("C:\Users\amrit\OneDrive\Desktop\sample.docx")