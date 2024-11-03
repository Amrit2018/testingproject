import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ops = webdriver.ChromeOptions()
ops.add_argument("--headless")
driver = webdriver.Chrome(options=ops)
driver.maximize_window()
my_wait = WebDriverWait(driver, 10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

username = my_wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']")))
username.send_keys("Admin")
#driver.find_element(By.XPATH, "//input[@placeholder='Username']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

claim = my_wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Claim']")))
claim.click()
#driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Claim']").click()
#driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active]").click()
#time.sleep(5)

count_status = 0

rows = my_wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='orangehrm-container']/div/div[2]/div")))
#rows = my_wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='orangehrm-container']/div/div[2]/div")))
no_of_rows = len(rows)
print(no_of_rows)
#no_of_rows = len(driver.find_elements(By.XPATH, "//div[@class='orangehrm-container']/div/div[2]/div"))
for r in range(1, no_of_rows+1):
    status = driver.find_element(By.XPATH, "//div[@class='orangehrm-container']/div/div[2]/div["+str(r)+"]/div/div[7]/div").text

    if status=="Submitted":
        count_status += 1
print(count_status)