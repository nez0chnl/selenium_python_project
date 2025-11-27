from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    
    y = calc(x)
    
    input_field = browser.find_element(By.ID, 'answer')
    input_field.send_keys(y)
    
    option_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    option_checkbox.click()
    
    robots_rule_radio = browser.find_element(By.ID, 'robotsRule')
    robots_rule_radio.click()
    
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    submit_button.click()
    
finally:
    time.sleep(10)
    browser.quit()