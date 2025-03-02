from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# Инициализируем драйвер Chrome
driver = webdriver.Chrome()

try:
    # Открываем тестовый сайт
    driver.get("https://demoqa.com/automation-practice-form")

    # Заполняем имя
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("Иван")

    # Заполняем фамилию
    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Иванов")

    # Заполняем email
    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("ivan@example.com")

    # Выбираем пол (радиокнопка)
    gender = driver.find_element(By.XPATH, '//label[contains(text(), "Male")]')
    gender.click()

    # Заполняем номер телефона
    phone = driver.find_element(By.ID, "userNumber")
    phone.send_keys("1234567890")

    # Выбираем дату рождения
    dob = driver.find_element(By.ID, "dateOfBirthInput")
    dob.click()
    month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
    month.select_by_visible_text("January")
    year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
    year.select_by_visible_text("1990")
    day = driver.find_element(By.XPATH, '//div[contains(@class, "react-datepicker__day") and text()="1"]')
    day.click()

    # Выбираем предметы (чекбоксы)
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Maths")
    subjects.send_keys(Keys.RETURN)

    # Загружаем файл
    upload_file = driver.find_element(By.ID, "uploadPicture")
    upload_file.send_keys("C:/Users/rodio/Onedrive/Рабочий стол/Обмен/Demo.bmp")

    # Отправляем форму
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # Ждем, чтобы увидеть результат
    time.sleep(5)

except Exception as e:
    print("Произошла ошибка:", e)

finally:
    # Закрываем браузер
    driver.quit()