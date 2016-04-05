import logging
import xmlrpc.client
from .exceptions import *

class CookiesTransport(xmlrpc.client.Transport):
    '''
    Only used for the class tapatalk itself.
    http://stackoverflow.com/a/25876504
    '''
    def __init__(self):
        super().__init__()
        self._cookies = []

    def send_headers(self, connection, headers):
        if self._cookies:
            connection.putheader("Cookie", "; ".join(self._cookies))
        super().send_headers(connection, headers)

    def parse_response(self, response):
        for header in response.msg.get_all("Set-Cookie"):
            cookie = header.split(";", 1)[0]
            self._cookies.append(cookie)
        return super().parse_response(response)

class tapatalk:
    '''
    Logins into the Tapatalk API and stores the cookies for later use.
    '''
    def __init__(self, id, pw):
        self.proxy = xmlrpc.client.ServerProxy('https://www.elitepvpers.com/forum/mobiquo/mobiquo.php', CookiesTransport())
        loginMsg = self.proxy.login(id.encode(), pw.encode(), True)
        if loginMsg['result'] == False:
            raise invalidAuthenticationException()
        else:
            logging.info("Tapatalk-Session created")

    def logout(self):
        '''
        Logouts from the Tapatalk session, seems not to work everytime.
        '''
        try:
            self.proxy.logout_user()
        except Exception:
            pass
