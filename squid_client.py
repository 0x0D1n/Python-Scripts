import time
import base64

#Retrieve Squid proxy info
HOST_IP = input("[+] Enter squid host IP : ") or "10.10.10.200"
HOST_PORT = int(input("[+] Enter squid PORT (Default 3128) : ") or 3128)

CMD = input("[+] Enter command to execute (menu) : ") #or "menu"

#Default ones
HOST = "Host: " + HOST_IP
USER_AGENT = "User-Agent: squidclient/4.6"
ACCEPT = "Accept: */*"

URL = "GET cache_object://" + HOST_IP + ":" + str(HOST_PORT) + "/"+CMD+" HTTP/1.1"

#Credentials
creds = input("[+] Do you have any credentials ? [Y\\n]: ").lower() or "y"
if creds == "y":
    USERNAME = input("[+] Enter squidclient username (Default cachemgr): ") or "cachemgr"
    PASSWORD = input("[+] Enter squidclient password : ") or "Thah$Sh1"
    str_b64 = USERNAME + ":" + PASSWORD
    AUTHORIZATION = "Authorization: Basic " + base64.b64encode(bytes(str_b64.encode('ascii'))).decode('utf-8')
    crafted_url = URL + "\r\n" + USER_AGENT + "\r\n" + HOST + "\r\n" + ACCEPT + "\r\n" + AUTHORIZATION + "\n\n"  
else:
    crafted_url = URL + "\r\n" + USER_AGENT + "\r\n" + HOST + "\r\n" + ACCEPT + "\n\n"


def netcat(host, port, content):
    import socket
    print("[+] Creating connection with squid proxy ... ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    print("[+] Sending content ...")
    s.sendall(content)
    time.sleep(0.5)
    
    res = ""
    while True:
        data = s.recv(1024)
        if not data:
            break
        res += data.decode()
        print(res)
    print(res)
    print("[+] Connection closed ...")
    s.close()


netcat(HOST_IP, HOST_PORT, bytes(crafted_url.encode()))
#print(crafted_url)
