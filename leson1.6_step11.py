from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        
        # Находим элементы по уникальным признакам
        first_name_input = browser.find_element(By.XPATH, '//div/input[@placeholder="Input your first name"]')
        last_name_input = browser.find_element(By.XPATH, '//div/input[@placeholder="Input your last name"]')
        email_input = browser.find_element(By.XPATH, '//div/input[@placeholder="Input your email"]')
        
        # Заполняем поля
        first_name_input.send_keys('Ivan')
        last_name_input.send_keys('Petrov')
        email_input.send_keys('ivan.petrov@example.com')
        
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # Ждём загрузки страницы
        time.sleep(1)
        
        # Проверяем наличие нужного текста на странице
        welcome_text_elm = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elm.text
        
        assert "Congratulations! You have successfully registered!" == welcome_text, f"Expected congratulation message, got {welcome_text}"
    
    finally:
        # Завершаем сессию браузера
        browser.quit()

if __name__ == "__main__":
    links = [
        "http://suninjuly.github.io/registration1.html",
        "http://suninjuly.github.io/registration2.html"
    ]
    
    for link in links:
        print(f"\nTesting page: {link}")
        test_registration(link)