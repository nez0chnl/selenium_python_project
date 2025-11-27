from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    
    
    elements = browser.find_elements(By.TAG_NAME, "input")  # Найдем все элементы типа input
    
    for element in elements:
        if element.is_displayed():
            element.send_keys("Nz")
            
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Ждём 30 секунд чтобы успеть скопировать код ссылки
    time.sleep(30)
    # Закрываем браузер
    browser.quit()