import unittest
import pyepvp.session

class GuestSessionTestCase(unittest.TestCase):
    def setUp(self):
        self.session = pyepvp.session.session("guest")

    def test_getSecurityToken(self):
        self.assertEqual(self.session.securityToken, "guest")

if __name__ == '__main__':
    unittest.main()