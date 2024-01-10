
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://irs.thsrc.com.tw/IMINT/")
driver.find_element(by=By.ID , value='cookieAccpetBtn').click()
time.sleep(2)
driver.find_element(By.XPATH, value="//input[@type='text'] ").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".open .dayContainer:nth-child(1) > .flatpickr-day:nth-child(12)").click()
time.sleep(10)
  
