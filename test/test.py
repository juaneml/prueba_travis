#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test.py


import sys
import pytest
import unittest

sys.path.append('../src/')
from principal import *
from usuario import *
from conexion import Conexion

class TestMethods(unittest.TestCase):
    pruebaUsuario = Usuario()
    pruebaServicio = Servicio()
    conex = Conexion()

    def test_nombre(self):
        self.assertEqual(self.pruebaUsuario.get_nombre(self),False,"El campo nombre está vacío") 
    
    def test_progreso(self):
        self.assertEqual(self.pruebaUsuario.get_progreso(self),0,"No tiene progreso")
        #self.assertEqual(self.pruebaUsuario.get_progreso(self),5,"No tiene progreso dato mal")

    def test_day(self):
        self.assertEqual(self.pruebaServicio.get_day(),0,"ehi")
    
     
    def test_conexion(self):
        self.assertEqual(self.conex.conexion(self),True,"Nice")

if __name__ == '__main__':
    unittest.main()