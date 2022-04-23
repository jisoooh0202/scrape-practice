from bs4 import BeautifulSoup
import requests
import lxml
import csv


url = 'https://www.premierleague.com/tables'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

standings = soup.find('div', attrs={'data-ui-tab': 'First Team'}).find_all('tr')[1::2]
print(standings)

file = open("pl_standings.csv", 'w')
writer = csv.writer(file)

writer.writerow(['position', 'club_name', 'points'])

for standing in standings:
    position = standing.find('span', attrs={'class': 'value'}).text.strip()
    club_name = standing.find('span', {'class': 'long'}).text
    points = standing.find('td', {'class': 'points'}).text

    print(position, club_name, points)

    writer.writerow([position, club_name, points])

file.close()

