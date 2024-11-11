import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(3)
driver.maximize_window()

driver.switch_to.frame("courses-iframe")
driver.find_element(By.LINK_TEXT,"Courses").click()
driver.switch_to.default_content()
driver.refresh()

time.sleep(3)