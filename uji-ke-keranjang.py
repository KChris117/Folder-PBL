from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

driver = webdriver.Chrome()

try:
    driver.get("http://localhost/PBL%20O'cos/masuk.php")
    time.sleep(3)

    nama_field = driver.find_element(By.XPATH, '//input[@name="nama"]')
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
    login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')

    nama = "tarissa"
    password = "tarissa"

    nama_field.send_keys(nama)
    time.sleep(3)
    password_field.send_keys(password)
    time.sleep(3)
    login_button.click()
    time.sleep(3)

    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(3)

    driver.get("http://localhost/PBL%20O'cos/barang.php")
    time.sleep(3)

    driver.get("http://localhost/PBL%20O'cos/beli.php?id_barang=5")
    time.sleep(3)

    current_url = driver.current_url

    if '/user/' in current_url:
        status = "succesful"
    elif '/' in current_url:
        status = "login gagal"
    else:
        status = "Failed (Unknown error)"

except Exception as e:
    status = "Gagal"
    print(f"Terjadi kesalahan: {e}")

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('uji-fungsionalitas.txt', 'a') as file:
    if "<h1>Internal Server Error</h1>" in driver.page_source:
        file.write(f"Fitur Login - Diuji pada: {current_datetime} - Status: Error - Internal Server Error\n")
    else:
        file.write(f"Fitur Login - Diuji pada: {current_datetime} - Status: {status}\n")



# Tutup browser
driver.quit()