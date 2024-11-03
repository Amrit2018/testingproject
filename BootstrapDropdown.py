import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

countries = driver.find_elements(By.XPATH, "//span//ul[@id='select2-billing_country-results']//li")
print(len(countries))
for country in countries:
    if country.text=="China":
        country.click()
        break

time.sleep(10)