import sys
import json

sentiDictionary = {}
posSentiDictionary = {}
negSentiDictionary = {}

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
         if lineTotal > 0: 
             populateCount(line, posSentiDictionary)
         else:
             populateCount(line, negSentiDictionary)

def populateCount(line, dict) :
	tweetText = json.loads(line)['text']  
	words = tweetText.split()
        for word in words:
		if sentiDictionary.get(word) is None:	
			count = dict.get(word)
                	if count is None:
                   		dict[word] = int(0)
                	else: 
                   		dict[word] = count +1  
    
             
def scoreUnkownWords() :
	for key, posSenti in posSentiDictionary.iteritems():
		negSenti = negSentiDictionary.get(key)
                if negSenti is not None: 
			print key, posSenti - negSenti
			negSentiDictionary.pop(key)
                else:
			print key, posSenti  
        for key, value in negSentiDictionary.iteritems():
		print key , value*-1					


def main():
    senti_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    buildTermScoreDict(senti_file)
    scoreTweets(tweet_file)
    scoreUnkownWords()
if __name__ == '__main__':
    main()
