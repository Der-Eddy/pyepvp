import pyepvp.session
import pyepvp.parser
import re

with open("passwd.txt") as txt:
    passwd = txt.read()
#passwd = "my md5 hash password"
eddy = pyepvp.session.session("Der-Eddy", passwd, True)
print (eddy.securityToken)
forumList = pyepvp.parser.getSections(eddy)
print(forumList.getByID(205))
print(forumList.getByName("e*pvp News"))
print(forumList.isIn(('205', 'e*pvp News')))
#shoutbox = pyepvp.parser.getShoutbox(eddy)
#print(shoutbox.findAll(attrs={"align": "left"}))
eddy.logout()

guest = pyepvp.session.session("guest")
print (guest.securityToken)