import requests
from bs4 import BeautifulSoup
import time

# links = []

# for i in range(25):
#     url = 'http://example.python-scraping.com/places/default/index/' + str(i)
#     response = requests.get(url)
#     if response.ok:
#         print('Page' +str(i))
#         soup = BeautifulSoup(response.text, 'lxml')
#         tds = soup.findAll('td')
        
#         for td in tds:
#             a = td.find('a')
#             link = a['href']
#             links.append('http://example.python-scraping.com' + link)    
#         time.sleep(3)
        

# with open('urls.txt', 'w') as f:
#     for link in links:
#         f.write(link + "\n")


with open('urls.txt', 'r') as input_f:
    with open('countries.csv', 'w') as output_f:
        output_f.write('Country,Population\n')
        for row in input_f:
            url = row.strip()
            r = requests.get(url)
            if r.ok:
                soup = BeautifulSoup(r.text, 'lxml')
                country = soup.find('tr', {'id':'places_country_or_district__row'}).find('td', {'class': 'w2p_fw'})
                population = soup.find('tr', {'id':'places_population__row'}).find('td', {'class': 'w2p_fw'})
                print(f"Country: {country.text} - Population: {population.text}")
                output_f.write(country.text + ',' + population.text.replace(',', '') + '\n')
            time.sleep(3)