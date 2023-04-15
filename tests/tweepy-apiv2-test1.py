import tweepy

consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

def is_handle_claimed(handle):
    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret,
        access_token, access_token_secret
    )
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        user = api.get_user(handle)
        return True
    except tweepy.TweepError as e:
        if "User not found" in str(e):
            return False
        else:
            raise e

handle = "example_handle"
if is_handle_claimed(handle):
    print(f"The handle @{handle} is claimed.")
else:
    print(f"The handle @{handle} is not claimed.")
