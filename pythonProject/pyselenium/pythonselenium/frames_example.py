import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
print("0")
driver.switch_to.frame("mce_0_ifr")
print("1")
driver.find_element(By.CSS_SELECTOR,'#tinymce').clear()
driver.find_element(By.CSS_SELECTOR,"#tinymce").send_keys("Ia m here ")

content=driver.find_element(By.TAG_NAME,'h3').text

print(content)
2


time.sleep(4)