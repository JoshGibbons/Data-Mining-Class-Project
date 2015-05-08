'''Authors:
    Josh Gibbons
    David
    Yun Nam Lin
'''

import tweepy
import imp
import sys
import json
import authKeys
import interface
import sent
import basicInfo

#utf check
imp.reload(sys)
sys.setdefaultencoding("utf-8")


#Private keys
consumer_key = authKeys.getA()
consumer_secret = authKeys.getB()
access_token_key = authKeys.getC()
access_token_secret = authKeys.getD()

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

# Creation of the api, using authentication
api = tweepy.API(auth)



def main():
    interface.createGUI()

def getUserData(username, window):
    print(username)

    tweets = []
    #get our arrays setup
    count = 0
    if count < 100:
        for status in tweepy.Cursor(api.user_timeline, screen_name=username).items():
            tweets.append(status.text)
            count += 1

    basicInfo.showBasicInfo(username)
    #sent.getSentiment(tweets, window)


if __name__ == '__main__':
    main()

