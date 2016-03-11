import requests
import cfscrape
import xmlrpc.client
import hashlib
import time
import platform
import json
import os
import sys
import logging
from . import regexp
from . import exceptions
from . import parser
from . import tapatalk

class session:
    system = platform.system()
    with open(os.path.abspath(os.path.dirname(os.path.abspath(sys.argv[0])) + "/pyepvp/about.json"), "r") as file:
        about = json.load(file)
    userAgent = system.lower() + ":" + about["appID"] + "." + about["name"] + ":" + about["version"] + " (by " + about["author"] + ")"
    solaire = about["contributors"]
    sess = requests.session()
    sess.headers = {
        "User-Agent" : userAgent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    sess.mount("http://", cfscrape.CloudflareAdapter())
    sess.mount("https://", cfscrape.CloudflareAdapter())
    username = ""
    guestSession = False
    securityToken = ""
    secretWord = None
    userID = ""
    ranks = ["guest"]
    paramsGet = "&langid=1"
    notifications = {'last_update': 0,
                     'unread_private_messages': 0,
                     'unread_vistor_messages': 0,
                     'unapproved_visitor_messages': 0,
                     'incoming_friend_requests': 0,
                     'groups_request': 0,
                     'groups_invitations': 0,
                     'unread_picture_comments': 0,
                     'unapproved_picture_comments': 0,
                     'unapproved_group_messages': 0,
                     'new_mentions': 0,
                     'new_post_quotes': 0,
                     'staff_changes': 0,
                     'subscribed_threads': 0}

    def __init__(self, uname, passwd=None, md5bool=False, secretWord=None):
        logging.info("Running on" + exceptions.systemInfo())
        if passwd is not None: #Checks if User Session
            if md5bool == True:
                md5 = passwd
            else:
                md5 = hashlib.md5(passwd.encode("utf-8"));md5 = md5.hexdigest()
            self.username = uname
            self.login(uname, md5)
            if secretWord is not None:
                self.secretWord = secretWord
        elif uname == "guest": #Checks if Guest Session
            self.username = "guest"
            self.guestSession = True
            self.securityToken = "guest"
        else:
            raise exceptions.noAuthenticationException()

    def __del__(self):
        try:
            self.logout()
        except Exception:
            pass

    def login(self, uname, md5):
        loginnurl = "https://www.elitepvpers.com/forum/login.php?do=login" + self.paramsGet

        params = {
            "do": "login",
            "vb_login_md5password": md5,
            "vb_login_md5password_utf": md5,
            "s": "",
            "cookieuser": "1",
            "vb_login_username": uname,
            "security_token": "guest"
        }
        params = parser.dicttostr(params)
        r = self.sess.post(loginnurl, data=params, verify=True)

        content = parser.parser(self, "https://www.elitepvpers.com/forum/usercp.php")
        self.securityToken = parser.securityTokenParser(content)
        if self.securityToken == "guest":
            raise exceptions.invalidAuthenticationException()
        self.userID = parser.userIDParser(content)
        usercontent = parser.parser(self, "https://www.elitepvpers.com/forum/member.php?userid=" + self.userID)
        self.ranks = parser.rankParser(usercontent)
        logging.info("User-Session created: {0}:{1}:{2}".format(self.username, self.userID, self.ranks))

        self.tapatalk = tapatalk.tapatalk(uname, md5)

    def logout(self):
        self.sess.get("https://www.elitepvpers.com/forum/login.php?do=logout&logouthash=" + self.securityToken)
        self.tapatalk.logout()

    def updateNotifications(self):
        url = 'https://www.elitepvpers.com/forum/usercp.php'
        parser.getUpdates(session, url)
        self.notifications['last_update'] = time.time()
