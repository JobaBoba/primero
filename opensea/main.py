import requests
import json
import os

# Ваш ключ API
api_key = 'e0869ba5c5f746f2bfd5274efc0d02ca'

# Название коллекции
collection_slug = 'anatoli-georgievich-bogdanov'

# URL API
url = f"https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=20&collection={collection_slug}"

# Заголовки запроса
headers = {
    "Accept": "application/json",
    "X-API-KEY": api_key,
}

# Отправляем запрос
response = requests.request("GET", url, headers=headers)

# Проверяем статус ответа
if response.status_code == 200:
    # Преобразуем ответ в JSON
    data = json.loads(response.text)

    # Создаем папку для сохранения данных, если она еще не существует
    if not os.path.exists('data'):
        os.makedirs('data')

    # Сохраняем данные в файл JSON
    with open(f'data/{collection_slug}.json', 'w') as f:
        json.dump(data, f)
else:
    print(f"Ошибка: {response.status_code}")
