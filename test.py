import pyepvp.session
import pyepvp.parser
import pyepvp.shoutbox
import pyepvp.privatemessages
import pyepvp.threads
import re
import logging, sys, os

def safeprint(s):
    try:
        print(s)
    except UnicodeEncodeError:
        print(s.encode('utf8', errors='replace').decode(sys.stdout.encoding))

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
with open(os.path.dirname(os.path.abspath(sys.argv[0])) + '/passwd.txt') as txt:
    passwd = txt.read()
#passwd = 'my md5 hash password'
secretWord = 'Super Secret Word'
eddy = pyepvp.session.session('Dere-Eddy', passwd, True, secretWord)
print (eddy.securityToken)
forumList = pyepvp.parser.getSections(eddy)
print(forumList.getByID(205))
print(forumList.getByName('e*pvp News'))
print(forumList.isIn(('205', 'e*pvp News')))
shoutbox = pyepvp.shoutbox.shoutbox(eddy)
print('--------------')
#print(shoutbox.messages[1])
for i in shoutbox.messages:
    safeprint((i['username'] + ' (' + i['usercolor'] + '): ' + i['message']).encode('utf-8'))
print('--------------')
#pyepvp.shoutbox.send(eddy, 'Ich bin ein Бot')
pm = pyepvp.privatemessages.privatemessage(eddy, 'Test', 'läuft bei dir\r\nyea', 'Dere-Eddy')
#pm.send()
print('--------------')
pms = pyepvp.privatemessages.privatemessages(eddy)
print('--------------')
thread = pyepvp.threads.thread(eddy, 'https://www.elitepvpers.com/forum/premium-main/3734972-der-l-ngste-e-pvp-premium-thread-xxii.html')
#print(thread.content)
eddy.logout()

guest = pyepvp.session.session('guest')
print (guest.securityToken)
guestForumList = pyepvp.parser.getSections(guest)
print(guestForumList.getByID(489))
