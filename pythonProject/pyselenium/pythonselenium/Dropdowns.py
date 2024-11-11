import time
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
#Static Drop down
""" 
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
dropdown = Select(driver.find_element(By.CSS_SELECTOR,'#exampleFormControlSelect1'))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)
"""

#Dynamic Auto suggestive

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.CSS_SELECTOR,"#autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']")
for country in countries:
    if country.text=="India":
        country.click()
        break
print(len(countries))

assert driver.find_element(By.CSS_SELECTOR,"#autosuggest").get_attribute("value")=="India"


time.sleep(5)