import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 1. Open Web Browser
# 2. Open URL https://opensource-demo.orangehrmlive.com/
# 3. Enter username (Admin).
# 4. Enter password (admin123).
# 5. Click on Login.
# 6. Compare title of the home page with the expected title.
# 7. Close browser.

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
username = driver.find_element(By.NAME,"username")
password = driver.find_element(By.XPATH, "//input[@name='password']")
submit= driver.find_element(By.XPATH, "//button[@type='submit']")


print(username.is_displayed())

username.send_keys("Admin")
password.send_keys("admin123")
submit.click()


time.sleep(10)

#title = driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-chevron-right']")
page_title = driver.title
print(page_title)
#title.click()



