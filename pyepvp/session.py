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
from .regexp import *
from .exceptions import *
from .parser import *
from .tapatalk import *
from .user import *
from . import __version__, __title__, __author__

class session:
    '''
    Needed for several methods, logs into an elitepvpers user account and provides several useful informations about that account.
    '''
    system = platform.system()
    userAgent = "{0}:{1}:{2} (by {3})".format(system.lower(), __title__, __version__, __author__)
    sess = cfscrape.create_scraper()
    sess.headers = {
        "User-Agent" : userAgent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    username = ""
    guestSession = False
    securityToken = ""
    logoutHash = ""
    secretWord = None
    userID = ""
    ranks = ["guest"]
    paramsGet = "&langid=1"
    refreshTime = 30
    _notifications = {'last_update': 0,
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
    _elite_gold = 0
    @property
    def elite_gold(self):
        if self._notifications['last_update'] + self.refreshTime < time.time():
            self.updateNotifications()
        return self._elite_gold

    @elite_gold.setter
    def elite_gold(self, value):
        self._elite.gold = value

    def __enter__(self):
        return self


    def __init__(self, uname='guest', passwd=None, md5bool=False, secretWord=None):
        logging.info("Running on" + systemInfo())
        if passwd is not None: #Checks if User Session
            if md5bool == True:
                md5 = passwd
            else:
                md5 = hashlib.md5(passwd.encode("utf-8"));md5 = md5.hexdigest()
            self.username = uname
            self._login(uname, md5)
            if secretWord is not None:
                self.secretWord = secretWord
        elif uname == "guest": #Checks if Guest Session
            self.username = "guest"
            self.guestSession = True
            self.securityToken = "guest"
        else:
            raise noAuthenticationException()

    def __exit__(self, *kwargs):
        self.__del__()

    def __del__(self):
        try:
            self._logout()
        except Exception:
            pass

    def _login(self, uname, md5):
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
        params = dicttostr(params)
        r = self.sess.post(loginnurl, data=params, verify=True)

        content = parser(self, "https://www.elitepvpers.com/forum/usercp.php")
        self.securityToken = securityTokenParser(content)
        self.logoutHash = logoutHashParser(content)
        if self.securityToken == "guest":
            raise invalidAuthenticationException()
        self.userID = userIDParser(content)
        usercontent = parser(self, "https://www.elitepvpers.com/forum/member.php?userid=" + self.userID)
        self.ranks = rankParser(usercontent)
        logging.info("User-Session created: {0}:{1}:{2}".format(self.username, self.userID, self.ranks))
        self.updateNotifications()

        self.tapatalk = tapatalk(uname, md5)

    def logout(self):
        '''
        Logout the user session and destroys itself.
        '''
        self.__del__()

    def _logout(self):
        self.sess.get("https://www.elitepvpers.com/forum/login.php?do=logout&logouthash=" + self.logoutHash)
        self.tapatalk.logout()

    def updateNotifications(self):
        '''
        Updates the notifications of the session user and returns them.
        '''
        url = 'https://www.elitepvpers.com/forum/usercp.php'
        getUpdates(session, url)
        self._notifications['last_update'] = time.time()
        logging.info('Updated notifications - {0}'.format(time.time()))
        return self._notifications
