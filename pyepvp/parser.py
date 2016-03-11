import requests
#import cfscrape
import re
import logging
import os, sys
import urllib
from html import unescape
from . import regexp
from . import exceptions

def parser(session, url, debugFlag=False):
    if session == "debug":
        r = requests.get(url + "?langid=1")
    else:
        r = session.sess.get(url + "?langid=1")
    logging.debug("Size of " + url + ": " + str(len(r.content)))
    if regexp.htmlTag("title", r.content) == "Database Error":
        raise exceptions.requestDatabaseException()
    content = r.content.decode('iso-8859-1')
    content = unescape(content)
    if debugFlag == True:
        debug(content)
    return content

def getSections(session):
    content = parser(session, "https://www.elitepvpers.com/forum/main/announcement-board-rules-signature-rules.html")
    match = re.findall("value=\"(\d+)\".+\">\s+(\D+)<\/option>", content)
    return forumList(match)

def rankParser(content):
    ranks = re.findall("teamicons\/relaunch\/(\w+).png", content)
    ranks += ["user"]
    return ranks

def securityTokenParser(content):
    securityToken = regexp.match("SECURITYTOKEN = \"(\S+)\";", content)
    return securityToken

def userIDParser(content):
    userID = regexp.match("members\/(\d+)-\D+>Your Profile", content)
    return userID

def getUpdates(session, url):
    content = parser(session, url)
    session.notifications['unread_private_messages'] = int(regexp.match("<a href=\"private\.php\"\D+\">(\d+)<\/a>", content, 0))
    session.notifications['unread_vistor_messages'] = int(regexp.match("Unread Visitor Messages\D+\n.*tab=visitor_messaging#visitor_messagin\D+\">(\d+)<\/a>", content, 0))
    session.notifications['unapproved_vistor_messages'] = int(regexp.match("Unapproved Visitor Messages\D+\n.*tab=visitor_messaging#visitor_messagin\D+\">(\d+)<\/a>", content, 0))
    session.notifications['incoming_friend_requests'] = int(regexp.match("profile\.php\?do=buddylist#irc\">(\d+)<\/a>", content, 0))
    session.notifications['groups_request'] = int(regexp.match("href=\"group\.php\?do=requests\">(\d+)<\/a>", content, 0))
    session.notifications['groups_invitations'] = int(regexp.match("href=\"group\.php\?do=invitations\">(\d+)<\/a>", content, 0))
    session.notifications['unread_picture_comments'] = int(regexp.match("href=\"album\.php\?do=unread\">(\d+)<\/a>", content, 0))
    session.notifications['unapproved_picture_comments'] = int(regexp.match("href=\"album\.php\?do=moderated\">(\d+)<\/a>", content, 0))
    session.notifications['unapproved_group_messages'] = int(regexp.match("href=\"group\.php\?do=moderatedgms\">(\d+)<\/a>", content, 0))
    session.notifications['new_mentions'] = int(regexp.match("href=\"usertag\.php\?do=profilenotif&amp;tab=mentions\">(\d+)<\/a>", content, 0))
    session.notifications['new_post_quotes'] = int(regexp.match("href=\"usertag\.php\?do=profilenotif&amp;tab=quotes\">(\d+)<\/a>", content, 0))
    session.notifications['staff_changes'] = int(regexp.match("do=staffchanges\">(\d+)<\/a>", content, 0))
    session.notifications['subscribed_threads'] = int(regexp.match("New Subscribed Threads<span class=\"normal\">: \((\d+)\)<\/span>", content, 0))

def debug(content):
    logging.info("Debug Content Length: " + len(content))
    with open(os.path.dirname(os.path.abspath(sys.argv[0])) + "/debug.html", 'wb') as file_:
        file_.write(content.encode("utf-8"))

def htmlescape(text):
    #text = (text).decode('utf-8')

    from html.entities import codepoint2name
    d = dict((unichr(code), u'&%s;' % name) for code,name in codepoint2name if code!=38) # exclude "&"
    if u"&" in text:
        text = text.replace(u"&", u"&amp;")
    for key, value in d.iteritems():
        if key in text:
            text = text.replace(key, value)
    return text

def asciiescape(text):
    replace = (
        ["\\xf6", "%F6"],
        ["\\xfc", "%FC"],
        ["\\xe4", "%E4"],
        ["\\xdf", "%DF"],
        ["ö", "%F6"],
        ["ü", "%FC"],
        ["ä", "%E4"],
        ["ß", "%DF"]
    )
    for i in replace:
        text = text.replace(i[0], i[1])
    return text

def dicttostr(dictvar):
    string = ""
    for item in dictvar:
        string += str(item) + "=" + str(dictvar[item]) + "&"
    return string[:-1]

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
