import requests
from bs4 import BeautifulSoup

url = 'https://www.senate.gov/general/committee_assignments/assignments.htm'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

fetterman_div = soup.find('a', {'name': 'FettermanPA'}).find_parent('div', {'style': 'float:left; width:25%; font-weight:bold; min-width:200px;'})
fetterman_name = fetterman_div.find('a', {'name': 'FettermanPA'}).find_next('a').text.split()[0]
last_name = fetterman_div.text
split_last_from_first = last_name[0:11].split()
print(fetterman_name[0:9] +':')

committees_div = fetterman_div.find_next('div', {'style': 'float:left; width:72%; min-width:200px;'})
committees_strong_tags = committees_div.find_all('strong')

for strong_tag in committees_strong_tags:
    committee_name = strong_tag.find('a').text
    print(committee_name)

print()

casey_div = soup.find('a', {'name': 'CaseyPA'}).find_parent('div', {'style': 'float:left; width:25%; font-weight:bold; min-width:200px;'})
casey_name = casey_div.find('a', {'name': 'CaseyPA'}).find_next('a').text.split()[0]
last_name = casey_div.text
split_last_from_first = last_name[0:11].split()
print(casey_name[0:5] + ':')

committees_div = casey_div.find_next('div', {'style': 'float:left; width:72%; min-width:200px;'})
committees_strong_tags = committees_div.find_all('strong')

for strong_tag in committees_strong_tags:
    committee_name = strong_tag.find('a').text
    print(committee_name)