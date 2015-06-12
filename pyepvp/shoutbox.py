import re
import logging
import requests
from . import exceptions
from . import parser
from . import regexp

channelDict = {"general": "0", "english": "1"}

def send(session, message, channel="general"):
    params = {
            "do": "ajax_chat",
            "channel_id": channelDict[channel],
            "chat": message,
            "cookieuser": "1",
            "s": "", 
            "securitytoken": session.securityToken
        }
    print (session.securityToken)
    r = requests.post("http://www.elitepvpers.com/forum/mgc_cb_evo_ajax.php", data=params, headers=session.headers, cookies=session.cookieJar)
    print (r.content)

class shoutbox:
    topChatter = []
    allMessages = 0
    lastdayMessages = 0
    selfMessages = 0
    channel = "general"
    messages = []

    def getShoutbox(self, session, site=[1, 1], channel="general"):
        exceptions.hasPermissions(session.ranks, exceptions.premiumUsers)
        messagesList = []
        for s in range(site[1], site[0] - 1, -1):
            content = parser.parser(session, "http://www.elitepvpers.com/forum/mgc_cb_evo.php?do=view_archives&page=" + str(s) + "?langid=1")
            content = regexp.match(re.compile("<div class=\"cw1hforum\">(.+)<\/table>", re.DOTALL), content)
            messages = re.findall(re.compile(u"smallfont\">\n(.*)\n.*\n.*\n.*\n.*\n.*members\/(\d+).*html\">(.*)<\/a>\n.*\n.*\n.*\n.*\n(.*)"), content)
            for shout in messages:
                if shout[2].find("</span>") == -1:
                    rank = "black"
                    username = shout[2]
                else:
                    p = re.compile("color:(\S+)>(.+)<\/span>")
                    matches = re.search(p, shout[2])
                    rank = matches.group(1)
                    username = matches.group(0)
                messageDict = {"time": shout[0], "userid": shout[1], "username": username, "usercolor": rank, "message": shout[3]}
                messagesList.append(messageDict)
        return messagesList

    def __init__(self, session, site=[1, 1], channel="general"):
        self.channel = channel
        self.messages = self.getShoutbox(session, site, self.channel)
        #logging.info(len(self.messages))

    def update(self, session, site=[1, 1]):
        self.messages = []
        self.messages = self.getShoutbox(session, site, self.channel)
