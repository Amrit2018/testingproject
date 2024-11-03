from selenium import webdriver
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
ops.add_argument('--headless')
driver = webdriver.Chrome(options=ops)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

#Get the total no. of rows.
no_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
print(no_of_rows)

#Get the total no. of columns.
no_of_cols = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr//th"))
print(no_of_cols)

#Read specific row and column data.
print(driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]//td[2]").text)

#Read all the rows and columns data.
for r in range(2, no_of_rows+1):
    for c in range(1, no_of_cols+1):
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]//td["+str(c)+"]").text
        print(data, end='          ')
    print()

#Read data based on condition (List book name is author name is Mukesh)
for r in range(2, no_of_rows+1):
    data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]//td[2]").text

    if data=="Mukesh":
        print(driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]").text, end='          ')
    print()