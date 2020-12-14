import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url=input('Enter url-')
if len(url)<1:url='http://py4e-data.dr-chuck.net/comments_917711.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags=soup('span')
s=0
c=0
for tag in tags:
    s=s+int(tag.contents[0])
    c=c+1
print("Count -",c)
print("Sum -",s)
