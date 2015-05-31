from . import exceptions

def getShoutbox(session):
    exceptions.hasPermissions(session.ranks, exceptions.shoutboxUsers)
            
    r = requests.get("http://www.elitepvpers.com/forum/mgc_cb_evo.php?do=view_archives&page=1?langid=1", headers=session.headers, cookies=session.cookieJar)
    soup = bs4.BeautifulSoup(r.content)
    return soup

class shoutbox:
    topChatter = []
    allMessages = 0
    lastdayMessages = 0
    selfMessages = 0
    channel = "General"
    messages = []