from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from math import log, sin

# Определяем функцию для расчета капчи
def calc(x):
    return str(log(abs(12 * sin(float(x)))))

try:
    # Инициализация драйвера и открытие страницы
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    
    # Ждём загрузки кнопки и нажимаем её
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    ).click()
    
    # Переключаемся на новую вкладку
    windows = browser.window_handles
    if len(windows) > 1:
        new_window = windows[-1]
        browser.switch_to.window(new_window)
    else:
        raise Exception("Новая вкладка не открылась")
    
    # Решаем капчу
    input_value = browser.find_element(By.ID, 'input_value').text
    result = calc(input_value)
    
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(result)
    
    # Отправляем ответ
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit_button.click()
    
    # Читаем результат из Alert'a
    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    print("Ваш ответ:", alert.text.split()[-1])
    alert.accept()

finally:
    # Закрываем браузер после завершения работы
    time.sleep(5)
    browser.quit()