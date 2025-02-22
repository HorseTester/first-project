from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Указываем путь к chromedriver.exe
driver_path = r"C:\Users\rodio\OneDrive\Рабочий стол\Python\chromedriver.exe"

# Создаем объект Service для указания пути к chromedriver
service = Service(executable_path=driver_path)

# Инициализируем драйвер Chrome с использованием объекта Service
driver = webdriver.Chrome(service=service)

# Открытие веб-страницы
driver.get("https://www.ya.ru")

# Задержка в 5 секунд
time.sleep(5)

# Закрытие браузера
driver.quit()