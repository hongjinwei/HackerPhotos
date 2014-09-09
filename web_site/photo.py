# -*- coding=utf-8 -*-
import unittest
import exceptions 
import sae.kvdb
import uuid
import tornado.ioloop
import tornado.web
import re

class Photo(object):
    ''' A abstract class of Photo

        all of photo class will derived from this class
    '''
    _url = ""  # the url of photo
    _desc = "" # the description of photo
    _src = ""  # the source page of this photo
    _id = ""   # the unique id of this photo

    def __init__(self, url, desc="", src=""):
        if not url:
            raise exceptions.ValueError("url can't be None") 
        _url = url.strip()
        _desc = desc.strip()
        _src = src.strip()
        _id = 'photo_' + uuid.uuid1()
    
    def __repr__(self):
        return "<Photo@{0}>".format(self._url)

    def __str__(self):
        return __repr__()

    def __eq__(self, other):
        return self._url == other._url

    def set(self, id, url):
        kv = sae.kvdb.KVClient()  
        if not id or not url:
            id = self.id
            url = self.url
        if not re.match(id, 'photo_'):
            raise exceptions.ValueError("pic id should predixed with 'photo_'")
        kv.set(id,url)
        kv.disconnect_all()
    
    def get(self, id):
        kv = sae.kvdb.KVClient()
        if not id:
            id = self.id
        url = kv.get(id)
        if not url:
            raise exceptions.ValueError("No pic id: " + self.id)
        return url
    
    def delete(self):
        kv = sae.kvdb.KVClient()
        kv.delete(self.id)

    def replace(self, newurl):
        if not newurl:
            raise exceptions.ValueError("new url can't be None")
        kv = sae.kvdb.KVClient()
        kv.replace(self.id, newurl)

class PhotoHanlder(tornado.web.RequestHandler):
    def get(self): 
        photo_id = self.get_argument("filename")
        photo = Photo()
        return photo.get(photo_id)
   
    def post(self)
        url = self.get_argument("url")
        desc = self.get_argument("desc")
        src = self.get_argument("src")
        photo = Photo(url, desc, src)
        photo.set()

application = tornado.web.Application([
    (r'/photo/(.*)', PhotoHanlder)
    ])

class PhotoTest(unittest.TestCase):

    def test_eq(self):
        p1 = Photo("http://www.baidu.com/fav.icon")
        p2 = Photo("http://www.baidu.com/fav.icon", "baidu icon")
        self.assertEqual(p1,p2)
        p2 = Photo("http://google.com/fav.icon")
        self.assertNotEqual(p1,p2)

if __name__ == "__main__":
    unittest.main()
        
