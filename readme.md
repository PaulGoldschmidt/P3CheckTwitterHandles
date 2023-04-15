# P3CheckTwitterHandles (P3CTH)
The script reads a list of Twitter usernames from a file, checks if they are available using the `snscrape` command, compares the results to the last run, logs the output, sends a Telegram message if a username becomes available, and adds a cooldown to limit the rate at which usernames are checked.

## Function of the script
1. The script starts by importing the necessary modules and reading the Telegram bot token and chat ID from a JSON file.
2. The `log` function is defined, which writes log messages to a file named "check_usernames.log" with a timestamp.
3. The `send_telegram_message` function is defined, which sends a message using the Telegram bot API.
4. The `check_username` function is defined, which checks if a Twitter username is available using the `snscrape` command.
   a. If the output of the `snscrape` command is empty, it assumes the username is not claimed.
   b. The function logs both the output and error output of the `snscrape` command.
5. The `main` function is defined, which performs the following steps:
   a. Reads the list of Twitter usernames from the "usernames.txt" file.
   b. Iterates over the list of usernames and checks if they are available using the `check_username` function.
   c. Adds a cooldown of 6 seconds between checking usernames to limit the rate to 10 usernames per 60 seconds.
   d. Reads the last available usernames from the "last_available_usernames.txt" file.
   e. Compares the newly found available usernames to the last run's available usernames.
   f. Sends a Telegram message if a username has become available compared to the last run.
   g. Updates the "last_available_usernames.txt" file with the current run's available usernames.
6. The script executes the `main` function.

## Installation of the script

1. Install Python (version 3.6 or later) on your computer if you haven't already.
2. Install Git if you haven't already. You can follow this guide for installation: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
3. Open a terminal or command prompt and navigate to the directory where you want to clone the repository.
4. Run `git clone https://github.com/PaulGoldschmidt/P3CheckTwitterHandles.git` to clone the repository.
5. Change the directory to the cloned repository by running `cd P3CheckTwitterHandles`.
6. Install the `requests` library by running `pip install requests` in your terminal or command prompt.
7. Install `snscrape` by running `pip install snscrape`.
8. Copy the "credentials.json.example" file to "credentials.json" by running `cp credentials.json.example credentials.json`.
9. Update the "credentials.json" file with your actual Telegram bot token and chat ID.
   Replace `your_telegram_bot_token` and `your_telegram_chat_id` with your own Telegram bot token and chat ID, respectively.
   You can follow this tutorial to create a Telegram bot and obtain the necessary values: https://core.telegram.org/bots#creating-a-new-bot
10. Copy the "usernames.txt.example" file to "usernames.txt" by running `cp usernames.txt.example usernames.txt`.
11. Update the "usernames.txt" file with the list of Twitter usernames you want to check, one per line.
12. Create an empty file named "last_available_usernames.txt" in the same directory as "script.py".
13. Run the script using `python checktwitterhandle.py`.
14. The script will check the availability of the Twitter usernames, log the output, compare the results to the last run, and send a Telegram message if a username becomes available.
15. You can run the script periodically to monitor the availability of the Twitter usernames and receive updates via Telegram messages.

## Install as crontab
1. Follow the steps 1-12 from the previous instructions to set up the script and its dependencies.
2. Open a terminal or command prompt and navigate to the directory where the "P3CheckTwitterHandles" repository is cloned.
3. To set up the script as a cronjob, first open the crontab editor by running `crontab -e`.
4. Add a new line to the crontab file with the following format:
    ```bash
    * * * * * /path/to/python /path/to/P3CheckTwitterHandles/checktwitterhandle.py
    ```
    Replace `/path/to/python` with the path to the Python executable on your system, and `/path/to/P3CheckTwitterHandles` with the absolute path to the "P3CheckTwitterHandles" directory.

    For example, if Python is installed at `/usr/bin/python3` and the "P3CheckTwitterHandles" directory is at `/home/user/P3CheckTwitterHandles`, the line should look like this:
    ```bash
    * * * * * /usr/bin/python3 /home/user/P3CheckTwitterHandles/checktwitterhandle.py
    ```
    The `* * * * *` in the above line represents the cronjob schedule. Each field corresponds to

