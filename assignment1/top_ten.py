__author__ = 'moony'
import sys
import json
import operator


def main():
    tweet_file = open(sys.argv[1])
    tweet_size = 0
    cnt = {}
    all = 0
    for line in tweet_file:
        tweet_size += 1
        obj = json.loads(line)
        try:
            hashtags = obj["entities"]["hashtags"]
            for tag in hashtags:
                if "text" in tag:
                    all += 1
                    cnt[tag["text"]] = cnt.get(tag["text"], 0) + 1
        except:
            pass

    #print cnt
    #print all
    result = sorted(cnt.items(), key=operator.itemgetter(1), reverse=True)
    #print result
    #print len(result)
    for i in range(10):
        print result[i][0].encode('utf-8'), float(result[i][1])


if __name__ == '__main__':
    main()
