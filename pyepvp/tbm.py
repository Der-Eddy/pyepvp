import logging
from . import exceptions

class tbm:
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
        if custom is not None:
            r = self.session.sess.get(custom)
        else:
            if self.secretWord == None:
                raise exception.tbmSecretwordException('receiveTransactions')
                return
            r = self.session.sess.get('https://www.elitepvpers.com/theblackmarket/api/transactions.php?u=' + self.session.userID + '&type=' + typeTrans + '&secretword=' + self.secretWord)
        if r.content == b'':
            raise exceptions.requestFailedTBMAPIException()
            return False
        return r.json()
