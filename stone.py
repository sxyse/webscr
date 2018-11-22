import os
import requests
from bs4 import BeautifulSoup

path = "storyofstone"
folder = os.path.exists(path) 
if not folder: 
    os.mkdir(path) 
    print ("path created" )
    print("begain downloading...")
else: 
    print("begain downloading...")


url = "http://www.purepen.com/hlm"
r = requests.get(url)
r.encoding = r.apparent_encoding
r = r.text

soup = BeautifulSoup(r, 'lxml')
findtd = soup.find_all('td')
findtd = findtd[1:-1]

fullbook = ""
for i in range(len(findtd)//2):
    filename = findtd[2*i].get_text()
    filename = ''.join(filename.split())
    filename = 'storyofstone/' + filename + ".txt"

    url_chapter = url + '/' + findtd[2*i+1].a.get('href')
    r = requests.get(url_chapter)
    r.encoding = r.apparent_encoding
    r = r.text

    soup = BeautifulSoup(r, 'lxml')
    title = soup.find('b')
    
    content = soup.find('center')
    str = "     " + title.get_text() + '\n' + content.get_text()
    f = open(filename,'w')
    f.write(str)
    f.close()
    fullbook += str
    print("%s saved!"%(title.get_text()))

f = open('storyofstone/full_book.txt','w')
f.write(fullbook)
f.close()
print('full book saved!')