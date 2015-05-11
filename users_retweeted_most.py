import json
import collections

def showUsersRetweetedMost(tweet_object_list, window):

    retweets = []
    retweetees = [] 
    count = 0

    # Store retweets in a list
    for tweet in tweet_object_list:
        if tweet_object_list[count]['text'].split(' ', 1)[0] == 'RT':
            retweets.append(tweet_object_list[count]['text'])
        count+=1

    count = 0
    # Store the original tweeters in a list 
    for tweet in retweets:
        temp_string = ''
        retweetee = ''
        temp_string = retweets[count]
        atAndColonCount = 0
        for i in range(0, len(temp_string)):
            if atAndColonCount > 1:
                break
            if atAndColonCount == 1:
                retweetee = retweetee + temp_string[i]
            if temp_string[i] == '@' or (i + 1 < len(temp_string) and temp_string[i + 1] == ':'):
            #if temp_string[i] == '@' or temp_string[i + 1] == ':': 
                atAndColonCount+=1
        retweetees.append(retweetee)
        count+=1   

    top_five_retweetees =  collections.Counter(retweetees).most_common(5)
    print 'Top 5 Users Most Often Retweeted: '
    for user, occurrences in top_five_retweetees:
        print '\t\t\t\t%s' %user
    # Include number of occurrences? 
    #for hashtag,occurrences in top_five_hashtags:
        # print "%s is used %s times" %(hashtag,occurences)
