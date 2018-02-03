from nose.tools import *
import os
from mdserve import blog
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        blog.app.config['TESTING'] = True
        self.app = blog.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        assert_true('Hello World!' in rv.data.decode('utf-8'))

    def test_mdfile(self):
        rv = self.app.get('/foo.html')
        print(rv.data)
        assert_true('Welcome!' in rv.data.decode('utf-8'))

    def test_edit(self):
        self.app.post('/edit/foo.html',
                      data={'contents':'testpart',
                            'doc':'foo.md'},
                      follow_redirects=True)
        rv = self.app.get('/edit/foo.html')
        assert_true('textarea', rv.data)
        assert_true('testpart' in rv.data.decode('utf-8'))
        

if __name__ == '__main__':
    unittest.main()
