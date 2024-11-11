import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#autosuggest").send_keys("ind")
time.sleep(3)
countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

#Valdiate if India is selected.

selectedCountry=driver.find_element(By.CSS_SELECTOR,"#autosuggest").get_attribute('value')
print(selectedCountry)
assert selectedCountry=="India"