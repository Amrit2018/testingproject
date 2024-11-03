import time

from selenium import webdriver
import os

from selenium.webdriver.common.by import By

location = os.getcwd() #Gets the current working directory

def chrome_setup():

    #download files in desired location
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(options=ops)
    driver.maximize_window()
    return driver

def edge_setup():

    #download files in desired location
    preferences = {"download.default_directory": location}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    driver = webdriver.Edge(options=ops)
    driver.maximize_window()
    return driver

def firefox_setup():

    #download files in desired location
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference("browser.download.folderList", 2) #0-Desktop, 1-Downloads, 2-Desired Location
    ops.set_preference("browser.download.dir", location)

    driver = webdriver.Firefox(options=ops)
    driver.maximize_window()
    return driver

#driver = chrome_setup()
#driver=edge_setup()
driver = firefox_setup()
driver.implicitly_wait(10)
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")

driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(10)