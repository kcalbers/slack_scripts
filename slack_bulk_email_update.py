import requests
import time
import json


print 
print "Initializing script to bulk update email addresses within Slack"
print
token = raw_input("Please input an admin token: ")
print

api_token = token
API_HEADER = {
    'Accept': 'application/json',
    'Authorization': api_token
}

# Add (email from, email to)
# in excel or google sheets, column A = email from, column b = email to
# column c, paste the following: =CONCATENATE("(",CHAR(34),A1,CHAR(34),",",CHAR(34),B1,CHAR(34),")",",")
# copy and paste special (only values) into any column.  copy paste that value from column C below.  remove final comma. 

user_ref_tuples = [
    ("test1@test.com", "test2@test.com"),
    ("test2@test.com", "test3@test.com")
]



def bulk_email_update(emailfrom, emailto):
 
    #Looking for User ID in order to pass that to SCIM API
    UsersUrl = 'https://slack.com/api/users.list?token=%s' % (api_token)
    data = requests.get(url=UsersUrl, headers=API_HEADER)
    json_data = data.json()
    dump = json.dumps(json_data)
    json1data = json.loads(dump)
    for i in json_data['members']:
        if not i['deleted']:
                if not i['is_bot']:
                    if (i['name'] != 'slackbot'):
                        if (i['profile']['email'] == '%s' % (emailfrom)):
                            user_id = (i['id'])


    print "Trying user_id=%s with email address=%s" % (user_id, emailfrom)

    scim_UsersUrl = 'https://api.slack.com/scim/v1/Users/%s' % (
        user_id
        ) 
    time.sleep(0.1)
    # Update email address 
    # patch to the scim api, updating the user
    data = json.dumps({
    "schemas": [
        "urn:scim:schemas:core:1.0"
    ],
    "id": user_id,
    "active": "true",
    "emails": [
        {
            "value": emailto,
            "primary": "true"
        }
    ]
}
    )
    patch_response = requests.patch(scim_UsersUrl, headers=API_HEADER, data=data)


    if patch_response.status_code != 200:
        print "Failed to update email address for email=%s with code (%s): %s" % (
            emailto, patch_response.status_code, patch_response.text
        )
        return False
    else:
        print "Succeeded to update email address for email=%s with response %s" % (
            emailto, patch_response.text
        )
        return True

success = 0
fails = 0

def run_script(success, fails):
    for emailfrom, emailto in user_ref_tuples:
        ret = bulk_email_update(emailfrom, emailto)
        if ret:
            success += 1
        else:
            fails += 1
    print "Success: %s.  Fails: %s" % (success, fails)

try:
    run_script(success, fails)
except:
    print "ERROR: One or more email addresses could not be found"



