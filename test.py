import pyepvp.session
import pyepvp.parser
import pyepvp.shoutbox
import re
import logging, sys

def safeprint(s):
    try:
        print(s)
    except UnicodeEncodeError:
        print(s.encode('utf8').decode(sys.stdout.encoding))

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
with open("passwd.txt") as txt:
    passwd = txt.read()
#passwd = "my md5 hash password"
secretWord = "Super Secret Word"
eddy = pyepvp.session.session("Der-Eddy", passwd, True, secretWord)
print (eddy.securityToken)
forumList = pyepvp.parser.getSections(eddy)
print(forumList.getByID(205))
print(forumList.getByName("e*pvp News"))
print(forumList.isIn(('205', 'e*pvp News')))
shoutbox = pyepvp.shoutbox.shoutbox(eddy)
print("--------------")
print(shoutbox.messages[1])
for i in shoutbox.messages:
    safeprint((i["username"] + " (" + i["usercolor"] + "): " + i["message"]).encode("utf-8"))
print("--------------")
#pyepvp.shoutbox.send(eddy, "Ich bin ein Бot")
eddy.logout()

guest = pyepvp.session.session("guest")
print (guest.securityToken)
guestForumList = pyepvp.parser.getSections(guest)
print(guestForumList.getByID(489))