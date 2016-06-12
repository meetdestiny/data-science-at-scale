import sys
import json

sentiDictionary = {}
stateSenti = {}
states = {
        'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa', 'AZ': 'Arizona', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DC': 'District of Columbia', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi', 'MT': 'Montana', 'NA': 'National', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 'VI': 'Virgin Islands', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'WY': 'Wyoming' 
}

def buildTermScoreDict (fp):
   for line in fp:
	term, score  = line.split("\t") 
	sentiDictionary[term] = int(score) 

def scoreTweets (fp) :
     for line in fp:
         tweet = json.loads(line) 
	 tweetText = tweet.get('text')  
         if tweetText is None:
		continue 
         words = tweetText.split() 
         state = getState(tweet) 
         lineTotal = 0 
         for word in words:
	    score = sentiDictionary.get(word)
            if score is not None:
               lineTotal += score
         addSentiToState(state, lineTotal)    
     happiestScore = -99999999 
     happiestState = "" 

     stateSenti.pop("NA")
     for key,value in stateSenti.iteritems() :
         if value > happiestScore :
	 	happiestScore = value
         	happiestState = key          
     print happiestState

def getState(tweet):
	place = tweet['place']
        if place is not None:
		city = place['full_name']		 
                if city.find(",") > -1 :  
                	return city.split(",")[1].strip() 
        location = tweet['user']['location']     		
	if location is not None:
        	if location in states.values():
          		return getCodeFromName(location)
		if location.find(",") > -1 :
			if states.get(location.split(",")[1].strip()) is not None:
				return location.split(",")[1].strip()
        return "NA" 


def getCodeFromName(stateName) :
	for code,name in states.iteritems():
    		if name == stateName:
       			return code	 

def addSentiToState(state,senti):
	sentiScore = stateSenti.get(state)
        if sentiScore is None:
		stateSenti[state] = senti
	else: 
	 	stateSenti[state] = sentiScore + senti

def main():
    senti_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    buildTermScoreDict(senti_file)
    scoreTweets(tweet_file)

if __name__ == '__main__':
    main()
