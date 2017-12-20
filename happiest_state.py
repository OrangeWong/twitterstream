# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:32:34 2017

@author: richa
"""

import sys
import json 
import operator 
from collections import defaultdict

def get_text(tweet):
    return json.loads(tweet, encoding = 'utf-8').get('text', '')

def get_sentiment(tweet_text, scores):
    # to caluclate the sentiment for a tweet
    sentiment = sum( scores.get(word, 0) for word in tweet_text.split(" ") )
    return sentiment
    
def get_afinn_scores(afinnfile):
    scores = {} # initialize an empty dictionary
    with open(afinnfile, 'r') as f:
        for line in f:
            term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
            scores[term] = int(score)  # Convert the score to an integer.
    return scores

def get_state(tweet):
    # if the tweet is located, info is in the place dictionary
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}
    
    try:
        place = json.loads(tweet, encoding = 'utf-8').get('place')
        _, state=(x.strip().upper() for x in place.get('full_name').split(","))
        if state in states: 
            return state
        else:
            return None
    except:
        return None
    
def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    scores = get_afinn_scores(sent_file)
    
    with open(tweet_file, 'r') as f:
        US_scores = [ (get_state(line), get_sentiment(get_text(line), scores)) 
                     for line in f if get_state(line)]
    
    states_score, states_count = defaultdict(int), defaultdict(int)
    for key, val in US_scores:
        states_score[key] += val
        states_count[key] += 1
        
    states_avg = {state: states_score[state]/float(states_count[state])
        for state in states_score}
    
    # stdout the sentiment
    happiest_state = max(states_avg.iteritems(), key=operator.itemgetter(1))[0]
    sys.stdout.write('{0} {1:f}\n'.format(happiest_state.encode('utf-8'), 
                                          states_avg[happiest_state]))
    
if __name__ == '__main__':
    main()
    