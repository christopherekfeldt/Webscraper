import requests
from bs4 import BeautifulSoup
import smtplib
import json

with open("config.json") as config:
    data = json.load(config)

URL = 'https://www.pricerunner.se/pl/226-4474441/Golf/Callaway-Rogue-Fairway-Wood-priser'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find("div", class_="_3ua0LznGtn").get_text()
    price = soup.find("meta", itemprop="lowPrice")
    price = price["content"] if price else None
    price = int(price)
    print(title)
    print(price)

    if (price < 1500):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(data.get('server').get('username'), data.get('server').get('password'))

    subject = "The price fell down!"
    body = "Check the pricerunner link https://www.pricerunner.se/pl/226-4474441/Golf/Callaway-Rogue-Fairway-Wood-priser"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        data.get('server').get('username'),
        data.get('mail').get('sendTo'),
        msg
    )

    print('Hey email has been sent!')

    server.quit()


check_price()