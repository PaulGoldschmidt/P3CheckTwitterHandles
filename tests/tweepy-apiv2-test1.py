import os
import json
import tweepy

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
keys_path = os.path.join(parent_dir, "api-keys.json")

with open(keys_path) as f:
    keys = json.load(f)

bearer_token = keys["bearer_token"]

auth = tweepy.AppAuthHandler(keys["consumer_key"], keys["consumer_secret"])
api = tweepy.API(auth, wait_on_rate_limit=True)

handle = "example_handle"
try:
    user = api.get_user(handle)
    print(f"The handle @{handle} is claimed by user ID {user.id} and name {user.name}.")
except tweepy.TweepError as e:
    if "User not found" in str(e):
        print(f"The handle @{handle} is not claimed.")
