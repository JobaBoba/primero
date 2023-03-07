import requests
from bs4 import BeautifulSoup

url = input("Введите URL страницы: ")

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

category = soup.find('span', {'class': 'grey dove-text', 'data-t': 'details-panel-category-text'})
if category:
    category = category.text.strip()

license_type = soup.find('span', {'class': 'grey dove-text', 'data-t': 'details-panel-license-type-text'})
if license_type:
    license_type = license_type.text.strip()

similar_keywords = []
for div in soup.find_all('div', {'class': 'keyword-badge-details-panel'}):
    keyword = div.find('a').text.strip()
    similar_keywords.append(keyword)

print("CATEGORY:", category)
print("LICENSE TYPE:", license_type)
print("SIMILAR KEYWORDS:", ", ".join(similar_keywords))
