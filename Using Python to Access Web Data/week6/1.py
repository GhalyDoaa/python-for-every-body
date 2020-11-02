import urllib.request, urllib.error, urllib.parse
import json
url = 'http://py4e-data.dr-chuck.net/comments_385760.json'
print('Retriving', url)
url_handler = urllib.request.urlopen(url).read()
print('Retrived', len(url_handler), 'characters')
js = json.loads(url_handler)
print(js)
res = 0
for comment in js['comments']:
    res = res + comment['count']
print('Sum:', res)
