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
    '''
    Args:
        tweet (str): A string that contains a tweet's text.
    
    Returns:
        str: The string of text in the tweet object or an empty string if 
        text section is empty. 
    '''
    return json.loads(tweet, encoding = 'utf-8').get('text', '')

def get_sentiment(tweet_text, scores):
    '''
    Args:
        tweet_text (str): A string that contains the text in tweet.
        scores (dict): A dict of English word scores.
    Returns:
        float: The sentiment of the tweet text. 
    '''
    
    # Zero if word is not in the scores
    sentiment = sum( scores.get(word, 0) for word in tweet_text.split(" ") )
    
    return sentiment
    
def get_afinn_scores(afinnfile):
    '''
    Args:
        afinnfile (file): A file contains the English word scores, and the file
        is tab-delimited.
        
    Returns:
        dict: The dict that contains pairs of English word and the related 
        score
    '''
    # initialize an empty dictionary
    scores = {}
    with open(afinnfile, 'r') as f:
        for line in f:
            # The file is tab-delimited.
            term, score  = line.split("\t")  
            scores[term] = int(score)
    return scores

def get_state(tweet):
    '''
    Args:
        tweet (string): A string contains the tweet's object
        
    Returns:
        Str: The state in the US if it is written in tweet's place, otherwise
        None.
    '''
    # A list of states in the US
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
        # try if the tweet contains place
        place = json.loads(tweet, encoding = 'utf-8').get('place')
        _, state=(x.strip().upper() for x in place.get('full_name').split(","))
        if state in states:
            # check if state is in states
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
        # get a list of tuples containing state and score of the tweets
        US_scores = [ (get_state(line), get_sentiment(get_text(line), scores)) 
                     for line in f if get_state(line)]
    
    # initiate two defaultdicts
    states_score, states_count = defaultdict(int), defaultdict(int)
    for key, val in US_scores:
        states_score[key] += val
        states_count[key] += 1
    
    # return a dict contains state and its average score
    states_avg = {state: states_score[state]/float(states_count[state])
        for state in states_score}
    
    # get the max based on the average score
    happiest_state = max(states_avg.iteritems(), key=operator.itemgetter(1))[0]
    
    # stdout the sentiment
    sys.stdout.write('{0} {1:f}\n'.format(happiest_state.encode('utf-8'), 
                                          states_avg[happiest_state]))
    
if __name__ == '__main__':
    main()
    