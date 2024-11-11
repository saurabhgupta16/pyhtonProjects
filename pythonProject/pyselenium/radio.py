import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radiobutton= driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobutton[1].click()
assert radiobutton[1].is_selected()


