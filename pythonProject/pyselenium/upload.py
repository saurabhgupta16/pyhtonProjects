import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
file_path = "C:\\Users\\saura\\Downloads\\download.xlsx"

driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.CSS_SELECTOR,"#downloadButton").click()

File_input=driver.find_element(By.CSS_SELECTOR,"input[type='file']")
File_input.send_keys(file_path)

toast_locator =(By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located(toast_locator))
toast_message=driver.find_element(*toast_locator).text
print(toast_message)
time.sleep(2)
