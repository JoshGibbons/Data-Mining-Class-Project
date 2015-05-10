'''
Authors:
Josh Gibbons
David
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
import basicInfo
import twitter      
import Tkinter
from PIL import Image, ImageTk
import datetime  # python datetime module      
imp.reload(sys)
sys.setdefaultencoding("utf-8")
# utf check

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

username = 'gavinfree'

def main():
 
 interface.createGUI()
 
 # def getUserData(username, window):
 # print(username)

 # This generates the 'tweet_objects.txt' and returns tweet_object_list
 #tweet_object_list = write_and_read_objects.writeTweetObjectsToFile(api, username)

 # Only used for testing (when you have previously generated 'tweet_objects.txt' don't exceed your access limit)
 #tweet_object_list = write_and_read_objects.readJsonFile()
 
 #for tweet in tweet_object_list:
  #print tweet["text"]
  #pass
 
 #basic_and_general_info.showBasicInfo(tweet_object_list)
 #basic_and_general_info.showGeneralInfo(tweet_object_list) 

 #users_retweeted_most.showUsersRetweetedMost(tweet_object_list)

 # Storing a list of statuses

 '''
 tweetStatuses = []
 count = 0
 for tweet in tweet_object_list:
  tweetStatuses.append(tweet['text'])
  count += 1
  if count > 99:
   break
 '''

 #sent.getSentiment(tweetStatuses, window)

 #for user in tweepy.Cursor(api.followers, screen_name = "GreatPowerKyle").items(): #print user.screen_name

if __name__ == '__main__':
    main()
