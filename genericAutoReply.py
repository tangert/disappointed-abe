from tweepy.utils import import_simplejson
json = import_simplejson()

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener

ckey = ''
csecret = ''
atoken = ''
asecret = ''

class autoReply(StreamListener):

	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)

	screenName = ''
	response = ''

	def on_connect(self):
		print "Internet ok."

	def on_data(self, raw_data):

		api = API(self.auth)
		user = api.get_user(screen_name = self.screenName)
		tweetID = user.id

		newTweet = api.user_timeline(screen_name = self.screenName,count=10)[0]
		replyText = '@' + screenName + ' ' + response

		#checking if tweet is longer than 140 (but shouldn't happen)
		if len(replyText) > 140:
			replyText = replyText[0:137] + '...'

		#send on an interval.
		api.update_status(status = replyText, in_reply_to_status_id= tweetID)

		return True


	def on_error(self, status):
		print status


if __name__ == '__main__':
    streamListener = trumpListener()
    twitterStream = Stream(streamListener.auth, streamListener)
    twitterStream.userstream(_with='DisappointedAbe')


