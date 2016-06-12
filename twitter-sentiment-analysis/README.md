# Twitter sentiment analysis

This script uses [AFINN] (http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010) to derive overall sentiment of tweets. 
While we can use any weighted aggregation function, this sample shows simple arithmetic addition of sentiments can work as point of reference.

For deriving sentiment scores of unlisted words, I have used scoring based on 
[O'Connor, B., Balasubramanyan, R., Routedge, B., & Smith, N. From Tweets to Polls: Linking Text Sentiment to Public Opinion Time Series. (ICWSM), May 2010.](http://www.cs.cmu.edu/~nasmith/papers/oconnor+balasubramanyan+routledge+smith.icwsm10.pdf)

