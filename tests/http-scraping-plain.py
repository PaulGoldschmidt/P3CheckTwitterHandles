import requests

def is_handle_claimed(handle):
    url = f"https://twitter.com/{handle}"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        raise Exception(f"Unexpected status code: {response.status_code}")

handle = "example_handle"
if is_handle_claimed(handle):
    print(f"The handle @{handle} is claimed.")
else:
    print(f"The handle @{handle} is not claimed.")
