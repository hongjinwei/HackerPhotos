# -*- encoding=utf-8 -*-
from __future__ import print_function
import unittest

class User(object):
    '''The base class of user

    '''
    def __init__(self, name, email, nickname="newbee"):
        if not name:
            raise ValueError("name can't be None")
        self._name = name
        if not email:
            raise ValueError("email can't be None")
        self._email = email
        self._nickname = nickname

    def Update(self, name, email, nickname):

        if name:
            self._name = name

        if email:
            self._email = email

        if nickname:
            self._nickname = nickname
            
    def Get(self, property):
        try:
            return getattr(self, "_" + property.lower())
        except AttributeError as e:
            print(str(e))
            return None

    def Set(self, property, value):
        try:
            return setattr(self, "_" + property.lower(),value)
        except AttributeError as e:
            print(str(e))
            return None


class UserTest(unittest.TestCase):

    def setUp(self):
        self.user = User(name="liuchang", email="liuchang0812@gmail.com", nickname="chenchu")

    def test_Get(self):
        self.assertEqual(self.user.Get("name"), "liuchang")

    def test_Set(self):
        self.user.Set("nickname", "lc")
        self.assertEqual("lc", self.user._nickname)


if __name__ == "__main__":
    unittest.main()