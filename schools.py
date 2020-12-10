import requests
from bs4 import BeautifulSoup as bs

base_url = 'https://en.wikipedia.org/wiki/'

book = open('ken.txt', 'r').readlines()
lis = list(book)
locations = {}
i = 0
with open('ken.txt', 'r') as lis:
    for sc in lis.readlines():
        name = str(sc.split(',')[0])
        name = name[0:-1] # assumes the last letter of the name is '*'
        name = "_".join(name.split(' '))

        page = requests.get(base_url+name)
        soup = bs(page.content, 'html.parser')

        # if you'd like a soft copy on your device
        save = open(f'school/{name}.txt', 'w', encoding = 'utf-8')
        save.write(soup.prettify())
        save.close

        if soup.find(attrs={"class": "latitude"}) and soup.find(attrs={"class": "longitude"}):
            locations.update({name: {'latitude': soup.find(attrs={"class": "latitude"}).get_text(), 'longitude': soup.find(attrs={"class": "longitude"}).get_text()}})

        details = {}
        txt = soup.select('table tbody')[0]
        tt = txt.find_all(attrs={'class': "nickname"})
        tx = txt.find_all('tr')
        for tt in tx:
            if tt.find('th') and tt.find('td'):
                details.update({tt.find('th').get_text(): tt.find('td').get_text()})
        locations.update({name:details})
        i+= 1

print(i)
print(locations['Wesleyan_University'])


#  for one school. works well.
# name = 'stanford_university'
# page = requests.get(base_url+name)
# soup = bs(page.content, 'html.parser')
#
# txt = soup.select('table tbody')[0]
# tt = txt.find_all(attrs={'class': "nickname"})
# tx = txt.find_all('tr')
# for tt in tx:
#     if tt.find('th'):
#         details.update({tt.find('th').get_text():tt.find('td').get_text()})
# print(details)


