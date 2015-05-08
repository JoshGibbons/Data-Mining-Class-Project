from twython import Twython	# Required to retrieve Users/show.json
from datetime import datetime
import authKeys

def showBasicInfo(userName):

    #Creating a new Twython object
    show_user_twython = Twython(app_key = authKeys.getA(),
                        app_secret = authKeys.getB(),
                        oauth_token = authKeys.getC(),
                        oauth_token_secret = authKeys.getD())

    #Creating the show_user json dictionary
    show_user = show_user_twython.show_user(screen_name=userName)

    print 'Name: ' + show_user.get('name')				# Name of the account owner
    print 'Screen Name: ' + show_user.get('screen_name')		# Screen name # This is a bit redundant
    print 'User ID: ' + show_user.get('id_str')			# Numeric id of the account

    #print 'Account Creation: ' + show_user.get('created_at')	# Date the account was created in twitter datetime format
    # Converting from twitter datetime format to python datetime format
    account_creation = datetime.strptime(show_user.get('created_at'), '%a %b %d %H:%M:%S +0000 %Y')
    print 'Account Creation: {:%m-%d-%Y}'.format(account_creation)	# Formatting
    age = (datetime.now() - account_creation).days			# Account Age in days
    print 'Account Age: ' + str(age / 365) + ' Years, ' + str(age % 365) + ' days'	# Formatting

    #print 'Account Location: ' + show_user.get('location')
    #  Users location # This requires decoding
    # Total number of tweets
    print 'Total Tweets: ' + str(show_user.get('statuses_count'))
    # Average number of tweets each day
    print 'Average Number of Tweets Daily: ' + str('%.2f'%(float(show_user.get('statuses_count')) / float(age)))
