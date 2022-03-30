from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv


# write scraped data as csv file
response = urlopen('https://www.premierleague.com/tables')
soup = BeautifulSoup(response, 'html.parser')
i = 1
l = 22
file = open("pl_standings.csv", 'w')
writer = csv.writer(file)

# write title row
writer.writerow(['position', 'club_name', 'points'])

tags = ['span', 'td']
classes = ['value', 'long', 'points']
scraper = soup.find_all(tags, attrs={'class': classes})

for standing in scraper:
    position = soup.find('span', {'class': 'value'}).string
    club_name = soup.find('span', {'class': 'long'}).string
    points = soup.find('td', {'class': 'points'}).string
    i = i + 1
    if i == l:
        break

    writer.writerow([position, club_name, points])

# data = [str(standing) for standing in scraper]
# writer.writerow([data])
file.close()

