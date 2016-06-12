import sys
import json

sentiDictionary = {}


def buildTermScoreDict (fp):
   for line in fp:
	term, score  = line.split("\t") 
	sentiDictionary[term] = int(score) 

def scoreTweets (fp) :
    for line in fp:
	 tweetText = json.loads(line)['text']  
         words = tweetText.split() 
         lineTotal = 0 
         for word in words:
	    score = sentiDictionary.get(word)
            if score is not None:
               lineTotal += score
         print lineTotal  
             
def main():
    senti_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    buildTermScoreDict(senti_file)
    scoreTweets(tweet_file)

if __name__ == '__main__':
    main()
