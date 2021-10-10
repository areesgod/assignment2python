
from bs4 import BeautifulSoup
import requests

class List:
    def Paragraph(self, text):
        url = 'https://www.google.com/search?q=site:https://coinmarketcap.com/+' + text + '&num=20'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        for g in soup.find_all('h3'):
            print(g.text)
            print('-----')
    def __init__(self,text):
        self.text = text
