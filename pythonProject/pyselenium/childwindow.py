from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#action clas Handle all Advacnced Action such as Double click , Hover over or right click
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowOpen = driver.window_handles
driver.switch_to.window(windowOpen[1])
childText = driver.find_element(By.XPATH,"//h3").text
print(childText)
driver.close()
driver.switch_to.window(windowOpen[0])
parentext = driver.find_element(By.XPATH,"//h3").text
print(parentext)
