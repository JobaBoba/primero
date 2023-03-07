import requests

# Запрос у пользователя URL страницы
url = input("Введите URL страницы: ")

# Загрузка страницы
response = requests.get(url)
content = response.content

# Подсчет символов
num_chars = len(content)

# Вывод результатов
print(f"Количество символов на странице {url}: {num_chars}")
