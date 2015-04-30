'''Authors:
    Josh Gibbons
    David
    Yun Nam Lin
'''

import twitter
import Tkinter
import tweepy
import datetime  # python datetime module
import imp
import sys
import json
import authKeys
from PIL import Image, ImageTk

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

#create gui
window = Tkinter.Tk()
window.geometry("1296x810+50+10")
window.title("Project name here");

#background
im = Image.open('bckg.jpg')
tkimage = ImageTk.PhotoImage(im)
myvar=Tkinter.Label(window,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)

window.mainloop()


def main():
    print("hello")
    #for user in tweepy.Cursor(api.followers, screen_name="GreatPowerKyle").items():
    #    print user.screen_name
    #for status in tweepy.Cursor(api.user_timeline, screen_name="GreatPowerKyle").items():
    #  print status.text

if __name__ == '__main__':
    main()

