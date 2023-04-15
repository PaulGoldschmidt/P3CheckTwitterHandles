import snscrape.modules.twitter as sntwitter
from snscrape.modules.twitter import TwitterUser as user
from requests.exceptions import HTTPError

# Ask for user input for the Twitter username to check
username = input("Enter a Twitter username to check: ")

# Try to scrape the Twitter profile for the given username
try:
    user_info = user(username)
    print(f"The username '{username}' is already taken.")
except HTTPError:
    print(f"The username '{username}' is available.")
