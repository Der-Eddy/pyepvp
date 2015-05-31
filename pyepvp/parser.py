import requests
import bs4
import re
from . import regexp
from . import exceptions

def parser(session, url):
    r = requests.get(url + "?langid=1", headers=session.headers, cookies=session.cookieJar)
    soup = bs4.BeautifulSoup(r.content)
    if soup.title == "Database Error":
        raise exceptions.requestDatabaseException()
    return soup

def getSections(session):
    soup = parser(session, "http://www.elitepvpers.com/forum/main/981452-hwid-generator-dev-tools-f-r-e-pvps-hwid-system.html")
    content = soup.find(attrs={"label": "Site Areas"}).parent.prettify()
    match = re.findall("value=\"(\d+)\">\s*(.+)\s*<\/option>", str(content))
    return forumList(match)

def rankParser(content):
    soup = content.find(id="rank")
    if soup == None:
        return ["user"]
    ranks = re.findall("teamicons\/relaunch\/(\w+).png", soup.prettify())
    return ranks

def securityTokenParser(content):
    securityToken = regexp.match("SECURITYTOKEN = \"(\S+)\";", content)
    return securityToken

def userIDParser(content):
    userID = regexp.match("members\/(\d+)-\D+>Your Profile", content)
    return userID

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