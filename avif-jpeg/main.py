from PIL import Image

# Открываем исходный файл в формате AVIF
with Image.open('zebra.avif') as im:
# Конвертируем в формат JPEG с качеством 90%
im.convert('RGB').save('output.jpg', quality=90)