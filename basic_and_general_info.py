import json
from datetime import datetime
import collections
import interface

def showBasicInfo(tweet_object_list, window):

    name = 'Name: ' + tweet_object_list[0]['user']['name'] # Name of the account owner
    screenName = 'Screen Name: ' + tweet_object_list[0]['user']['screen_name'] # Screen name
    userID = 'User ID: ' + tweet_object_list[0]['user']['id_str'] # Numeric id of the account
    location = 'Location: ' + tweet_object_list[0]['user']['location']     # Users location # This requires decoding

    #print 'Account Creation: ' + tweet_object_list[0]['user']['created_at']   # Date the account was created in twitter datetime format

    # Converting from twitter datetime format to python datetime format
    account_creation = datetime.strptime(tweet_object_list[0]['user']['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
    accCreation = 'Account Creation: {:%m-%d-%Y}'.format(account_creation) # Formatting

    age = (datetime.now() - account_creation).days        # Account Age in days
    accAge =  'Account Age: ' + str(age / 365) + ' Years, ' + str(age % 365) + ' days'   # Formatting

    interface.showBasicInfo(window, name, screenName, userID, location, accCreation, accAge)

def showGeneralInfo(tweet_object_list, window):

    account_creation = datetime.strptime(tweet_object_list[0]['user']['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
    age = (datetime.now() - account_creation).days        # Account Age in days
 
    print 'Total Tweets: ' + str(tweet_object_list[0]['user']['statuses_count'])  # Total number of tweets
    print 'Average Number of Tweets Daily: ' + str('%.2f'%(float(tweet_object_list[0]['user']['statuses_count']) / float(age)))   # Average number of tweets each day
 
    retweetCount = 0
    mostRetweeted = 'foo_status'

    hashtags = []

    urls = []
    # Stores the tweet with the highest amount of retweets
    count = 0
    for tweet in tweet_object_list:
        if retweetCount < tweet_object_list[count]['retweet_count'] and tweet_object_list[count]['text'].split(' ', 1)[0] != 'RT':
            mostRetweeted = tweet_object_list[count]['text']
            retweetCount = tweet_object_list[count]['retweet_count']
 
        # NOTE: str(tweet_object_list[count]['retweeted']) returns true if the API user has retweeted this particular tweet
        # not if the tweet itself is a retweet.

        # Stores the hashtags in a list
        # Only applies if the user is the creator of the tweet
        eachHashtag = 0
        while eachHashtag < len(tweet_object_list[count]['entities']['hashtags']) and tweet_object_list[count]['text'].split(' ', 1)[0] != 'RT':
            hashtags.append(tweet_object_list[count]['entities']['hashtags'][eachHashtag]['text'])
            eachHashtag+=1

        # Stores the urls in a list
        temp_string = ''
        truncated_url = ''
        eachUrl = 0
        while eachUrl < len(tweet_object_list[count]['entities']['urls']):
            temp_string = str(tweet_object_list[count]['entities']['urls'][eachUrl]['expanded_url'].partition('/')[2:3:2])
            slashCount = 0
            for i in range(0, len(temp_string)):
                if slashCount > 1:
                    break
                if slashCount == 1:
                    truncated_url = truncated_url + temp_string[i]
                if temp_string[i] == '/' or (i + 1 < len(temp_string) and slashCount == 1 and (temp_string[i + 1] == '/' or temp_string[i + 1] == '\'')):
                    slashCount+=1
            urls.append(truncated_url)
            eachUrl+=1

        count+=1

    freqTweet = 'Most Retweeted Tweet: ' + mostRetweeted
    freqCount = 'Retweet Count for Most Retweeted Tweet : ' + str(retweetCount)

    tags = []
    top_five_hashtags =  collections.Counter(hashtags).most_common(5)
    print 'Top Five Hashtags Used: '
    for hashtag, occurrences in top_five_hashtags:
        tag = '%s' %hashtag
        tags.append((str)(tag))
    # Include number of occurrences?
    #for hashtag,occurrences in top_five_hashtags:
        #print "%s is used %s times" %(hashtag,occurences)

    sites = []
    top_five_urls =  collections.Counter(urls).most_common(5)
    print 'Top Five Websites Referenced: '
    for url, occurrences in top_five_urls:
        site = '%s' %url
        sites.append((str)(site))
    # Include number of occurrences?
    #for url,occurrences in top_five_hashtags:
        #print "%s is used %s times" %(url,occurrences)

    interface.displayGenInfo(window, freqTweet, freqCount, tags, sites)
