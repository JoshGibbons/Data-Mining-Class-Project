'''
Authors:
	Josh Gibbons
	David Noftsier
	Yun Nam Lin
'''

import tweepy
import imp
import sys
import json
import authKeys
import basic_and_general_info
import write_and_read_objects
import users_retweeted_most
import interface
import sent
import cloud

# utf check
imp.reload(sys)
sys.setdefaultencoding("utf-8")


# Private keys
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
    #Switch between accessing the API or accessing the text file
    onlineMode = True

    if(onlineMode): # Access the stored tweet objects instead of API
        interface.createGUI()
    else: # Just access the stored tweet objects
        interface.createOfflineGUI()
         

def getUserData(username, window):

    tweet_object_list = write_and_read_objects.writeTweetObjectsToFile(api, username)

    basic_and_general_info.showBasicInfo(tweet_object_list, window)
    basic_and_general_info.showGeneralInfo(tweet_object_list, window)

    sent.getSentiment(tweet_object_list, window)

    users_retweeted_most.showUsersRetweetedMost(tweet_object_list, window)

    #cloud.makeCloud(tweet_object_list, window)




def getUserDataOFFLINE(window):


    username = 'gavinfree'
    tweet_object_list = write_and_read_objects.readJsonFile()

    basic_and_general_info.showBasicInfo(tweet_object_list, window)
    basic_and_general_info.showGeneralInfo(tweet_object_list, window)

    sent.getSentiment(tweet_object_list, window)

    users_retweeted_most.showUsersRetweetedMost(tweet_object_list, window)

    #cloud.makeCloud(tweet_object_list, window)

if __name__ == '__main__':
	main()
