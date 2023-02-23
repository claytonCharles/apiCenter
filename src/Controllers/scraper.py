import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import io

def ScraperOlx(search, pages):
    myHeaders = {
        "method": "GET",
        "scheme": "https",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    }
    jsonData = []
    search = f'&q={search}'
    for i in range(pages):
        try:
            count = i + 1
            page = f'&o={count}'
            r = requests.get(f"http://www.olx.com.br/estado-df?{search}{page}", headers=myHeaders)
            soup = bs(r.text , 'html.parser')
            li = soup.find_all('li', {'class': 'sc-1fcmfeb-2'})
            count = 0
            for bloco in li:
                try:
                    jsonData.append({
                        'item': bloco.find('h2', {'class': 'kgl1mq-0'}).text,
                        'preco': bloco.find('span', {'class': 'm7nrfa-0'}).text,
                        'link': bloco.find('a', {'class' : 'sc-12rk7z2-1'})['href']
                        })
                    count += 1
                except:
                    pass

        except:
            pass
    return jsonData

def TableXlsx(data):
    itens = []
    precos = []
    links = []
    for row in data:
        itens.append(row['item'])
        precos.append(row['preco'])
        links.append(row['link'])
    table = pd.DataFrame( { 'Item': itens, 'Preço': precos, 'Link': links } )
    by = io.BytesIO()
    table.to_excel(by)

    return by.getvalue()