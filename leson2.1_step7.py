from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    link = 'http://suninjuly.github.io/get_attribute.html'
    browser.get(link)

    wait = WebDriverWait(browser, 10)
    treasure_img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#treasure')))

    x_value = treasure_img.get_attribute('valuex')

    result = calc(x_value)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(result)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit_button.click()

finally:
    time.sleep(10) 
    browser.quit()