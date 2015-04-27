'''authours:
    Josh Gibbons
    David
    Yun Nam
'''

import twitter
import tweepy  # twitter api module - python version
import datetime  # python datetime module
import imp
import sys
import json  # python json module
import authKeys

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

# Creation of the actual interface, using authentication
api = tweepy.API(auth)


def print_info(tweet):
    print('***************************')
    print(('Tweet ID: ', tweet['id']))
    print(('Post Time: ', tweet['created_at']))
    print(('User Name: ', tweet['user']['screen_name']))
    try:
        print(('Tweet Text: ', (tweet['text'])))
    except:
        pass


def main():

    for user in tweepy.Cursor(api.followers, screen_name="GreatPowerKyle").items():
        print user.screen_name

if __name__ == '__main__':
    main()

