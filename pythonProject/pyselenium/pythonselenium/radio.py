import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

radios= driver.find_elements(By.XPATH,"//input[@class='radioButton']")
for radio in radios:
    if radio.get_attribute("value") == "radio2":

        radio.click()
        assert radio.is_selected()
        break

time.sleep(5)
