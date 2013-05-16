import sys
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}  # initialize an empty dictionary
    sent_size = 0
    tweet_size = 0
    for line in sent_file:
        sent_size += 1
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    new_sent = {}
    for line in tweet_file:
        tweet_size += 1
        obj = json.loads(line)
        if "text" in obj:
            score = 0
            text = obj["text"]
            #print text
            for term in text.split():
                score += scores.get(term, 0)
            #print score
            if score != 0:
                for term in text.split():
                    if term not in scores:
                        new_sent[term] = new_sent.get(term, 0) + score

    #print new_sent
    #print sent_size, tweet_size
    for t in new_sent.iteritems():
        print t[0].encode('utf-8'), t[1]


if __name__ == '__main__':
    main()
