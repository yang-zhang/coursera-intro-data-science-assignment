import sys
import json
import re

def hw(sent_file,tweet_file):
    sent_dict = {}

    for line in sent_file:
        line_list = line.split()
        if len(line_list) > 2:
            length = len(line_list)
            temp_line_list = []
            temp_line_list.append(" ".join(line_list[:length-1]))
            temp_line_list.append(line_list[length-1])
            line_list = temp_line_list                       
        sent_dict[line_list[0]] = float(line_list[1])        
        
    for line in tweet_file:
##        print "a new tweet"
        dict = json.loads(line)
        sum = 0;
        if 'text' in dict.keys():
            text = dict['text']
##            print text.encode('utf-8')
            words = text.split()
            
            for word in words:
                word = re.sub('[^0-9a-zA-Z]+', '', word)
                sum += sent_dict.get(word, 0)
        print sum

            


def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
