import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#Locator Id, Xpath ,CSS SElector , Class , Link Text
#Xapth   //tagname[@attribute='value']
#Css     tagname[attribute='value']

driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("saurabh")
driver.find_element(By.NAME, "email").send_keys("testSaurabh@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123345")
driver.find_element(By.CLASS_NAME,'form-check-input').click()

driver.find_element(By.XPATH,"//input[@type='submit']").click()
value=driver.find_element(By.CLASS_NAME,'alert-success').text
print(value)
assert "Succesdsdss" in value

time.sleep(5)