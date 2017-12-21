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

def main():
    '''
    Args: 
        
    Returns: 
        stdout: The stdout of the sentiment of the tweet based on the scored 
        file.    
    '''
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    
    # get the scores from the AFINN file
    scores = get_afinn_scores(sent_file)

    with open(tweet_file, 'r') as f:
        for line in f:
            # extract the text otherwise return empty string
            tweet_text = get_text(line)
            # return the sentiment
            sentiment = get_sentiment(tweet_text, scores)
            # stdout the sentiment
            sys.stdout.write('{0:d}\n'.format(sentiment))
    
if __name__ == '__main__':
    main()
    