import requests
from bs4 import BeautifulSoup

baseurl = "https://www.urbandictionary.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

wordlinks = []
for x in range(2,3):
    r = requests.get(f'https://www.urbandictionary.com/browse.php?character=A&page={x}')

    soup = BeautifulSoup(r.content, 'html.parser')
    wordlist = soup.find_all('li')
    for item in wordlist:
        for link in item.find_all('a', href = True):
            wordlinks.append(baseurl + link['href'])

testlink = 'https://www.urbandictionary.com/define.php?term=A%20Bama'
r = requests.get(testlink)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.find("div",{"class":"meaning"}))
#try to scrape the meaning out of this as done previously