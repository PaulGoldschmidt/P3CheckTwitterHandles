import requests
from bs4 import BeautifulSoup

def check_handle(handle):
    url = f"https://twitter.com/{handle}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'lxml')
        print(soup.prettify())
        return "Claimed"
    elif response.status_code == 404:
        return "Not claimed"
    else:
        raise Exception(f"Unexpected status code: {response.status_code}")

handle = "example_handle"
result = check_handle(handle)
print(f"The handle @{handle} is {result}.")
