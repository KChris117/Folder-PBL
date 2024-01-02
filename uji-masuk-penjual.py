from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

login_url = 'http://127.0.0.1:9999/'
nama_penjual = 'onlinecosmetik'
password_penjual = 'onlinecosmetik'

driver = webdriver.Chrome()

driver.get(login_url)

nama_penjual_field = driver.find_element(By.XPATH, '//input[@name="nama_penjual"]')
password_penjual_field = driver.find_element(By.XPATH, '//input[@name="password_penjual"]')
masuk_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

time.sleep(2)
nama_penjual_field.send_keys(nama_penjual)
time.sleep(2)
password_penjual_field.send_keys(password_penjual)
time.sleep(2)
masuk_button.click()

time.sleep(2)

current_url = driver.current_url

if '/dashboard' in current_url:
    status = "Successful"
elif '/' in current_url:
    status = "Gagal Masuk"
else:
    status = "Failed (Unknown error)"

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('uji-fungsionalitas.txt', 'a') as file:
    if '<h1>Internal Server Error</h1>' in driver.page_source:
        file.write(f"Fitur Login - Diuji pada: {current_datetime} - Status: Error - Internal Server Error\n")
    else:
        file.write(f"Fitur Login - Diuji pada: {current_datetime} - Status: {status}\n")