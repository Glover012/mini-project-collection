from websites import *
import os, sys
import threading
import requests
import validators

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
dataLock = threading.Lock()

websites = Websites("websites.txt")

class Client(threading.Thread):
    def __init__(self, threadName, websites):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.websites = websites
    
    def run(self):
        while True:
            dataLock.acquire()
            websiteToCheck = self.websites.getNextWebsiteToCheck()
            dataLock.release()
            if not websiteToCheck:
                break
            self.checkUrl(websiteToCheck)
        print(self.threadName, "ended")

    def checkUrl(self, data):
        try:
            validUrlFlag = validators.url(data["website"])
            if validUrlFlag:
                data["validUrlFlag"] = True
                response = requests.get(data["website"], allow_redirects=True)
                data["status-code"] = response.status_code 
            else:
                data["validUrlFlag"] = True
        except:
            data["exception"] = sys.exc_info()[0] 

        dataLock.acquire()
        self.websites.putWebsiteData(data)
        dataLock.release()

numThreads = 10
threadsList = []
num = 0

while num < numThreads:
    t = Client(f"T{num}", websites)
    threadsList.append(t)
    t.start()
    num+=1

for t in threadsList:
    t.join()

websites.saveReport()
print("Program ended")
