import requests
from bs4 import BeautifulSoup
import pymongo


url = 'http://quotes.toscrape.com/'


def scraped_quotes():
    more_links = True
    page = 10
    quotes = []
    
    while more_links:
        response = requests.get(f"{url}page/{page}").text
        soup = BeautifulSoup(response, 'html.parser')
        for item in soup.select('.quote'):
            quote = {}
            quote['text'] = item.select_one('.text').get_text()
            quote['author'] = item.select_one('.author').get_text()
            tags = item.select_one('.tags')
            quote['tags'] = [tag.get_text() for tag in tags.select('.tag')]
            quotes.append(quote)
            
        next_link = soup.select('.next > a')
        
        # print which page was scraped
        print(f'scraped page {page}')

        # check if the next link element exists
        if(next_link):
            page += 1
        else:
            more_links = False
    return quotes

quotes = scraped_quotes()
client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client.db.Quotes


