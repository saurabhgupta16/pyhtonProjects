import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.implicitly_wait(3)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,'tinymce').clear()
driver.find_element(By.ID,'tinymce').send_keys("Ia am here to learn this time")
driver.switch_to.default_content()
headertext=driver.find_element(By.XPATH,'//h3').text
print(headertext)