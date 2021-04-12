import unittest
from credentials import Creds
import pyperclip

class TestCreds(unittest.TestCase):

    def setUp(self):
        self.new_credential = Creds('Instagram', '1234qwer')

    def test_init(self):
        self.assertEqual(self.new_credential.account,'Instagram')
        self.assertEqual(self.new_credential.password,'1234qwer')

    def test_save_cred(self):
        self.new_credential.save_creds()
        self.assertEqual(len(Creds.creds_list),1)

    def tearDown(self):
        Creds.creds_list = []