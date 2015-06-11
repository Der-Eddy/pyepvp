import re
import logging
from . import exceptions
from . import parser
from . import regexp

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
                messageDict = {"time": shout[0], "userid": shout[1], "username": shout[2], "message": shout[3]}
                messagesList.append(messageDict)
        return messagesList

    def __init__(self, session, site=[1, 1], channel="general"):
        self.channel = channel
        self.messages = self.getShoutbox(session, site, self.channel)
        #logging.info(len(self.messages))

    def update(self, session, site=[1, 1]):
        self.messages = []
        self.messages = self.getShoutbox(session, site, self.channel)
