from . import exceptions
from . import parser

def getShoutbox(session):
    exceptions.hasPermissions(session.ranks, exceptions.shoutboxUsers)
            
    soup = parser.parser(session, "http://www.elitepvpers.com/forum/mgc_cb_evo.php?do=view_archives&page=1?langid=1")
    return soup

class shoutbox:
    topChatter = []
    allMessages = 0
    lastdayMessages = 0
    selfMessages = 0
    channel = "General"
    messages = []