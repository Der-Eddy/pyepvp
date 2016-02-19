import re
import logging
#from bs4 import BeautifulSoup
from . import exceptions
from . import parser
from . import regexp

def getThread(session, url):
    content = parser.parser(session, url)

class thread:
    sites = 0
    title = ""
    creator = ""
    section = ""
    threadid = 0
    sticked = False
    visible = True
    is_open = True
    posts = []

    def __init__(self, session, url):
        p = re.compile("elitepvpers.com\/forum\/(\S+)\/(\d+)-\D+(\S+).html")
        match = re.search(p, url)
        self.section = match.group(1)
        self.threadid = match.group(2)
        content = parser.parser(session, self.getUrl())
        self.content = content

    def getUrl(self):
        #return "https://www.elitepvpers.com/forum/-/" + self.threadid +  "--.html"
        return "https://www.elitepvpers.com/forum/showthread.php?t=" + self.threadid

    def getLastUrl(self):
        return "https://www.elitepvpers.com/forum/-/" + self.threadid +  "---new-post.html"

class post:
    creator = ""
    title = None
    content = ""
    postid = 0
    date = 0
    thanks = ""
    visible = True
    ignored = False
    last_edit = None
