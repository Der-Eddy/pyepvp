import pyepvp.session
import pyepvp.parser
import pyepvp.shoutbox
import re
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
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
shoutbox = pyepvp.shoutbox.getShoutbox(eddy)
print(shoutbox.findAll(attrs={"align": "left"}))
eddy.logout()

guest = pyepvp.session.session("guest")
print (guest.securityToken)
guestForumList = pyepvp.parser.getSections(guest)
print(guestForumList.getByID(489))