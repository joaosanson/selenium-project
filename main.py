from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser = Service("C:\Development\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.click()
first_name.send_keys("Your First Name")

last_name = driver.find_element(By.NAME, "lName")
last_name.click()
last_name.send_keys("Your Last Name")

email = driver.find_element(By.NAME, "email")
email.click()
email.send_keys("Your Email")

sign_up = driver.find_element(By.TAG_NAME, "button")
sign_up.click()