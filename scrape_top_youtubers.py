from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import csv

# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))

# write scraped data as csv file
url = 'https://socialblade.com/youtube/top/100/mostsubscribed'
page = requests.get(url, headers={'User-Agent': 'your user agent'})
soup = BeautifulSoup(page.content, 'html.parser')

channels = soup.find('div', attrs={'style': 'float: right; width: 900px;'}).find_all('div', recursive=False)[4:]

file = open("top_youtubers.csv", 'w')
writer = csv.writer(file)

writer.writerow(['Username', 'Uploads', 'Subscribers', 'Views'])

for channel in channels:
    username = channel.find('a').text.strip()
    uploads = channel.find('div', attrs={'style': 'float: left; width: 80px;'}).span.text.strip()
    subs = channel.find_all('div', attrs={'style': 'float: left; width: 150px;'})[0].text.strip()
    views = channel.find_all('div', attrs={'style': 'float: left; width: 150px;'})[1].span.text.strip()

    print(username + '' + uploads + '' + subs + '' + views)
    writer.writerow([username, uploads, subs, views])
file.close()

