import tweepy

# set up authentication
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

# set up API client
api = tweepy.Client(auth=auth, api_version="2")

# test GET /2/users/me endpoint
try:
    user = api.get_user("me")
    print(f"User ID: {user.id}")
    print(f"User Name: {user.name}")
    print(f"User Screen Name: {user.username}")
    print(f"User Description: {user.description}")
    print(f"User Location: {user.location}")
    print(f"User Followers Count: {user.public_metrics.followers_count}")
except tweepy.TweepError as e:
    print(f"Error: {e}")
