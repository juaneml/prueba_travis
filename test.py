#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
#import imp
import pytest
import unittest
#sys.path.append('../src/')
#from principal import *


class TestMethods(unittest.TestCase):

    # with open('../json/datos_m.json','r') as noti:
    #         lista_noticias = json.load(noti)

    # pruebaNot = Newsgroups()
    # pruebaNot.Crea_news(lista_noticias)
    prueba = 2
    def prueba(self):
        self.assertEqual(self.prueba,2,"Resultado correcto")
        
    
if __name__ == '__main__':
    unittest.main()