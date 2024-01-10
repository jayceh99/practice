
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

driver.get("https://irs.thsrc.com.tw/IMINT/")
driver.find_element(By.CSS_SELECTOR , value='#cookieAccpetBtn').click()
time.sleep(2)
driver.find_element(By.XPATH, value="//input[@readonly='readonly'] ").click()
time.sleep(2)
driver.find_element(By.XPATH, value='//span[@aria-label="一月 31, 2024"]').click()
time.sleep(2)
  
