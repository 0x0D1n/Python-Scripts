import requests as r
from bs4 import BeautifulSoup

def banner():
    print("[+] Fake Email generator based on : https://email-fake.com/")

    
def generateMail():
    url_generate_email = "https://email-fake.com/email-generator"
    url_retrieve_email = "https://email-fake.com/"

    req = r.get(url_generate_email)
    response = req.text
    soup = BeautifulSoup(response, features="lxml")

    find_email = soup.find(id="email_ch_text")
    email_generated = find_email.text
    print("[+] Email generated : " + email_generated)
    print("[+] Emails can be found at : " + url_retrieve_email + email_generated )

def main():
    banner()
    generateMail()

if __name__ == "__main__":
    main()
