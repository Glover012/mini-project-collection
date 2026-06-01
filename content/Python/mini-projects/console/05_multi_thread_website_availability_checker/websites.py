class Websites:
    def __init__(self, filename):
        self.filename = filename
        self.fileList = []
        self.reportList = []
        self.index = 0
        self.loadFile(filename)

    def loadFile(self, filename):
        fh = open(filename, "r")
        dataList = fh.readlines()
        fh.close()

        for v in dataList:
            v = "https://" + v.strip() 
            data = { "website": v, "status-code": -1 }
            self.fileList.append(data)
            data["index"] = len(self.fileList)-1

    def getNextWebsiteToCheck(self):
        if self.index >= len(self.fileList):
            return None 
        data = self.fileList[self.index]
        self.index += 1
        return data

    def putWebsiteData(self, data):
        if "index" in data and "website" in data and "status-code" in data:
            self.reportList.append(data)
        else:
            print(f"Bad keys in report: {data}")

    def saveReport(self):
        fh = open("report.txt", "w")
        for el in self.reportList:
            fh.write( f"{el["website"]} - {str(el)}\n")
        fh.close()
        print("Report saved!")
