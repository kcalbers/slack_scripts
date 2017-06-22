import requests
import json

# in excel, column A = username
# column c = =CONCATENATE("[",CHAR(34),A1,"@test.com",CHAR(34),"]") -> note, change the email domain
# column E = =CONCATENATE("(",CHAR(34),A1,CHAR(34),",",C1,")",",")
# copy and paste special (only values) into any column.  copy paste that value below.  remove final comma. 


print
print "Initializing user create script"
print

token = raw_input('token?: ')

API_HEADER = {
	'Accept': 'application/json',
    'Authorization': token
}

# format below is userName, emailAddress.  Given name and family name are static for test.
user_ref_tuples = [
   ("Rasheeda",["Rasheeda@acme.com"],"Rasheeda","Brault"),
("Reanna",["Reanna@acme.com"],"Reanna","Provencal"),
("Kermit",["Kermit@acme.com"],"Kermit","Wacaster"),
("Dusti",["Dusti@acme.com"],"Dusti","Maciel"),
("Alona",["Alona@acme.com"],"Alona","Crowther"),
("Kaci",["Kaci@acme.com"],"Kaci","Cole"),
("Clemencia",["Clemencia@acme.com"],"Clemencia","Riegel"),
("Vilma",["Vilma@acme.com"],"Vilma","Stalvey"),
("Kelli",["Kelli@acme.com"],"Kelli","Heider"),
("Yon",["Yon@acme.com"],"Yon","Breland"),
("Sharen",["Sharen@acme.com"],"Sharen","Than"),
("June",["June@acme.com"],"June","Thon"),
("Pierre",["Pierre@acme.com"],"Pierre","Rodrigue"),
("Estefana",["Estefana@acme.com"],"Estefana","Holguin"),
("Exie",["Exie@acme.com"],"Exie","Tollett"),
("Precious",["Precious@acme.com"],"Precious","Crownover"),
("Donna",["Donna@acme.com"],"Donna","Louis"),
("Ardelia",["Ardelia@acme.com"],"Ardelia","Devers"),
("Ayana",["Ayana@acme.com"],"Ayana","Thigpen"),
("Josefina",["Josefina@acme.com"],"Josefina","Withrow"),
("Sigrid",["Sigrid@acme.com"],"Sigrid","Hankey"),
("Sharika",["Sharika@acme.com"],"Sharika","Wildermuth"),
("Ming",["Ming@acme.com"],"Ming","Barletta"),
("Sandra",["Sandra@acme.com"],"Sandra","Berryman"),
("Marcus",["Marcus@acme.com"],"Marcus","Mcpeek"),
("Trinity",["Trinity@acme.com"],"Trinity","Hurn"),
("Marguerita",["Marguerita@acme.com"],"Marguerita","Farrand"),
("Ena",["Ena@acme.com"],"Ena","Nabors"),
("Leonora",["Leonora@acme.com"],"Leonora","Pedroso"),
("Chan",["Chan@acme.com"],"Chan","Botello"),
("Rudy",["Rudy@acme.com"],"Rudy","Jewell"),
("Gricelda",["Gricelda@acme.com"],"Gricelda","Roher"),
("Elmer",["Elmer@acme.com"],"Elmer","Alfonso"),
("Luanna",["Luanna@acme.com"],"Luanna","Doherty"),
("Eliseo",["Eliseo@acme.com"],"Eliseo","Franck"),
("Major",["Major@acme.com"],"Major","Spalla"),
("Hisako",["Hisako@acme.com"],"Hisako","Rone"),
("Coralee",["Coralee@acme.com"],"Coralee","Haddon"),
("Brenna",["Brenna@acme.com"],"Brenna","Townsel"),
("Jeanice",["Jeanice@acme.com"],"Jeanice","Burroughs"),
("Jorge",["Jorge@acme.com"],"Jorge","Weekley"),
("Alaina",["Alaina@acme.com"],"Alaina","Manz"),
("Marianne",["Marianne@acme.com"],"Marianne","Aldinger"),
("Tierra",["Tierra@acme.com"],"Tierra","Battista"),
("Lura",["Lura@acme.com"],"Lura","Mcqueen"),
("Tuan",["Tuan@acme.com"],"Tuan","Joyner"),
("Charlena",["Charlena@acme.com"],"Charlena","Kimery"),
("Lasandra",["Lasandra@acme.com"],"Lasandra","Sarvis"),
("Vina",["Vina@acme.com"],"Vina","Gargiulo"),
("Deedee",["Deedee@acme.com"],"Deedee","Pasch")
]


def createUser(userName, emailAddress, firstName, lastName):
    print "Trying userName=%s with emailAddress=%s" % (userName, emailAddress)
    scim_UsersUrl = 'https://api.slack.com/scim/v1/Users/' 
  

    # post to the scim api, creating a user
    data = json.dumps({
    "schemas": [
        "urn:scim:schemas:core:1.0"
    ],
    "userName": userName,
    "emails": emailAddress,
    "name": {
        "givenName": firstName,
        "familyName": lastName
    }
	})
    post_response = requests.post(scim_UsersUrl, headers=API_HEADER, data=data)
   
    if post_response.status_code != 201:
        print "Failed user create userName=%s with code(%s)reason:%s" % (
            userName, post_response.status_code, post_response.text)
        return False
    else:
        print "Succeeded user create for userName=%s with response %s" % (
            userName, post_response.text
        )
        return True


success = 0
fails = 0

for userName, emailAddress, firstName, lastName in user_ref_tuples:
    ret = createUser(userName, emailAddress, firstName, lastName)
    if ret:
        success += 1
    else:
        fails += 1

print "Success: %s.  Fails: %s" % (success, fails)
