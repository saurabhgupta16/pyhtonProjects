from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.LINK_TEXT,'Top Deals').click()
openWindow = driver.window_handles
sortlist=[]
driver.switch_to.window(openWindow[1])
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
items=driver.find_elements(By.XPATH,"//tr/td[1]")
for item in items:
    sortlist.append(item.text)
print(sortlist)
original_list=sortlist.copy()
sortlist.sort()
print(sortlist)
print(original_list)
assert original_list==sortlist