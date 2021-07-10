import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
}
url = 'https://store.steampowered.com/'
r = requests.get(url, headers=headers)
# print(r)
soup = BeautifulSoup(r.text, 'html.parser')
steams = soup.findAll('div', attrs={'class': 'carousel_items'})

for steam in steams:
    print(steam)
