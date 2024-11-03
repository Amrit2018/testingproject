import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://text-compare.com/")

textbox1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
textbox2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

textbox1.send_keys("My name is Amrit")
my_act = ActionChains(driver)
my_act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
my_act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

my_act.send_keys(Keys.TAB)
my_act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)