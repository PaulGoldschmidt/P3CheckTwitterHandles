import subprocess
import time
import requests
import json
from datetime import datetime

# Read credentials from the JSON file
with open("credentials.json", "r") as credentials_file:
    credentials = json.load(credentials_file)

telegram_bot_token = credentials["telegram_token"]
telegram_chat_id = credentials["telegram_chat_id"]

def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("check_usernames.log", "a") as log_file:
        log_file.write(f"{timestamp} - {message}\n")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {
        "chat_id": telegram_chat_id,
        "text": message
    }
    requests.post(url, data=payload)

def check_username(username):
    command = f"snscrape --max-results 1 twitter-user {username}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    error_output = result.stderr.decode('utf-8')

    log(output)  # Log the output
    log(error_output)  # Log the error output

    if not output.strip():  # If the output is empty, assume the username is not claimed
        return True
    else:
        return False

def main():
    with open("usernames.txt", "r") as usernames_file:
        usernames = [username.strip() for username in usernames_file.readlines()]

    available_usernames = []

    for username in usernames:
        if check_username(username):
            available_usernames.append(username)

        time.sleep(6)  # Cooldown to limit rate to 10 usernames per 60 seconds

    with open("last_available_usernames.txt", "r") as last_available_usernames_file:
        last_available_usernames = [username.strip() for username in last_available_usernames_file.readlines()]

    new_available_usernames = list(set(available_usernames) - set(last_available_usernames))

    if new_available_usernames:
        for username in new_available_usernames:
            message = f"Username {username} has become available."
            send_telegram_message(message)

    with open("last_available_usernames.txt", "w") as last_available_usernames_file:
        for username in available_usernames:
            last_available_usernames_file.write(f"{username}\n")

if __name__ == "__main__":
    main()