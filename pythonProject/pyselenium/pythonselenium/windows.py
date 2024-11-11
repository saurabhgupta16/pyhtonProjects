import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(2)
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'Click Here').click()
windowOpen=driver.window_handles
driver.switch_to.window(windowOpen[1])
childText=(driver.find_element(By.TAG_NAME,'h3').text)
print(childText)
driver.close()
driver.switch_to.window(windowOpen[0])
parentText = driver.find_element(By.TAG_NAME,'h3').text
assert "Opening a new window" ==parentText
time.sleep(4)
