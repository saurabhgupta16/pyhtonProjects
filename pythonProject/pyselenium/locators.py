import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# id , name , Class , CSSelector, Xpath , Linktext
# Xpath //tagname[@attribute='value']
# Css  tagname[attribute='value']
# css #id .classname
driver.find_element(By.NAME,"email").send_keys("ab2@test.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
driver.find_element(By.XPATH,"//input[@name='name']").send_keys("saurabh")
driver.find_element(By.CSS_SELECTOR,"input[name='bday']").send_keys('10/16/1982')
driver.find_element(By.XPATH,"//input[@value='option1']").click()
message=driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

assert  "success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("hello")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()






time.sleep(3)