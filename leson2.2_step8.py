from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


with open('test.txt', 'w'):
    pass 

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first_name_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, "firstname"))
    )
    last_name_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, "lastname"))
    )
    email_field = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )

    first_name_field.send_keys("Иван")
    last_name_field.send_keys("Иванов")
    email_field.send_keys("ivanov@example.com")

    choose_file_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "file"))
    )
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    choose_file_button.send_keys(file_path)

    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()

    time.sleep(5)
    alert = browser.switch_to.alert
    result_number = alert.text.split()[-1]
    print(result_number)
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()