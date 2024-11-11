import time
from selenium import webdriver
from selenium.webdriver.common.by import By
name="saurabh"
name1="Gupta"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)

assert name in alertText
alert.accept()
time.sleep(5)

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name1)
driver.find_element(By.CSS_SELECTOR,"#confirmbtn").click()
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(5)
