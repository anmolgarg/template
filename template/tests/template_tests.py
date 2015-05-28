'''
nose test suite for template module

To run some specific tests below use;
nosetests -w tests tests/template_tests.py:test_basic

'''

from nose.tools import *
from template import template


def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "Test basic"
    assert 1 == 1