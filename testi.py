import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Или другой браузер, если нужен

    def tearDown(self):
        self.browser.quit()

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.browser.get(link)
        
        # Используем явные ожидания для всех полей
        input1 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".first_block .form-control.first"))
        )
        input1.send_keys("Ivan")
        
        input2 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".first_block .form-control.second"))
        )
        input2.send_keys("Petrov")
        
        input3 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".first_block .form-control.third"))
        )
        input3.send_keys("example@example.com")
    
        # Отправим заполненную форму
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))
        )
        button.click()
    
        # Ждём появления текста приветствия
        welcome_text = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        ).text
    
        # Проверяем результат регистрации
        self.assertEqual("Поздравляем! Вы успешно зарегистрировались!", welcome_text, "Регистрация прошла неудачно")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.browser.get(link)
        
        # Используем явные ожидания для всех полей
        input1 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".first_block .form-control.first"))
        )
        input1.send_keys("Ivan")
        
        input2 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".first_block .form-control.second"))
        )
        input2.send_keys("Petrov")
        
        input3 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".first_block .form-control.third"))
        )
        input3.send_keys("example@example.com")
    
        # Отправим заполненную форму
        button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))
        )
        button.click()
    
        # Ждём появления текста приветствия
        welcome_text = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        ).text
    
        # Проверяем результат регистрации
        self.assertEqual("Поздравляем! Вы успешно зарегистрировались!", welcome_text, "Регистрация прошла неудачно")

if __name__ == "__main__":
    unittest.main()