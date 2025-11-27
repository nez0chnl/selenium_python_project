from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# Функция расчета значения выражения log(abs(12 * sin(x)))
def calc(x):
    return str(math.log(abs(12 * math.sin(float(x)))))

try:
    # Инициализация драйвера браузера Chrome
    browser = webdriver.Chrome()

    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    wait = WebDriverWait(browser, 10)
    x_element = wait.until(EC.visibility_of_element_located((By.ID, "input_value")))
    x = x_element.text

    result = calc(x)

    answer_input = wait.until(EC.presence_of_element_located((By.ID, "answer")))
    browser.execute_script("arguments[0].scrollIntoView();", answer_input)

    answer_input.clear()
    answer_input.send_keys(result)

    checkbox = wait.until(EC.element_to_be_clickable((By.ID, "robotCheckbox")))
    checkbox.click()
    
    robots_rule_radio = wait.until(EC.element_to_be_clickable((By.ID, "robotsRule")))
    robots_rule_radio.click()

    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))
    submit_button.click()

    time.sleep(10)
    
finally:
    # Закрываем браузер
    browser.quit()