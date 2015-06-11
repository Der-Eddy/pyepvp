import requests
import re
import logging
from . import regexp
from . import exceptions

def parser(session, url):
    r = requests.get(url + "?langid=1", headers=session.headers, cookies=session.cookieJar)
    logging.debug("Size of " + url + ": " + str(len(r.content)))
    if regexp.htmlTag("title", r.content) == "Database Error":
        raise exceptions.requestDatabaseException()
    content = r.content.decode('iso-8859-1')
    content = str.replace(str(content), "&amp;", "&")
    content = str.replace(str(content), "&nbsp;", "")
    content = str.replace(str(content), "&lt;", "")
    content = str.replace(str(content), "&gt;", "")
    return content

def getSections(session):
    content = parser(session, "http://www.elitepvpers.com/forum/main/announcement-board-rules-signature-rules.html")
    match = re.findall("value=\"(\d+)\".+\">\s+(\D+)<\/option>", content)
    return forumList(match)

def rankParser(content):
    ranks = re.findall("teamicons\/relaunch\/(\w+).png", content)
    return ranks

def securityTokenParser(content):
    securityToken = regexp.match("SECURITYTOKEN = \"(\S+)\";", content)
    return securityToken

def userIDParser(content):
    userID = regexp.match("members\/(\d+)-\D+>Your Profile", content)
    return userID

def debug(content):
    with open("debug", 'wb') as file_:
        file_.write(content.encode("utf-8"))

class forumList:
    forumList = []

    def __init__(self, forumList):
        if forumList == []:
            raise exceptions.emptyObjectException("forumList")
        self.forumList = forumList

    def isSet(self):
        if forumList == []:
            raise exceptions.emptyObjectException("forumList")
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
        return string in self.forumList