import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
from selenium.webdriver.support.select import Select
import XLUtils

file = "D:\Python\python-selenium\seleniumPavan\moneycontrol.xlsx"
row_num = XLUtils.get_row(file, "Sheet1")
col_num = XLUtils.get_col(file, "Sheet1")
prin, intrst, prd, ten, frncy, expval = 0, 0, 0, 0, 0, 0
for r in range(2, row_num+1):
    for c in range(1, col_num+1):
        if c==1:
            prin = XLUtils.read_val(file, "Sheet1", r, c)

        elif c==2:
            intrst = XLUtils.read_val(file, "Sheet1", r, c)
            #time.sleep(5)
        elif c==3:
            prd = XLUtils.read_val(file, "Sheet1", r, c)
            #time.sleep(5)
        elif c==4:
            ten = XLUtils.read_val(file, "Sheet1", r, c)
            #time.sleep(5)
        elif c==5:
            frncy = XLUtils.read_val(file, "Sheet1", r, c)
            #time.sleep(5)
        elif c==6:
            expval = XLUtils.read_val(file, "Sheet1", r, c)
        else:
            pass
        time.sleep(5)

    ops = webdriver.ChromeOptions()
    ops.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=ops)
    driver.maximize_window()
    driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")

    principal = driver.find_element(By.XPATH, "//input[@id='principal']")
    principal.send_keys(prin)
    interest = driver.find_element(By.XPATH, "//input[@id='interest']")
    interest.send_keys(intrst)
    period = driver.find_element(By.XPATH, "(//input[@id='tenure'])[1]")
    period.send_keys(prd)
    tenure_period = driver.find_element(By.XPATH, "//select[@id='tenurePeriod']")
    tenure = Select(tenure_period)
    tenure.select_by_visible_text(ten)
    fre = driver.find_element(By.XPATH, "//select[@id='frequency']")
    frequency = Select(fre)
    frequency.select_by_visible_text(frncy)
    calculate = driver.find_element(By.XPATH, "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']")
    calculate.click()
    actval = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text
    print(actval)
    if float(actval) == float(expval):
        print("Test Passed")
        XLUtils.write_val(file, "Sheet1", r , 7, "Passed")
        #XLUtils.fillGreenColor(file, "Sheet1", r, 6)

    else:
        print("Test Failed")
        #XLUtils.fillRedColor(file, "Sheet1", r, 6)

    clear = driver.find_element(By.XPATH, "//img[@class='PL5']")
    clear.click()

    driver.close()