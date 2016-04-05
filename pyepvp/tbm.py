import logging
from .exceptions import *

class tbm:
    '''
    Has some The Black Market features, needs an secretword for the most of them.
    '''
    secretWord = None

    def __init__(self, session, secretword=None):
        self.session = session
        if secretword == None and session.secretWord == None:
            logging.info("No Secretword defined, some TBM functions are not available!")
        elif session.secretWord == None:
            self.secretWord = secretword
        else:
            self.secretWord = session.secretWord

    def retrieveTransactions(self, typeTrans='all', custom=None):
        '''
        Retrieves the JSON for the provided type of transactions, needs a secretword in order to work.
        '''
        if custom is not None:
            r = self.session.sess.get(custom)
        else:
            if self.secretWord == None:
                raise tbmSecretwordException('receiveTransactions')
                return
            r = self.session.sess.get('https://www.elitepvpers.com/theblackmarket/api/transactions.php?u=' + self.session.userID + '&type=' + typeTrans + '&secretword=' + self.secretWord)
        if r.content == b'':
            raise erequestFailedTBMAPIException()
            return False
        return r.json()
