import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
print json.load(response)

numPages = 1;

for i in range(1,numPages+1):
    print 'Page: ' + str(i)
    url = 'http://search.twitter.com/search.json?q=microsoft' + str(i)
    response = urllib.urlopen(url)
    data = json.load(response)


