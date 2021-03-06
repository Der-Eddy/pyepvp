# -*- coding: utf-8 -*-
import pyepvp
import re
import logging, sys, os
import urllib.parse

def safeprint(s):
    try:
        print(s)
    except UnicodeEncodeError:
        print(s.encode('utf8', errors='replace').decode(sys.stdout.encoding))

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
with open(os.path.dirname(os.path.abspath(sys.argv[0])) + '/passwd.txt') as txt:
    passwd = txt.read()
#passwd = 'my md5 hash password'
with open(os.path.dirname(os.path.abspath(sys.argv[0])) + '/secretword.txt') as txt:
    secretWord = txt.read()
#secretWord = 'Super Secret Word'
eddy = pyepvp.session('Der-Eddy', passwd, True, secretWord)
print(eddy.securityToken)
print('Your Elite*gold: {0}'.format(eddy.elite_gold))

forumList = pyepvp.getSections(eddy)
print(forumList.getByID(205))
print(forumList.getByName('e*pvp News'))
print(forumList.isIn(('205', 'e*pvp News')))

print('--------------')
sb = pyepvp.shoutbox(eddy)
#print(shoutbox.messages[1])
for i in sb.messages:
    safeprint((i['username'] + ' (' + i['usercolor'] + '): ' + i['message']).encode('utf-8'))
print('--------------')
#pyepvp.shoutbox.send(eddy, 'Ich bin ein Böt')

#pm = pyepvp.privatemessage(eddy, 'Test tästa', 'Was läuft bei dir\r\ny%E4', 'Dere-Eddy', icon='2').send()

print('Unread Messages:')
pms = pyepvp.privatemessages(eddy)
for message in pms.pms:
    if message['msg_state'] == 1:
        print(message)
print('--------------')

transactions = pyepvp.tbm(eddy)
tbmJSON = transactions.retrieveTransactions('received')
for i in tbmJSON:
    if int(i['amount']) >= 30 and i['note'] == 'Katze':
        print(i)

print('--------------')

print(eddy.updateNotifications())

#thread = pyepvp.thread(eddy, 'https://www.elitepvpers.com/forum/premium-main/3734972-der-l-ngste-e-pvp-premium-thread-xxii.html')
#print(thread.content)

eddy.logout()

with pyepvp.session('guest') as guest:
    print (guest.securityToken)
    guestForumList = pyepvp.getSections(guest)
    print(guestForumList.getByID(489))

test = pyepvp.user('Der-Eddy', '984054')
print(test.ranks)
