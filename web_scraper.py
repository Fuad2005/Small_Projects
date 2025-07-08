from bs4 import BeautifulSoup
import requests
import pandas as pd


df = pd.DataFrame(columns=['Title', 'Doze', 'Type','Price'])

html = requests.get('https://www.opensourcesports.com/')
s = BeautifulSoup(html.content, 'html.parser')

container = s.find(id='main')
cont1 = container.find_all('div', class_='column four centertxt')

for el in cont1:
    text = str(el.find('h3'))
    text_l = text.split('<br/>')
    title = text_l[2][:-5]
    doze = text_l[1]
    type = text_l[0][4:]
    price = el.find('p').find('span').text
    df = df._append({'Title': title, 'Doze': doze, 'Type': type, 'Price': price}, ignore_index=True)


print(df)
    

