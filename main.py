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

#Global tweet text array
tweets = []

def sentiment(username):
    print("in sentiment")

def main():

    interface.createGUI()

def getUserData(username):
    print(username)

    #get our array setup for use
    idx = 0
    for status in tweepy.Cursor(api.user_timeline, screen_name=username).items():
        tweets[idx] = status.text
        idx += 1

    sentiment(username)

    #for user in tweepy.Cursor(api.followers, screen_name="GreatPowerKyle").items():
    #    print user.screen_name



if __name__ == '__main__':
    main()

