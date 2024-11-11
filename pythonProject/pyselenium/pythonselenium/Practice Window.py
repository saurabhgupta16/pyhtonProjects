from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/#")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR,'.blinkingText').click()
openWindow=driver.window_handles
driver.switch_to.window(openWindow[1])
content=driver.find_element(By.XPATH,"//p[@class='im-para red']").text
print(content)
Var=content.split(" ")
print(Var)
for x in Var:
    if x=="mentor@rahulshettyacademy.com":
        y="mentor@rahulshettyacademy.com"
        break
driver.close()
driver.switch_to.window(openWindow[0])
driver.find_element(By.CSS_SELECTOR,'#username').send_keys(y)
driver.find_element(By.ID,'password').send_keys(1234)
driver.find_element(By.Id,'signInBtn').click()
