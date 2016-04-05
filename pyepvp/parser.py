import requests
#import cfscrape
import re
import logging
import os, sys
import urllib
from html import unescape
from .regexp import *
from .exceptions import *

def parser(session, url, debugFlag=False):
    '''
    Retrieves and prepare a page from an url, can also save the html file debug purposes.
    '''
    if session == "debug":
        r = requests.get(url + "?langid=1")
    else:
        r = session.sess.get(url + "?langid=1")
    logging.debug("Size of " + url + ": " + str(len(r.content)))
    if htmlTag("title", r.content) == "Database Error":
        raise requestDatabaseException()
    content = r.content.decode('iso-8859-1')
    content = unescape(content)
    if debugFlag == True:
        debug(content)
    return content

def getSections(session):
    '''
    Retrieves all availble sections with their ID.
    '''
    content = parser(session, "https://www.elitepvpers.com/forum/main/announcement-board-rules-signature-rules.html")
    match = re.findall("value=\"(\d+)\".+\">\s+(\D+)<\/option>", content)
    return forumList(match)

def rankParser(content):
    '''
    Retrieves all ranks from the session user.
    '''
    ranks = re.findall("teamicons\/relaunch\/(\w+).png", content)
    ranks += ["user"]
    return ranks

def securityTokenParser(content):
    '''
    Retrieves securitytoken.
    '''
    securityToken = match("SECURITYTOKEN = \"(\S+)\";", content)
    return securityToken

def logoutHashParser(content):
    '''
    Only used to logout.
    '''
    logoutHash = match("href=\"login\.php\?do=logout&amp;logouthash=(\S+)\" onclick", content)
    return logoutHash

def userIDParser(content):
    '''
    Retrieves userid from user session.
    '''
    userID = match("members\/(\d+)-\D+>Your Profile", content)
    return userID

def getUpdates(session, url):
    '''
    Retrieves updates, used in the notifications property
    '''
    content = parser(session, url)
    session.notifications['unread_private_messages'] = int(match("<a href=\"private\.php\"\D+\">(\d+)<\/a>", content, 0))
    session.notifications['unread_vistor_messages'] = int(match("Unread Visitor Messages\D+\n.*tab=visitor_messaging#visitor_messagin\D+\">(\d+)<\/a>", content, 0))
    session.notifications['unapproved_vistor_messages'] = int(match("Unapproved Visitor Messages\D+\n.*tab=visitor_messaging#visitor_messagin\D+\">(\d+)<\/a>", content, 0))
    session.notifications['incoming_friend_requests'] = int(match("profile\.php\?do=buddylist#irc\">(\d+)<\/a>", content, 0))
    session.notifications['groups_request'] = int(match("href=\"group\.php\?do=requests\">(\d+)<\/a>", content, 0))
    session.notifications['groups_invitations'] = int(match("href=\"group\.php\?do=invitations\">(\d+)<\/a>", content, 0))
    session.notifications['unread_picture_comments'] = int(match("href=\"album\.php\?do=unread\">(\d+)<\/a>", content, 0))
    session.notifications['unapproved_picture_comments'] = int(match("href=\"album\.php\?do=moderated\">(\d+)<\/a>", content, 0))
    session.notifications['unapproved_group_messages'] = int(match("href=\"group\.php\?do=moderatedgms\">(\d+)<\/a>", content, 0))
    session.notifications['new_mentions'] = int(match("href=\"usertag\.php\?do=profilenotif&amp;tab=mentions\">(\d+)<\/a>", content, 0))
    session.notifications['new_post_quotes'] = int(match("href=\"usertag\.php\?do=profilenotif&amp;tab=quotes\">(\d+)<\/a>", content, 0))
    session.notifications['staff_changes'] = int(match("do=staffchanges\">(\d+)<\/a>", content, 0))
    session.notifications['subscribed_threads'] = int(match("New Subscribed Threads<span class=\"normal\">: \((\d+)\)<\/span>", content, 0))
    session.notifications['elite_gold'] = int(match("<span class=\"gold\">(\d+)<\/span", content, 0))

def htmlescape(text):
    '''
    The method name is self explanatory.
    '''
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
    '''
    Hacky workaround until I found a better method.
    '''
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
    '''
    Converts dict objects into strings used in POST requests.
    '''
    string = ""
    for item in dictvar:
        string += str(item) + "=" + str(dictvar[item]) + "&"
    return string[:-1]

class forumList:
    '''
    In workaround
    '''
    forumList = []

    def __init__(self, forumList):
        if forumList == []:
            raise emptyObjectException("forumList")
        self.forumList = forumList

    def isSet(self):
        if forumList == []:
            raise emptyObjectException("forumList")
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
