import sys
import json 

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

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]

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
    