from selenium import webdriver 
import time

# Инициализируем драйвер Chrome
driver = webdriver.Chrome()

# Открываем сайт Microsoft
driver.get("https://www.microsoft.com/ru-ru/microsoft-365/microsoft-office")

# Ждем, чтобы страница загрузилась
time.sleep(5)

# Находим выпадающий список "Продукты Майкрософт" и кликаем по нему
mic = driver.find_element("xpath", '//*[@id="uhf-c-nav"]/ul/li/div/button/span')
mic.click()

time.sleep(5)

# Находим вкладку "Образование" и кликаем по ней
mic = driver.find_element("xpath", '//*[@id="shellmenu_112"]')
mic.click()

# Ждем, чтобы страница загрузилась
time.sleep(5)

# Пролистываем страницу до конца с помощью JavaScript
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Ждем, чтобы страница прокрутилась
time.sleep(5)

# Находим вкладку "Контактная информация" и кликаем по ней
mic = driver.find_element("xpath", '//*[@id="c-uhff-footer_contactus"]/a')
mic.click()

# Ждем, чтобы страница загрузилась
time.sleep(5)

# Закрываем браузер
driver.quit()