'''Test Hello World application'''

import sys
sys.path.append('..')
from wsgi import application
from nose.tools import assert_equals

def test_application():
    '''Verify application returns our hello world'''
    assert_equals(['Hello world'],application('',lambda x,y: (x,y)))

