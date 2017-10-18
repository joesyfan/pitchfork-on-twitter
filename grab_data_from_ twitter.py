import encoding_fix
import tweepy
from twitter_authentication import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import time
import json

#Tweet = namedtuple('Tweet', 'text user_mentions retweet_count favorite_count')



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweets_d = {}

for n in range(1,163):
	search_results = api.user_timeline('pitchfork', page=n)
	#print(search_results)
	for t in search_results:
		tweetid = [t.id_str]
		properties = Tweet(t.text, t.entities['user_mentions'], t.retweet_count, t.favorite_count)
		tweets_d[t.id_str] = properties
		print (t.created_at)
	time.sleep(2)


with open('/Users/fanjun/Desktop/twitter/allresult.json', 'w') as fp:
    json.dump(tweets_d, fp)