import socks
import socket
import requests

# Функция для проверки прокси-сервера
def check_proxy(proxy):
    try:
        socks.set_default_proxy(socks.SOCKS5, proxy.split(':')[0], int(proxy.split(':')[1]))
        socket.socket = socks.socksocket
        response = requests.get("https://www.google.com/", timeout=5)
        return response.status_code == 200
    except:
        return False

# Открываем файл со списком прокси-серверов
with open("proxy_list.txt") as f:
    with open("proxy-ok.txt", "w") as f_ok:
        for line in f:
            # Получаем IP-адрес и порт прокси-сервера
            proxy = line.split()[0]
            # Проверяем прокси-сервер и записываем в файл, если работает
            if check_proxy(proxy):
                f_ok.write(proxy + "\n")
                print(proxy + " is working and added to proxy-ok.txt")
            else:
                print(proxy + " is not working")