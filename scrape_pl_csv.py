from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv


# write scraped data as csv file
response = urlopen('https://www.premierleague.com/tables')
soup = BeautifulSoup(response, 'html.parser')
file = open("pl_standings.csv", 'w')
writer = csv.writer(file)

# write title row
writer.writerow(['position', 'club_name', 'points'])

tags = ['span', 'td']
classes = ['value', 'long', 'points']
standings = soup.find_all(tags, attrs={'class': classes}, limit=20)
# standings = soup.find_all('tr')
# standings = soup.find('tbody', attrs={'class': 'tableBodyContainer isPL'}).find_all('tr', attrs={'data-compseason': '418'}, recursive=False)

print(standings)
# below code gives only the first place of table repeatedly.
for standing in standings:
    position = soup.find('span', {'class': 'value'}).string
    club_name = soup.find('span', {'class': 'long'}).string
    points = soup.find('td', {'class': 'points'}).string

    print(position, club_name, points)

    writer.writerow([position, club_name, points])

# below code gives only the first place.
# for standing in standings:
#     position = standing.find('span', {'class': 'value'}).text
#     club_name = standing.find('span', {'class': 'long'}).text
#     points = standing.find('td', {'class': 'points'}).text
#
#     print(position, club_name, points)
#
#     writer.writerow([position, club_name, points])

# below code gives all the tag and classes together.
# data = [str(standing) for standing in standings]
# print(data)
# writer.writerow(data)

# below code gives not in list of three.
# for standing in standings:
#     data = standing.contents
#     print(data)
#     writer.writerow(data)


# string/get_text() are giving commas between each letter.
# for standing in standings:
#     data = standing.string
#     print(data)
#     writer.writerow(data)

file.close()

