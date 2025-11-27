from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

try:
    browser.get("https://suninjuly.github.io/selects1.html")  

    num1_element = browser.find_element(By.ID, "num1").text
    num2_element = browser.find_element(By.ID, "num2").text
    
    sum_result = int(num1_element) + int(num2_element)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_result))

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    submit_button.click()

    time.sleep(5)

finally:
    browser.quit()