from selenium import webdriver  # Драйвер дб добавлен в PATH
import time
from selenium.webdriver.common.keys import Keys

# Инициализируем драйвер Chrome
driver = webdriver.Chrome()

# Открытие веб-страницы
driver.get("https://www.ya.ru")

# Поиск элемента через XPath
element = driver.find_element("xpath", "//input[@id='text']")

# Вводим текст в поле поиска
element.send_keys("Python")

# Нажимаем Enter
element.send_keys(Keys.RETURN)

# Задержка
time.sleep(10)

# Закрытие браузера
driver.quit()