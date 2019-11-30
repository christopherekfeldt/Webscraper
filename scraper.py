import requests
from bs4 import BeautifulSoup

URL = 'https://www.pricerunner.se/pl/94-4972002/Hoerlurar-och-Gaming-Headsets/Sony-WF-1000XM3-priser'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find("span", itemprop="name")
price = soup.find(id="national_offers")


print(title)
#print(price)

nickname = soup.find('span', class_ = "_1jlH40g035 _2Boi0NFO-E").get_text()

print(nickname)