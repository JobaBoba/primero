from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Запрос у пользователя URL страницы
url = input("Введите URL страницы: ")

# Создание экземпляра браузера Chrome
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Опционально: запустить браузер в фоновом режиме
driver = webdriver.Chrome(options=options)

# Загрузка страницы
driver.get(url)

# Запись содержимого страницы в файл
filename = input("Введите имя файла для сохранения: ")
with open(filename, 'w', encoding='utf-8') as f:
    f.write(driver.page_source)

# Поиск слова на странице
search_word = input("Введите слово для поиска: ")
if search_word in driver.page_source:
    print("Слово найдено на странице")
else:
    print("Слово не найдено на странице")

# Закрытие браузера
driver.quit()
