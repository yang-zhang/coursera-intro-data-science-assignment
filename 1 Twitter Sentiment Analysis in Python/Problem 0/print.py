import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
<<<<<<< HEAD
print json.load(response)

numPages = 1;

for i in range(1,numPages+1):
    print 'Page: ' + str(i)
    url = 'http://search.twitter.com/search.json?q=microsoft' + str(i)
    response = urllib.urlopen(url)
    data = json.load(response)


=======
##print json.load(response)

numPages = 2;

for i in range(1,numPages+1):
    print 'Page: ' + str(i)
    url = 'http://search.twitter.com/search.json?q=microsoft&page=' + str(i)
    response = urllib.urlopen(url)
    data = json.load(response)
##    print "type(data): " + str(type(data))
##    print 'data.keys(): ' + str(data.keys())
    tweets = data['results']
##    print 'tweets: ' + str(tweets)
##    print 'type(tweets): ' + str(type(tweets))
    for t in tweets:
##        print type(t)
        print t['text']
    
>>>>>>> testing
