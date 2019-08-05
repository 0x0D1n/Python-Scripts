##################################################################
# SCRIPT DOESNT HANDLE HTTPS - Anyways not really needed for CTF #
##################################################################

import requests as r
import sys


def main():

    if len(sys.argv) != 2:
        print("[+] Usage : ./<program> <URL> [+]")
        exit()

    # List of possible auto generated backup file extensions
    EXTENSIONS_BACKUP = ['.backup','.bck','.old','.save','.bak','.sav','~','.copy','.old','.orig','.tmp','.txt','.back','.bkp','.bac','.tar','.gz','.tar.gz','.zip','.rar']
    # URL to test
    url = ''

    cpt = 0

    if not sys.argv[1].startswith('http'):
        url = 'http://' + sys.argv[1]
    else:
        url = sys.argv[1]

    for i in range(0, len(EXTENSIONS_BACKUP)):
        #try: 
        req = r.get(url + EXTENSIONS_BACKUP[i])
        #except ConnectionError:
        #print("Connection can't be established - Wrong URL ?")
        #exit()

        if req.status_code == 200:
            print("Found existing backup file at : " +  url + EXTENSIONS_BACKUP[i] + " - CHECK IT OUT")
            cpt += 1

    if cpt == 0:
        print("No results found for : " + url)


main()
