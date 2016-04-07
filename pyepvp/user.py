import logging
from .regexp import *
from .exceptions import *
from .parser import *

class user:
    '''
    Represents an Elitepvpers user.
    '''
    #__slots__ = ['name', 'id', 'url', 'ranks', 'posts', 'thanks', 'given_thanks', 'posts_per_days', 'profil_messages', 'blog_posts', 'join_date', 'referrals', 'elite_gold', 'ratings', 'mediations']
    name = ''
    id = None
    url = None
    ranks = ['user']
    join_date = '1970/01/01'
    posts = 0
    thanks = 0
    given_thanks = 0
    posts_per_days = 0
    profil_messages = 0
    blog_posts = 0
    referrals = 0
    elite_gold = 0
    ratings = [0, 0, 0]
    mediations = [0, 0]

    def __init__(self, username, id=None):
        self.name = username
        if id is not None:
            self.id = id
            self.url = 'https://www.elitepvpers.com/forum/member.php?u=' + self.id
            self._update()

    def __str__(self):
        return self.id

    def _update(id=None):
        '''
        Fills the user class with informations about the user.
        '''
        if id is not None:
            self.id = id
        elif self.id is None and id is None:
            #getting somehow the id
            pass
        usercontent = parser('debug', self.url)
        self.ranks = rankParser(usercontent)
