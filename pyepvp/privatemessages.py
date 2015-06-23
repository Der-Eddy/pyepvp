import logging
from html import escape
#from . import exceptions
#from . import parser

class privatemessages:
    def __init__(self, session, title, message, recipients, bccrecipients=[""], icon="0"):
        self.session = session
        self.title = title
        self.message = message
        if recipients is list:
            self.recipients = str.join("; ", recipients)
        else:
            self.recipients = recipients
        if bccrecipients is list:
            self.bccrecipients = str.join("; ", bccrecipients)
        else:
            self.bccrecipients = bccrecipients
        self.icon = icon

    def view(self):
        return self.title + self.message

    def send(self):
        params = {
            "do": "insertpm",
            "message": escape(self.message),
            "title": self.title,
            "recipients": self.recipients,
            "bccrecipients": "",
            "cookieuser": "1",
            "s": "",
            "iconid": self.icon,
            "signature": "1",
            "forward": "",
            "savecopy": "1",
            "pmid": "",
            "wysiwyg": "1",
            "sbutton": "Submit",
            "parseurl": "1",
            "securitytoken": self.session.securityToken
        }
        logging.info(params)
        self.session.sess.post("http://www.elitepvpers.com/forum/private.php?do=insertpm&pmid=", data=params)