import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def top_sellers():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }
    url = 'https://store.steampowered.com/search/?filter=topsellers&os=win'

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    top_sellers = soup.findAll('a', attrs={'class': 'search_result_row'})
    return render_template('grid_template.html', top_sellers=top_sellers)

if __name__ == '__main__':
    app.run(debug=True)

# print(top_sellers)
# for top_seller in top_sellers:
#     print('Title', top_seller.find('span', attrs={'class': 'title'}).text)
#     print('Images', top_seller.find('div', attrs={'class': 'search_capsule'}).find('img'))
# #     print('Tags', top_seller.find('div', attrs={'class': 'tab_item_top_tags'}).text)
# #     print('-' * 22)
