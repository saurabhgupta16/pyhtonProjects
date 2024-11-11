import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#service_obj = Service("C:\\Users\\saura\\PycharmProjects\\Browser\\chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)
#driver1=webdriver.Firefox()
#driver1.get("https://google.com")
#driver2=webdriver.Edge()
#driver2.get("https://google.com")
driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)





time.sleep(3)
