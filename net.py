import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url=input('Enter url-')
html = urllib.request.urlopen(url).read()
data=html.decode()
tree = ET.fromstring(data)
ls=list()
sum=0;
c=0;
ls=tree.findall('.//count')
for l in ls:
    sum=sum+int((l.text))
    c=c+1
print(sum)
