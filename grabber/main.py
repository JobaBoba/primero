import requests
from bs4 import BeautifulSoup

# Запрос у пользователя URL страницы
url = input("Введите URL страницы: ")

# Загрузка страницы
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Поиск ключевых слов
keywords = []
for a in soup.find_all('a', {'class': 'keyword'}):
    keywords.append(a.text.strip())

# Вывод результатов
print(", ".join(keywords))
