from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    #вводим ответ в текстовое поле
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    #скроллим страницу
    browser.execute_script("window.scrollBy(0, 100);")

    #включаем чекбокс
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    
    #включаем радиобаттон
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
