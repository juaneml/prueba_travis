#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test.py


import sys
import pytest
import unittest
import json
import yaml
sys.path.append('../')
sys.path.append('../src/')
from principal import *
from usuario import *
#from conexion import *
class TestMethods(unittest.TestCase):
    #conex = Conexion()
    with open('../json/datos.json','r') as usuarios:
        lista_usuario = json.load(usuarios)
    
    pruebaUsuario = Usuario()
    pruebaUsuario.crea_usu(lista_usuario)
    
    #print(lista_usuario)

    #for i in usuario:
    # for i in range(usuario.num_usuarios):
    #     print(usuario.to_s(i))

    with open('../json/datos_tabaco.json','r') as marcas:
        lista_tabaco = json.load(marcas)

   
    pruebaServicio = Servicio()
    pruebaServicio.crea_sistema(pruebaUsuario,pruebaUsuario.get_numUsuarios(),lista_tabaco)

    
    with open('../data.yaml') as f:
        lista = yaml.load(f,Loader=yaml.FullLoader)
    print (lista)


    """ test nombre usuario """

    def test_nombre(self):
       self.assertEqual(self.pruebaUsuario.get_nombre(self),False,"El campo nombre está vacío")
       self.assertEqual(self.pruebaUsuario.get_nombre(0),"Usuario 1", "Tiene nombre")
    
    """ test dias que lleva sin fumar """

    # def test_diaSin(self):
    #     self.assertEqual(self.pruebaUsuario.get_diaSin(self),0,"No tiene progreso")
    #     self.assertEqual(self.pruebaUsuario.get_diaSin(0),8750,"Es progreso obtenido es correcto")

    """ test marca tabaco """

    def test_marca(self):
        self.assertEqual(self.pruebaServicio.get_marca(self),False,"No marca")
        self.assertEqual(self.pruebaServicio.get_marca(0),'MarcaA', "La marca es correcta")
       
    """ test cambiar moneda """

    def test_moneda(self):
        
        self.assertEqual(self.pruebaServicio.set_moneda(0),False, "Dato incorrecto")
        self.assertEqual(self.pruebaServicio.set_moneda("Libra"),True, "Dato correcto")

    def test_to_s(self):
        self.assertEqual(self.pruebaServicio.to_s(0,self.pruebaUsuario)['Nombre'],'Usuario 1', "Usuario correcto")
    
    #def test_dinAho(self):
    #    self.assertEqual(self.pruebaServicio.get_dinAho(0),43357.05, "Dinero ahorrado correcto")

    # def test_conex(self):
    #     self.assertEqual(self.conex.conexion(),True,"Conexión con éxito" ) 
    #     print("Conexión con éxito",self.conex.conexion())
if __name__ == '__main__':
    unittest.main()
    

    
