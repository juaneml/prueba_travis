#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
#import imp
import pytest
import unittest
#sys.path.append('../src/')
#from principal import *


#class TestMethods(unittest.TestCase):
    
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4
        
if __name__ == '__main__':
    unittest.main()