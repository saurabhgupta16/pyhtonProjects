import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

option=webdriver.ChromeOptions()
option.add_argument("start-maximized")
driver = webdriver.Chrome(options=option)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
items = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for item in items:
    Phone=item.find_element(By.XPATH,"div/h4/a").text
    if Phone=='Blackberry':
        item.find_element(By.XPATH,"div/button").click()
        break

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("ind")
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()

driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
message=driver.find_element(By.CLASS_NAME,'alert-success').text
print
assert "Success! Thank you!" in message
driver.close()

