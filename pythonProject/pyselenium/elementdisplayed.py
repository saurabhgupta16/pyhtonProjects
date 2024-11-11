import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

assert  driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert  driver.find_element(By.CSS_SELECTOR,"#displayed-text").is_displayed()
