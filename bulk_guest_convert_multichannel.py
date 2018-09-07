import requests
import time
import json

# You will need to install the requests package for this script to function properly. 'pip install requests'
# This will convert users to multi channel guests and put them into one channel only.
# Note that there is little error logic in this script. If it fails, it may be because the email address is in correct or potentially other unforeseen errors. 

########################################################################
# Add API Tokens of admin users here. You will need two separate tokens.


# This is your xoxs token. To find this token, please follow the steps below:
# 1) Open up your Slack instance in a Google Chrome. You will need to be an owner or admin. 
# 2) Open up the developer console. You can do this by right clicking and selecting 'Inspect'
# 3) Select the 'Network' tab
# 4) Perform an action, such as staring a message
# 5) Click on the API request (stars.add for example) inside the network tab. Under the 'Headers' tab, scroll down to 'Request Payload'
# 6) In here, you'll see the 'xoxs-XXXXXXXX-XXXXXXXX' session token. Copy and paste that value below as 'api_token'
api_token = 'xoxs-123456789-123456789-123456789-123456789'

# You'll now need to generate a legacy token. You can do that here: https://api.slack.com/custom-integrations/legacy-tokens
# 1) Create a token for the workspace you are addressing. Copy and paste the xoxp token value below as 'api_token_users'

api_token_users = 'xoxp-123456789-123456789-123456789-123456789'

########################################################################

API_HEADER = {
    'Accept': 'application/json',
    'Authorization': api_token_users
}


# Add (email address, channel_id)
# In excel or google sheets, column A = email address, column b = Channel_ID of General. To find channel ID, open up Slack in a browser. 
######### Right click on 'General' and select 'Copy Link'. When you paste the link, you'll see a CHANNEL_ID with the format of 'CXXXXXXXX'. 
# In Column c, paste the following: =CONCATENATE("(",CHAR(34),A1,CHAR(34),",",CHAR(34),B1,CHAR(34),")",",")
# Copy and paste special (only values) into any column.  copy paste the values from column C below in the tuples array.  Don't forget to remove the final comma. 

user_ref_tuples = [
    ("email_address@email.com", "C09RAEFPU"),
    ("email_address2@email.com", "C09RAEFPU")
]




def update_single_channel_guest(email, channel_id):
    # return user_id
    scim_UsersUrl = 'https://api.slack.com/scim/v1/Users?filter=email+eq+%s' % (email)
    data = requests.get(url=scim_UsersUrl, headers=API_HEADER)
    json_data = data.json()
    
    dump = json.dumps(json_data)
    json1data = json.loads(dump)
    user_id = json1data['Resources'][0]['id']

    print "Trying user_id=%s with channel_id=%s" % (user_id, channel_id)
    scg_url = 'https://slack.com/api/users.admin.setRestricted?token=%s&user=%s&channel=%s&pretty=1' % (
        api_token, user_id, channel_id
    )
    time.sleep(0.1)

    response = requests.get(
        scg_url
    )
    if response.status_code != 200:
        print "Failed to update role for user_id=%s with code (%s): %s" % (
            user_id, response.status_code, response.text
        )
        return False
    else:
        print "Succeeded to update role for user_id=%s with response %s" % (
            user_id, response.text
        )
        return True

success = 0
fails = 0

for email, channel_id in user_ref_tuples:
    ret = update_single_channel_guest(email, channel_id)
    if ret:
        success += 1
    else:
        fails += 1


print "Success: %s.  Fails: %s" % (success, fails)
