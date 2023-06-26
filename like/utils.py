import tweepy

#Application key
CONSUMER_KEY = 'hrvbByPT3bjv4k72EpfWxURHV'
CONSUMER_SECRET = 'ftQjFa09AbLOV36SjogOgHDgNo96glrIs08PXm70gM5hqyMljc'

def get_api(request):
	# set up and return a twitter api object
	oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	access_key = request.session['access_key_tw']
	access_secret = request.session['access_secret_tw']
	oauth.set_access_token(access_key, access_secret)
	api = tweepy.API(oauth)
	return api