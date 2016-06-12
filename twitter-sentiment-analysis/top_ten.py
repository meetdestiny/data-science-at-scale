import sys
import json
import heapq

hashtagsDictionary = {}


def top10 (fp) :
    for line in fp:
         entities = json.loads(line).get('entities')
         if entities is None:
		continue
	 hashtags = entities['hashtags']  
         if len(hashtags) <= 0 :
		continue 
         for hashtag in hashtags:
             countHashTag(hashtag['text']) 
    k_keys_sorted = heapq.nlargest(10, hashtagsDictionary)     
    for key in k_keys_sorted:
	print key , hashtagsDictionary.get(key) 


def countHashTag(hashtag) :
	count = hashtagsDictionary.get(hashtag)
        if count is None:
		hashtagsDictionary[hashtag] = 1 
	else:
		hashtagsDictionary[hashtag] = count +1
         
def main():
    tweet_file = open(sys.argv[1])
    top10(tweet_file)

if __name__ == '__main__':
    main()
