import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/OnePlus-Nord-Lite-128GB-Storage/dp/B09WQYFLRX/ref=sr_1_3?crid=17X02WLCUUC24&keywords=oneplus&qid=1674654638&sprefix=oneplus%2Caps%2C219&sr=8-3&th=1'

headers = {"user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
title = soup.find(id='productTitle').get_text()
print(title)
price = soup.find(class_name='a-price-whole').title()
print(price)

