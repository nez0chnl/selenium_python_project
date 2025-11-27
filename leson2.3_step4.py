from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

try:

    browser.get('http://suninjuly.github.io/alert_accept.html')

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'input_value'))
    )
    x = int(x_element.text)
    y = calc(x)

    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit_button.click()
 
    final_alert = browser.switch_to.alert
    answer_text = final_alert.text.split(':')[-1].strip()
    print(answer_text)
    time.sleep(10)
finally:

    browser.quit()