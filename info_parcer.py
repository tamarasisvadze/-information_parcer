from bs4 import BeautifulSoup
import requests
import csv
from time import sleep
from random import randint


file = open('posters.csv', 'w',encoding='utf-8_sig', newline = '\n')
f_object = csv.writer(file)
f_object.writerow(['Title','Author','Price'])


h = {'Accept-Language':'en-US'}
p = 1

url = 'https://fineartamerica.com/art/vintage+fashion?start= ' +str(p)
while p < 16:
    respo = requests.get(url,headers = h)
    content = respo.text
    soup = BeautifulSoup(content,'html.parser')
    section = soup.find('div',id='imageFlowContainerDiv')

    poster = section.find_all('div',class_ = 'flowDiv')

    for each in poster:
        title = each.find('p',class_='flowArtworkName').text
        author = each.find('p',class_='flowArtistName').text
        price = each.find('p',class_='flowProductPrice').text
        
        f_object.writerow([title,author,price])

    p += 1
    sleep(randint(10,15))


