import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import urllib.error
url = 'http://py4e-data.dr-chuck.net/comments_385759.xml'
sorc = urllib.request.urlopen(url)
data = sorc.read()
print('Retrived', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')

print('Count:', len(counts))
resault = 0
for count in counts:
    resault = resault + int(count.text)
print('Sum:', resault)