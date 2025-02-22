from selenium import webdriver # Драйвер дб добавлен в PATH!!!
import time

# Инициализируем драйвер Chrome
driver = webdriver.Chrome()

# Открытие веб-страницы
driver.get("https://www.ya.ru")

# Задержка в 5 секунд
time.sleep(5)

# Закрытие браузера
driver.quit()