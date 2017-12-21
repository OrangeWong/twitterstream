import sys
import json 

def get_text(tweet):
    '''
    Args:
        tweet (str): A string that contains a tweet object.
    
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

def get_non_afinn_pairs(tweet_text, scores):
    '''
    Args:
        tweet_text (str): A string constians the text from a tweet.
        scores (dict): A dict contains the pairs of English word and its score.
        
    Returns:
        dict: A dict contains the pairs of word and its scores, where the word 
        does not belong to the scores. 
    '''
    # get the sentiment of the tweet's text
    sentiment = get_sentiment(tweet_text, scores)
    
    # assign the sentniment to the rest of the words
    return {word: sentiment 
            for word in tweet_text.split(" ") if word not in scores}
    
def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    
    # get the sentiment of the tweet's text
    scores = get_afinn_scores(sent_file)
    
    with open(tweet_file, 'r') as f:
        for line in f:
            # extract the text otherwise return empty string
            tweet_text = get_text(line)
            # return the non_afinn pairs
            non_afinn_pairs = get_non_afinn_pairs(tweet_text, scores)
            # stdout the sentiment
            for non_afinn_word, non_afinn_score in non_afinn_pairs.items():
                sys.stdout.write(
                    '{0} {1:d}\n'.format(non_afinn_word.encode('utf-8'), 
                                         non_afinn_score))

if __name__ == '__main__':
    main()
