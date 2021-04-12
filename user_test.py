import unittest
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_person = User('Yone','Yasuo','1234qwer')

    def test_user_init(self):
        self.assertEqual(self.new_person.nameone,"Yone")
        self.assertEqual(self.new_person.nametwo,"Yasuo")
        self.assertEqual(self.new_person.password,"1234qwer")