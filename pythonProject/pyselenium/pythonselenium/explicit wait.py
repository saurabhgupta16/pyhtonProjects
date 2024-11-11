import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
expected_items=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
actual_items=[]
driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert count > 0
for result in results:
    actual_items.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()

assert actual_items==expected_items
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
#time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promocode").send_keys("rahulshettyacademy")

# total Sum of the item

amounts=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)

totalAmt= int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
print(sum)
print(totalAmt)
assert sum == totalAmt

#


driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
mess=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
assert "Code" in mess


discountAmt = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(discountAmt)
assert totalAmt > discountAmt

