# -*- encoding=utf-8 -*-

class User(object):
    '''The base class of user

    '''
    def __init__(self, name, email, nickname):
        self._name = name 
        self._email = email
        self._nickname = nickname


