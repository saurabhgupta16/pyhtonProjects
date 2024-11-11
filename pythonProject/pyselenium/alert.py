import time

from selenium import webdriver
from selenium.webdriver.common.by import By
name = "saurabh"
name1= "pearl"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
alert = driver.switch_to.alert

alerttext = alert.text
print(alerttext)
assert name in alerttext
alert.accept()
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name1)
driver.find_element(By.ID,"confirmbtn").click()
secondalert = driver.switch_to.alert
secondtext=secondalert.text
print(secondtext)
assert name1 in secondtext
time.sleep(2)
secondalert.dismiss()



time.sleep(3)