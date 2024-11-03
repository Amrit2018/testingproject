from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

#Cookies are temporary files that stores data like what activities were performed in the browser, field values etc.

#Get and print all the cookies along with their details
cookies = driver.get_cookies();
print("Size of cookies:",len(cookies))
print(cookies)
for cookie in cookies:
    print(cookie)
    print("Name:"+cookie.get('name') +' '+ "Value:"+cookie.get('value'))

#Add a new cookie.
driver.add_cookie({'name':'AmritCookie',
                   'value': '0d345678901'})
cookies = driver.get_cookies()
print("Size of cookies after adding a new cookie:",len(cookies))
print(driver.get_cookie('AmritCookie'))
print(cookies)

#Delete specific cookie from the browser.
driver.delete_cookie('AmritCookie')
cookies = driver.get_cookies()
print("Size of cookies after deleting a cookie:",len(cookies))
print(cookies)

#Delete all the cookies from the browser.
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of cookies after deleting a cookie:",len(cookies))
print(cookies)


