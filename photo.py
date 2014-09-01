# -*- coding=utf-8 -*-
import unittest
import exceptions 

class Photo(object):
    ''' A abstract class of Photo

        all of photo class will derived from this class
    '''
    _url = ""  # the url of photo
    _desc = "" # the description of photo
    _src = ""  # the source page of this photo

    def __init__(self, url, desc="", src=""):
        if not url:
            raise exceptions.ValueError("url can't be None") 
        _url = url.strip()
        _desc = desc.strip()
        _src = src.strip()
    
    def __repr__(self):
        return "<Photo@{0}>".format(self._url)

    def __str__(self):
        return __repr__()

    def __eq__(self, other):
        return self._url == other._url

class PhotoTest(unittest.TestCase):

    def test_eq(self):
        p1 = Photo("http://www.baidu.com/fav.icon")
        p2 = Photo("http://www.baidu.com/fav.icon", "baidu icon")
        self.assertEqual(p1,p2)
        p2 = Photo("http://google.com/fav.icon")
        self.assertNotEqual(p1,p2)

if __name__ == "__main__":
    unittest.main()
        
