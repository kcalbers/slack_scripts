# slack_scripts
A list of random scripts that can be used for your test team.

# How to run the bulk user script

1. You'll need to install the requests package for python. Use an installer like pip.
- From a terminal: `curl -O https://bootstrap.pypa.io/get-pip.py`
2. Install pip
- From a terminal: `sudo python get-pip.py`
3. Install requests
- `sudo pip install requests` 
4. Ensure that you have an admin token for your Slack team. 
- https://api.slack.com/custom-integrations/legacy-tokens
5. Download the python script (.py) to your hard drive. 
6. From a terminal, run the program
- `python slack_create_50_users.py` 
