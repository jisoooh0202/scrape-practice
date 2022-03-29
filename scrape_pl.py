from bs4 import BeautifulSoup
from urllib.request import urlopen

# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))

# write scraped data as txt file
response = urlopen('https://www.premierleague.com/tables')
soup = BeautifulSoup(response, 'html.parser')
i = 1
l = 22
f = open("pl_standings.txt", 'w')
for anchor in soup.select('span.long'):
    data = str(i) + ":" + anchor.get_text() + "\n"
    i = i + 1
    if i == l:
        break
    f.write(data)
f.close()

