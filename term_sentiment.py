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

def get_non_afinn_pairs(tweet_text, scores):
    sentiment = get_sentiment(tweet_text, scores)
    return {word: sentiment 
            for word in tweet_text.split(" ") if word not in scores}
    
def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    
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
