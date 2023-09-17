import requests
import json
from datetime import datetime

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

    # Получаем текущее время в формате UNIX timestamp
    current_time = datetime.now().timestamp()

    # Получаем список объектов со статусом "List Expired"
    expired_listings = [asset for asset in data['assets'] if 'sell_orders' in asset and asset['sell_orders'] and float(
        asset['sell_orders'][0]['expiration_time']) < current_time]

    # Выводим имена объектов со статусом "List Expired"
    for asset in expired_listings:
        print(asset['name'])
else:
    print(f"Ошибка: {response.status_code}")
