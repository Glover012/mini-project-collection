import os, sys, urllib.parse, validators, requests
from datetime import datetime

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)
#print(f"CWD: {os.getcwd()}\n")

print(f"Number of arguments: ", len(sys.argv))
print("Arguments list:", sys.argv) 

url = "https://google.com"

if len(sys.argv) > 1:
    url = sys.argv[1]

print(f"Website to download: {url}")

if not os.path.exists("./websites"):
    os.mkdir("websites")

parsedUrl = urllib.parse.urlparse(url)
print(parsedUrl) 

validFlag = validators.url(url)

if validFlag:
    print(f"Url {url} is valid")
else:
    print(f"Url {url} is invalid")
    raise Exception("Bad URL!") 

response = requests.get(url, allow_redirects=True) 

if response.ok == True:
    print(f"Correct response from server for url: {url}")
    now = datetime.now()
    dateString = now.strftime("%d.%m.%Y %H-%M-%S")
    print(dateString)
    fileToSave = f"./websites/{parsedUrl.netloc} {dateString}.html"
    print(fileToSave)
    fh = open(fileToSave, "wb")
    fh.write(response.content)
    fh.close()
