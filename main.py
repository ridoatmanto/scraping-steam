import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
}
url = 'https://store.steampowered.com/'
r = requests.get(url, headers=headers)
print(r)
