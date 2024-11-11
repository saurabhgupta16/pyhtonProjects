import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for check in checkboxes:
    if check.get_attribute("value")=="option2":
        check.click()
        assert check.is_selected()
        break


time.sleep(5)