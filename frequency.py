# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 12:03:46 2017

@author: richa
"""

import sys
import json 
from collections import Counter

def get_text(tweet):
    '''
    Args:
        tweet (str): A string that contains a tweet object.
    
    Returns:
        str: The string of text in the tweet object or an empty string if 
                text section is empty. 
    '''
    return json.loads(tweet, encoding = 'utf-8').get('text', '')

def get_relative_freq(texts):
    '''
    Args:
        texts (list): A list contains all the words in the tweets.
        
    Returns:
        dict: A dict contains the relative frequency on word.
    '''
    
    # generate the freq to store the counting of word in texts
    freq = Counter(word for text in texts for word in text)
    # total occurrences
    sum_freq = sum( freq.values() )
    
    return {word: freq[word]/float(sum_freq) for word in freq}
    
def main():
    tweet_file = sys.argv[1]
    
    with open(tweet_file, 'r') as f:
        texts = [get_text(line).split() for line in f]
    
    # generate the relative freq
    rel_freq = get_relative_freq(texts)
    
    # stdout the pairs of word and its relative frequency
    for word in rel_freq:
        sys.stdout.write(
            '{0} {1:f}\n'.format(word.encode('utf-8'), rel_freq[word])
                        ) 
    
if __name__ == '__main__':
    main()
    