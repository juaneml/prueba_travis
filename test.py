#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
#import imp
import pytest
import unittest
#sys.path.append('../src/')
#from principal import *


class TestMethods(unittest.TestCase):
    
    prueba = 2
    def prueba(self):
        self.assertEqual(self.prueba,2,"Resultado correcto")
        
if __name__ == '__main__':
    unittest.main()