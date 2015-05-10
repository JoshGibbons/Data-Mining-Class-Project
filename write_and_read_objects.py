import tweepy
import json

def writeTweetObjectsToFile(api, user_name): 

 tweet_object_list = []

 # This loop will read either all of a users tweets or 3240 tweets (whichever is reached first) 
 with open('tweet_objects.txt', 'w') as out_file:
  for tweet in tweepy.Cursor(api.user_timeline, screen_name = user_name).items():
   out_file.write(json.dumps(tweet._json) + '\n')
   tweet_object_list.append(json.loads(json.dumps(tweet._json) + '\n'))  

 return tweet_object_list  

# This is only for reading from the text file - when using the app in real time this will not be called
def readJsonFile():

 tweet_object_list = []

 with open('tweet_objects.txt') as file:
  for line in file:
   json_obj = json.loads(line)
   tweet_object_list.append(json_obj)

   # Syntax for accessing attributes
   #print json_obj["text"]
   #print tweet_object_list[0]["text"]
 return tweet_object_list
