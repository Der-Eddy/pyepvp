import unittest
import pyepvp.session
import pyepvp.parser

class GuestSessionTestCase(unittest.TestCase):
    def setUp(self):
        self.session = pyepvp.session.session("guest")

    def test_getSecurityToken(self):
        self.assertEqual(self.session.securityToken, "guest")
        guestForumList = pyepvp.parser.getSections(self.session)
        self.assertEqual(guestForumList.getByID(489), "Anime & Manga")

suite = unittest.TestLoader().loadTestsFromTestCase(GuestSessionTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)