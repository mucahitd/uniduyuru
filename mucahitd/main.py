from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import tweepy

consumer_key = "sizin uygulama bilgileriniz"
consumer_secret = "sizin uygulama bilgileriniz"
access_token = "sizin uygulama bilgileriniz"
access_token_secret = "sizin uygulama bilgileriniz"
giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)
api = tweepy.API(giris)

url = "http://tek.firat.edu.tr/tr/duyurular/"
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
for item in soup.select("#content .field-content a"):
    link = urljoin(url, item['href'])
    api.update_status(status="Başlık: {}\nLink: {}\n".format(item.text, link))
    break
