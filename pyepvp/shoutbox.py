import re
import logging
from . import exceptions
from . import parser
from . import regexp
from . import icons

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
    session.sess.post("https://www.elitepvpers.com/forum/mgc_cb_evo_ajax.php", data=params)

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
        pHex = re.compile("color:(.*?)\">(.*?)<\/span>")
        pName = re.compile("color:(\S+)\">(.*?)<\/span>")
        for s in range(site[1], site[0] - 1, -1):
            content = parser.parser(session, "https://www.elitepvpers.com/forum/mgc_cb_evo.php?do=view_archives&page=" + str(s) + "?langid=1")
            content = regexp.match(re.compile("<div class=\"cw1hforum\">(.+)<\/table>", re.DOTALL), content)
            for i in icons.smilies:
                content = str.replace(str(content), "<img width=\"{0}\" height=\"{1}\" src=\"https://www.elitepvpers.com/forum/images/smilies/{2}\" border=\"0\" alt=\"\" title=\"{3}\" class=\"inlineimg\"/>".format(i[0], i[1], i[2], i[3]), i[4])
            messages = re.findall(re.compile(u"smallfont\">\n(.*)\n.*\n.*\n.*\n.*\n.*members\/(\d+).*html\">(.*)<\/a>\n.*\n.*\n.*\n.*\n(.*)"), content)
            for shout in messages:
                if shout[2].find("</span>") == -1:
                    rank = "black"
                    username = shout[2]
                else:
                    matches = re.search(pHex, shout[2])
                    if matches == None:
                        matches = re.search(pName, shout[2])
                    try:
                        rank = matches.group(1)
                    except AttributeError:
                        rank = "user"
                    try:
                        username = matches.group(2)
                    except AttributeError:
                        username = "undefined"
                messageDict = {"time": shout[0], "userid": shout[1], "username": username, "usercolor": rank, "message": shout[3]}
                messagesList.append(messageDict)
            if len(messagesList) < 15:
                logging.warn("List of shouts to short!")
                parser.debug(content)
        return messagesList

    def __init__(self, session, site=[1, 1], channel="general"):
        self.channel = channel
        self.messages = self.getShoutbox(session, site, self.channel)
        #logging.info(len(self.messages))

    def update(self, session, site=[1, 1]):
        self.messages = []
        self.messages = self.getShoutbox(session, site, self.channel)
