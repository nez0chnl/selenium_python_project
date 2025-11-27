import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/find_link_text'
browser.get(url)
try:
    secret_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    print("Зашифрованный текст:", secret_text)

    link = browser.find_element(By.LINK_TEXT, secret_text)
    link.click()
    time.sleep(0.1)

    first_name_input = browser.find_element(By.NAME, 'first_name')
    first_name_input.send_keys('Nz')
    time.sleep(0.1)

    last_name_input = browser.find_element(By.NAME, 'last_name')
    last_name_input.send_keys('Nez')
    time.sleep(0.1)

    city_input = browser.find_element(By.NAME, 'firstname')
    city_input.send_keys('OtsoCity')
    time.sleep(0.1)

    city_input = browser.find_element(By.ID, 'country')
    city_input.send_keys('OtsoCity')
    time.sleep(0.1)


    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()
    time.sleep(1)

finally:

    time.sleep(30)
    browser.quit()