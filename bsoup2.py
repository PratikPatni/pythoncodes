import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url=input('Enter url-')
count=int(input('Enter count-'))
pos=(int(input('Enter position-')))-1
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
for i in range(count):
  tags=soup('a')
  print(tags[pos].contents[0])
  url=tags[pos].get('href',None)
  html = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(html, 'html.parser')
  tags=None
