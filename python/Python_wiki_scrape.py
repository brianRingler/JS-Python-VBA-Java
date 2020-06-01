from bs4 import BeautifulSoup
import requests
import numpy as np

def check_response(resp_obj):
    try:
        if resp_obj.status_code == 200:
            print(f"Connection OK: {resp_obj.status_code}")
    except:
        print(f"Error: Not 200 return value was: {resp_obj}")

# get HTML
url_sbw = r"https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
page_sbw = requests.get(url_sbw)

# check for status code 200 
check_response(page_sbw)

soup = BeautifulSoup(page_sbw.text, 'html.parser')

# lets first get the body tag look for our tables 
body_tag = soup.body

# Here we use find_all looking for the tag table and attribute class spelled two ways
tables = body_tag.find_all('table',{'class': 'wikitable'})

# from the four tables we want index 1
sb_table = tables[1]

headerNames = []
for i in range(len(sb_table.find_all('th'))):
    try:
        if len(sb_table.find_all('th')[i].contents) > 1:
            convert = list(sb_table.find_all('th')[i].contents)
            name = convert[0].rstrip("\n") + convert[2].rstrip("\n`")
            headerNames.append(name)
        else:
            name = sb_table.find_all('th')[i].string.rstrip("\n")
            headerNames.append(name)
    except:
        pass

#print(headerNames)

winnerObj = {}
for name in headerNames:
    winnerObj[name] = []

try:
    j = 0
    while j < len(sb_table.find_all('td')):
        i = 0
        while i < len(winnerObj.keys()):
            #print(i)
            if i % 2 == 0 or i == 5:
                #print(sb_table.find_all('td')[j].find('a').string)
                winnerObj[headerNames[i]].append(sb_table.find_all('td')[j].find('a').string)
            else:
                #print(sb_table.find_all('td')[j].find('span').string)
                winnerObj[headerNames[i]].append(sb_table.find_all('td')[j].find('span').string)
            i += 1
            j += 1
            #print(winnerObj)
except:
    winnerObj[headerNames[i]].append(np.nan)
    i += 1
    j += 1

print(winnerObj)