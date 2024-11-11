import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
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
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
message = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
assert "Code" in message
print(message)
