import re
from . import exceptions
from . import parser
from . import regexp

def getShoutbox(session):
    exceptions.hasPermissions(session.ranks, exceptions.premiumUsers)
            
    content = parser.parser(session, "http://www.elitepvpers.com/forum/mgc_cb_evo.php?do=view_archives&page=1?langid=1")
    content = regexp.match(re.compile("<div class=\"cw1hforum\">(.+)<\/table>", re.DOTALL), content)
    parser.debug(content)
    messages = re.findall(re.compile(u"smallfont\">\n(.*)\n.*\n.*\n.*\n.*\n.*members\/(\d+).*html\">(.*)<\/a>\n.*\n.*\n.*\n.*\n(.*)"), content)
    messagesDict = {}
    return messages

class shoutbox:
    topChatter = []
    allMessages = 0
    lastdayMessages = 0
    selfMessages = 0
    channel = "General"
    messages = []