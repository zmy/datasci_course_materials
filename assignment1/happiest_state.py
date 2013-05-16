__author__ = 'moony'
import sys
import json
#import operator


def main():
    states = {
        'Mississippi': 'MS', 'Oklahoma': 'OK', 'Wyoming': 'WY', 'Minnesota': 'MN', 'Alaska': 'AK', 'Illinois': 'IL',
        'Arkansas': 'AR', 'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 'Texas': 'TX',
        'Iowa': 'IA', 'Wisconsin': 'WI', 'Arizona': 'AZ', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 'Virginia': 'VA',
        'Oregon': 'OR', 'Connecticut': 'CT', 'Tennessee': 'TN', 'New Hampshire': 'NH', 'Idaho': 'ID', 'West Virginia': 'WV',
        'South Carolina': 'SC', 'California': 'CA', 'Massachusetts': 'MA', 'Vermont': 'VT', 'Georgia': 'GA',
        'North Dakota': 'ND', 'Pennsylvania': 'PA', 'Florida': 'FL', 'Hawaii': 'HI', 'Kentucky': 'KY', 'Rhode Island': 'RI',
        'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 'Alabama': 'AL', 'South Dakota': 'SD', 'Colorado': 'CO',
        'New Jersey': 'NJ', 'Washington': 'WA', 'North Carolina': 'NC', 'New York': 'NY', 'Montana': 'MT', 'Nevada': 'NV',
        'Delaware': 'DE', 'Maine': 'ME'
    }
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    happy = {}  # initialize an empty dictionary
    sent_size = 0
    tweet_size = 0
    for line in sent_file:
        sent_size += 1
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for line in tweet_file:
        tweet_size += 1
        obj = json.loads(line)
        if "text" in obj and "place" in obj:
            place = obj["place"]
            try:
                if place["country_code"] == "US":
                    full_name = place["full_name"]
                    #print obj["text"]
                    #print full_name
                    state = "UNKNOWN"
                    for k, v in states.items():
                        #print k, v
                        if full_name.find(k) != -1 or full_name.find(v) != -1:
                            state = v
                            break
                    #print state
                    if state != "UNKNOWN":
                        score = 0
                        for term in obj["text"].split():
                            score += scores.get(term, 0)
                        happy[state] = happy.get(state, 0) + score
                        #print score
            except:
                pass
    #print happy
    best = 'CA'
    high = happy.get('CA', 0)
    #print max(happy.iteritems(), key=operator.itemgetter(1))
    for t in happy.iteritems():
        if t[1] > high:
            high = t[1]
            best = t[0]
    print best


if __name__ == '__main__':
    main()
