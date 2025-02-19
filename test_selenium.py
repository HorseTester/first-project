from selenium import webdriver
import time

# Укажите путь к исполняемому файлу Chrome для тестирования
chrome_binary_path = r"C:\Users\rodio\OneDrive\Рабочий стол\Системная\chrome-win64\chrome.exe"

# Создайте объект ChromeOptions и укажите путь к исполняемому файлу
options = webdriver.ChromeOptions()
options.binary_location = chrome_binary_path

# Инициализируйте драйвер Chrome с использованием ChromeOptions
driver = webdriver.Chrome(options=options)

# Открытие веб-страницы
driver.get("https://www.ya.ru")

# Задержка в 5 секунд
time.sleep(5)

# Закрытие браузера
driver.quit()
