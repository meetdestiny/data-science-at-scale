import sys
import json

termDictionary = {}


def scoreTweets (fp) :
    count = 0.0;
    for line in fp:
	 tweetText = json.loads(line)['text']  
         words = tweetText.split() 
         for word in words:
             populateCount(word, termDictionary)
             count += 1.0
    for word,wordCount in termDictionary.iteritems():
	print word, wordCount/count    
     
def populateCount(word, dict) :
	if dict.get(word) is None:
		count = dict.get(word)
		if count is None:
                     dict[word] = 1.0
                else:
                     dict[word] = count + 1.0

def main():
    tweet_file = open(sys.argv[1])
    scoreTweets(tweet_file)

if __name__ == '__main__':
    main()
