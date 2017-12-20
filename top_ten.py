import sys
import json 
from collections import Counter

def get_hashtag(tweet):
    hashtags = json.loads(tweet).get('entities', {}).get('hashtags', {})
    return [hashtag['text'] for hashtag in hashtags]
    
def main():
    tweet_file = sys.argv[1]
    
    with open(tweet_file, 'r') as f:
        hashtags = [hashtag for line in f for hashtag in get_hashtag(line)]
        
    hashtags_hist = Counter(hashtags).most_common(10)
    
    # stdout the sentiment
    for tag, count in hashtags_hist:
        sys.stdout.write('{0} {1:d}\n'.format(tag.encode('utf-8'), count))
    
if __name__ == '__main__':
    main()
    