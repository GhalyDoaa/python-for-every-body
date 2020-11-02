import xml.etree.ElementTree as ET
import urllib.request
import urllib.parse
import urllib.error
url = input('Enter - ')
if(url == ' '):
	url = 'http://py4e-data.dr-chuck.net/comments_385759.xml'
sorc = urllib.request.urlopen(url)
data = sorc.read()
print('Retrived', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
#tracking
print('Count:', len(counts))
resault = 0
for count in counts:
    resault = resault + int(count.text)
print('Sum:', resault)
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The #program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment #counts from the XML data, compute the sum of the numbers in the file
