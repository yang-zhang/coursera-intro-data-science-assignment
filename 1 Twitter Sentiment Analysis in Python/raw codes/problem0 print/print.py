import urllib
import json

numPages = 10;

for i in range(1,numPages+1):
    print "Page: " + str(i)
    url = "http://search.twitter.com/search.json?q=microsoft&page=" + str(i)
    response = urllib.urlopen(url)
    data = json.load(response)
    tweets = data['results']
    for t in tweets:
        print t['text']
