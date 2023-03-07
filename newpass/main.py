import random
import string

while True:
    try:
        cod = int(input('Введите количество символов для пароля: '))
        if cod < 8:
            print('Количество символов должно быть не менее 8.')
            continue
        break
    except ValueError:
        print('Количество символов должно быть целым числом.')

a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
d = '[]{}()*!,./@#$%^&<>:";-_?'
res = a + b + c + d
password = ''.join(random.choices(res, k=cod))

print('Пароль из', str(cod), 'символов:', password)
