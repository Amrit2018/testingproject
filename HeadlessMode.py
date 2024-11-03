from selenium import webdriver

def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.add_argument("headless=new")
    driver = webdriver.Chrome(options=ops)
    return driver

def headless_edge():
    ops = webdriver.EdgeOptions()
    ops.add_argument("headless=new")
    driver = webdriver.Edge(options=ops)
    return driver

'''def headless_firefox():
    ops = webdriver.FirefoxOptions()
    ops.add_argument("headless=new")
    driver = webdriver.Firefox(options=ops)
    return driver'''

#driver = headless_chrome()
#driver = headless_firefox()
driver = headless_edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
print(driver.current_url)
print(driver.title)
