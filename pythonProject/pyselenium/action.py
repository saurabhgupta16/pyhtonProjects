from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#action clas Handle all Advacnced Action such as Double click , Hover over or right click
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(4)
driver.maximize_window()
action = ActionChains(driver)
#rightclick
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
