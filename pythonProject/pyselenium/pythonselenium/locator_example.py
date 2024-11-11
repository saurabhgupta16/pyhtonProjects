import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#//tagname[@attribute="Value"]
#tagname[attribute='Value']
# #id .Class for Selector.
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"name").send_keys("saurabh")
driver.find_element(By.NAME,"email").send_keys("test@test.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys('111111')
driver.find_element(By.CLASS_NAME,"form-check-input").click()
driver.find_element(By.XPATH,"//input[@id='inlineRadio2']").click()
driver.find_element(By.XPATH,"//input[@name='bday']").send_keys("12/12/2012")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

message = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
print(message)
assert "submitted" in message
time.sleep(5)