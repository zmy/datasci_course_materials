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
    for line in tweet_file:
        tweet_size += 1
        obj = json.loads(line)
        score = 0
        if "text" in obj:
            text = obj["text"]
            #print text
            for term in text.split():
                score += scores.get(term, 0)
        print score
    #print sent_size, tweet_size


if __name__ == '__main__':
    main()
