from tweepy.utils import import_simplejson
json = import_simplejson()

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import API
from tweepy.streaming import StreamListener

ckey = 'JUo1JwXJXNuFOmbrjboKC7Iz9'
csecret = 'zFDQKK4vcdlIuIJJH6453iJgGlVpRYgg4sws1MKORZG7b0LXWE'
atoken = '762753721986060288-YQPemCSDa4w1c3q7tw4YFmG6xf6i52B'
asecret = '2wNgl0ezFLqJu0dswE3ukmNySxl2LlFj6J7PosTiVUlHf'

class trumpListener(StreamListener):

	#trumpID = '25073877'

	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)

	#header = "Dear Mr. Trump,"
	footer = "Sincerely, a Dissapointed Abe Lincoln."

	responses = ["Test."]

	trump = 'realDonaldTrump'
	test = 'DisappointedAbe'

	def on_connect(self):
		print "Internet ok."

	def on_data(self, raw_data):

		api = API(self.auth)
		user = api.get_user(screen_name = self.test)
		tweetID = user.id

		newTweet = api.user_timeline(screen_name = self.test,count=10)[0]
		oldTweet = api.user_timeline(screen_name = self.test,count=10)[1]
		newTweetID = newTweet.id
		
		replyText = '@DisappointedAbe ' + self.responses[0] + ' ' + self.footer

		#checking if tweet is longer than 140 (but shouldn't happen)
		if len(replyText) > 140:
			replyText = replyText[0:137] + '...'

		api.update_status(status = replyText, in_reply_to_status_id= newTweetID)
		return False


	def on_error(self, status):
		print status
		return False


if __name__ == '__main__':
    streamListener = trumpListener()
    twitterStream = Stream(streamListener.auth, streamListener)
    twitterStream.userstream(_with='DisappointedAbe')


