import json
import urllib.parse, urllib.error,urllib.request
url=input('Enter the url-')
html=urllib.request.urlopen(url).read()
data=html.decode()
info = json.loads(data)
s=0
for ls in info['comments']:
    print(ls['count'])
    s=s+ls['count']
print("sum -",s)
