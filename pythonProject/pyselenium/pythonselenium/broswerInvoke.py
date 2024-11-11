import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.edge.service import Service
#from selenium.webdriver.firefox.service import Service

#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver=webdriver.Edge()

#service_obj = Service("C:\\Users\\saura\\PycharmProjects\\Browser\\chromedriver.exe")
#driver = webdriver.Chrome(service=service_obj)

#service_obj = Service("C:\\Users\\saura\\PycharmProjects\\Browser\\msedgedriver.exe")
#driver = webdriver.Edge(service = service_obj)


service_obj = Service("C:\\Users\\saura\\PycharmProjects\\Browser\\geckodriver.exe")
driver=webdriver.Firefox(service=service_obj)


driver.get("https://advisor360.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(2)
