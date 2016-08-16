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

	header = "Dear Mr. Trump,"
	footer = "Sincerely, a Dissapointed Abe Lincoln."
	
	screenName = 'DisappointedAbe'
	
	responses = [
	"I died for THIS?!",
	"If I was alive today, I would shoot myself just because of you.",
	"I remember when the GOP actually had politicans in it. Guess not anymore."
	]

	def on_connect(self):
		print "Internet ok."

	def on_data(self, raw_data):

		api = API(self.auth)
		user = api.get_user(screen_name = self.screenName)
		tweetID = user.id

		newTweet = api.user_timeline(screen_name = 'DisappointedAbe',count=10)[0]
		oldTweet = newTweet #storage

		if newTweet is not oldTweet:
			oldTweet = ""

		responseNumber = 0

		#increment response number every time new tweet changes.

		replyText = '@DisappointedAbe ' + self.header + ' ' + self.responses[responseNumber] + ' ' + self.footer

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


