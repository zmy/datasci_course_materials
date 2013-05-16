__author__ = 'moony'
import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    tweet_size = 0
    cnt = {}
    all = 0
    for line in tweet_file:
        tweet_size += 1
        obj = json.loads(line)
        if "text" in obj:
            text = obj["text"]
            #print text
            for term in text.split():
                all += 1
                cnt[term] = cnt.get(term, 0) + 1

    #print cnt
    #print all
    for t in cnt.iteritems():
        print t[0].encode('utf-8'), float(t[1])/all


if __name__ == '__main__':
    main()
