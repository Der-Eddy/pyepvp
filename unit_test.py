import unittest
import pyepvp

class GuestSessionTestCase(unittest.TestCase):
    def setUp(self):
        self.session = pyepvp.session("guest")

    def test_getSecurityToken(self):
        self.assertEqual(self.session.securityToken, "guest")

    def test_getSections(self):
        guestForumList = pyepvp.getSections(self.session)
        self.assertEqual(guestForumList.getByID(489), "Anime & Manga")

    def test_getInsufficientAccessException(self):
        self.assertRaises(pyepvp.insufficientAccessException, pyepvp.shoutbox.getShoutbox, self.session)


suite = unittest.TestLoader().loadTestsFromTestCase(GuestSessionTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)
