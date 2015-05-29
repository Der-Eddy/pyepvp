import requests
import bs4
import re

def parser(session, url):
    r = requests.get(url + "?langid=1", headers=session.headers, cookies=session.cookieJar)
    soup = bs4.BeautifulSoup(r.content)
    return soup

def getSections(session):
    soup = parser(session, "http://www.elitepvpers.com/forum/main/981452-hwid-generator-dev-tools-f-r-e-pvps-hwid-system.html")
    content = soup.find(attrs={"label": "Site Areas"}).parent.prettify()
    match = re.findall("value=\"(\d+)\">\s*(.+)\s*<\/option>", str(content))
    return forumList(match)

class forumList:
    forumList = []

    def __init__(self, forumList):
        self.forumList = forumList

    def isSet(self):
        if forumList == []:
            print ("Exception Placeholder")
            return 0

    def getByID(self, id):
        self.isSet()
        id = str(id)
        for i, k in self.forumList:
            if i == id:
                return k

    def getByName(self, name):
        self.isSet()
        for i, k in self.forumList:
            if k == name:
                return int(i)

    def isIn(self, string):
        if string in self.forumList:
            return True
        else:
            return False