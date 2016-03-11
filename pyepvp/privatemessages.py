import logging
import re
import json
import urllib
from html import escape
from . import exceptions
from . import parser
from . import icons
from . import regexp

class privatemessage:
    def __init__(self, session, title, message, recipients, bccrecipients='', icon="0", pm_id='Not yet initiliazed', date='Not yet initiliazed', newFlag=False):
        self.session = session
        self.title = parser.asciiescape(title)
        self.message = parser.asciiescape(message)
        if recipients is list:
            self.recipients = str.join("; ", parser.asciiescape(recipients))
        else:
            self.recipients = recipients
        if bccrecipients is list:
            self.bccrecipients = str.join("; ", bccrecipients)
        else:
            self.bccrecipients = bccrecipients
        self.icon = icon
        self.id = pm_id
        self.date = date
        self.newFlag = newFlag

    def view(self):
        return self.title + ' - ' + self.message

    def send(self, savecopy="1"):
        paramsDict = {
            "do": "insertpm",
            "recipients": self.recipients,
            "bccrecipients": self.bccrecipients,
            "title": self.title,
            "message": self.message,
            "cookieuser": "1",
            "s": "",
            "iconid": self.icon,
            "signature": "1",
            "forward": "",
            "savecopy": savecopy,
            "pmid": "",
            "wysiwyg": "0",
            "sbutton": "Submit+Message",
            "parseurl": "1",
            "securitytoken": self.session.securityToken
        }
        #params = "recipients=" + self.recipients + "&bccrecipients=" + self.bccrecipients + "&title=" + self.title + "&message=" + self.message + "&wysiwyg=0&iconid=" + self.icon + "&s=&securitytoken=" + self.session.securityToken + "&do=insertpm&pmid=&forward=&sbutton=Submit+Message&savecopy=" + savecopy + "&signature=1&parseurl=1"
        params = parser.dicttostr(paramsDict)
        logging.info(params)
        r = self.session.sess.post("https://www.elitepvpers.com/forum/private.php?do=insertpm&pmid=", data=params)
        #recipients=Der-Eddy&bccrecipients=&title=L%E4uft&message=L%E4uft+bei%0D%0Adir%21+%3AD&wysiwyg=0&iconid=0&s=&securitytoken=&do=insertpm&pmid=&forward=&sbutton=Submit+Message&savecopy=1&signature=1&parseurl=1

class privatemessagesOLD:
    def __init__(self, session, folder=0, site=0):
        self.session = session
        if folder == 'Inbox' or folder == 'inbox':
            self.folder = '0'
        elif folder == 'Sent' or folder == 'sent':
            self.folder = '1'
        elif isinstance(folder, int):
            self.folder = str(folder)
        else:
            raise exceptions.pyepvpBaseException('Provide a valid foldername (Inbox or Sent) or folderid')
        self.site = str(site)
        self.url = 'https://www.elitepvpers.com/forum/private.php?s=&pp=50&folderid=' + self.folder + '&page=' + self.site
        self.getPMs()

    def getPMs(self):
        exceptions.hasPermissions(self.session.ranks, exceptions.user)
        pmsList = []
        content = parser.parser(self.session, self.url)
        content = regexp.match(re.compile("<div class=\"cw1hforum\">(.+)<\/table>", re.DOTALL), content)
        parser.debug(content)
        #for i in icons.icons:
        #    content = str.replace(str(content), "<img width=\"{0}\" height=\"{1}\" src=\"https://www.elitepvpers.com/forum/images/smilies/{2}\" border=\"0\" alt=\"\" title=\"{3}\" class=\"inlineimg\"/>".format(i[0], i[1], i[2], i[3]), i[4])
        pms = re.findall(re.compile(u'<td class=\"alt2">(.*?)<\/td>.*\n.*\n.*\n<span style=\"float:right\" class=\"smallfont\">(\S+)<\/span>\n<a rel=\"nofollow\" href=\"private\.php\?do=showpm&amp;pmid=(\d+)\">(.*?)<\/a>\n.*\n.*\n.*class=\"time\">(\S+)<\/span>\n.*location=\'members\/(\d+)-.*\">(.*?)<\/span>'), content)
        print(len(pms))
        for pm in pms:
            print (pm[2])

# <td class="alt2">(.*?)<\/td>.*\n.*\n.*\n<span style="float:right" class="smallfont">(\S+)<\/span>\n<a rel="nofollow" href="private\.php\?do=showpm&amp;pmid=(\d+)">(.*?)<\/a>\n.*\n.*\n.*class="time">(\S+)<\/span>\n.*location='members\/(\d+)-.*">(.*?)<\/span>

class privatemessages:
    def __init__(self, session, folder=0):
        self.session = session
        if folder == 'Inbox' or folder == 'inbox':
            self.folder = '0'
        elif folder == 'Sent' or folder == 'sent':
            self.folder = '1'
        elif isinstance(folder, int):
            self.folder = str(folder)
        else:
            raise exceptions.pyepvpBaseException('Provide a valid foldername (Inbox or Sent) or folderid')
        self.getPMs()

    def getPMs(self):
        exceptions.hasPermissions(self.session.ranks, exceptions.user)
        pms = self.session.tapatalk.proxy.get_box(self.folder, 0,  50)
        self.unread = pms["total_unread_count"]
        self.messagesCount = pms["total_message_count"]
        self.pms = pms["list"]
