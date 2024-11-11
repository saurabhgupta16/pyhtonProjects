import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)
items = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(items)
print(count)
assert count > 0
for item in items:
    item.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
#Sum Validation of Items
prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
totalamount = 0
for price in prices:
    totalamount = totalamount + int(price.text)
print(totalamount)

totamt=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert totalamount == totamt


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
message = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
assert "Code" in message
print(message)
