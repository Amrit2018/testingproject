import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# time.sleep() - Performance of the script is very poor. If the element is not found within the time mentioned, there is a chance of getting exception.
# Implicit wait -  Available for the entire driver lifecycle. If the element is available within the time, it proceeds furthur
# But if the element is not found, it throws exception.
# Explicit wait works based on the condition. If the element is not found, exception is handled.
# poll_frequency regularly checks the element list in the specified time. This improves the performance of explicit wait.

driver = webdriver.Chrome()

#Implicit Wait
#driver.implicitly_wait(10)

#Explicit wait declaration
my_wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])

driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#username = driver.find_element(By.NAME, "username")
username = my_wait.until(EC.presence_of_element_located((By.NAME, "username")))
EC.
password = driver.find_element(By.XPATH, "//input[@name='password']")
submit = driver.find_element(By.XPATH, "//button[@type='submit']")

print(username.is_displayed())
username.send_keys("Admin")
password.send_keys("admin123")
submit.click()
page_title = driver.title
print(page_title)




