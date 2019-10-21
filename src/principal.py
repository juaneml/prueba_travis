#!/usr/bin/env python
# -*- coding: utf-8 -*-
# principal.py


from usuario import Usuario
import json
import os
import sys

""" Clase principal para el servicio en esta clase se va a definir
    Los atributos:
    - day: para los contar los días
    - din_aho: dinero ahorrado
    - tipo_tab: tipo de tabaco
    - marca: marca del tabaco
    - num_cigar: número de cigarrillos diarios
    - logs: los logs para cada usuario

    Obtendremos los datos que tenemos almacenados del usuario de nuestra base de datos
    que ya han sido facilitados por el usuario
 """
 
class Servicio:
    day = 0
    din_aho = 0
    tipo_tab = []
    marca  = []
    num_cigar = []
    precio = 0
    lista_tabaco = []
    num_usuarios = 0
    logs = []
    progres = []
    moneda = " "

    def __init__(self):
        self.tipo_tab = []
        self.day = []
        self.din_aho = []
        self.marca = []
        self.num_cigar = []
        self.lista_tabaco = []
        self.precio = []
        self.num_usuarios = 0
        self.progres = []
        self.moneda = " "

    
    """ Devuelve el número de días que el usuario lleva sin fumar"""
    def get_day(self):
        return self.day

    """ Devuelve el dinero ahorrado en euros """
    def get_dinAho(self,string):
        return self.din_aho[string]


    """ Devuelve la marca """
    def get_marca(self,string):
        return self.marca[string]

    """ Devuelve el numero de cigarrillos """
    def get_Ncigar(self,string):
        return self.num_cigar[string]

    """ Devuelve los logs de los usuarios """
    def get_logs(self):
        return self.logs
    
    """ Devuelve el número de usuarios """
    def get_numUsuarios(self):
        return self.num_usuarios

    """ Devuelve la moneda """

    def get_moneda(self):
        return self.moneda

    """ Cambia la moneda """
    def set_moneda(self,string):
        self.moneda = string

    """ Add nombre marca """
    def add_marca(self,string):
       
        if(type(string) != int):
            self.marca.append(string)
            return True
        else:
            return False

    
    """ Add tipo de tabaco """

    def add_tipo(self,string):

        if(type(string) != int):

            self.tipo_tab.append(string)
            return True
        
        else:
            return False
    
    """ Devuelve el tipo de tabaco"""
    def get_tipo(self,int):
        return self.tipo_tab[int]


    """ Add número de cigarros """

    def add_numCigar(self,int):

        if(type(int) != str):
            self.num_cigar.append(int)
            return True

        else:
            return False

    """ add Dinero ahorrado
        num: numero de cigarros
        marca: marca del tabaco
        tipo: tipo de tabaco, liar o industrial
        dias: dias que el usuario lleva sin fumar
    """ 
    def add_dinAho(self,num,marca,tipo,dias):
        num_cigar = num 
        marca = marca 
        tipo = tipo     
        precio_uno = 0   
        dinAho_dia = 0  
        dinAho = 0.0    

        if (marca == "MarcaA" and tipo == "Industrial"):
            precio_uno = 4.50 / 20.0
            dinAho_dia = precio_uno * num_cigar
            dinAho = dinAho_dia * dias
           

        if (marca == "MarcaB" and tipo == "Industrial"):
            precio_uno = 4.80 / 20.0
            dinAho_dia = precio_uno * num_cigar
            dinAho = dinAho_dia * dias
            
        if (marca == "MarcaC" and tipo == "Industrial"):
            precio_uno = 5.0 / 20.0
            dinAho_dia = precio_uno * num_cigar
            dinAho = dinAho_dia * dias 
           
        
        if (marca == "MarcaD" and tipo == "Liar"):
            precio_uno = 3.5 / 30.0
            dinAho_dia = precio_uno * num_cigar
            dinAho = dinAho_dia * dias 
        
        if (marca == "MarcaE" and tipo == "Liar"):
            precio_uno = 3.75 / 30.0
            dinAho_dia = precio_uno * num_cigar
            dinAho = dinAho_dia * dias 
        
        self.din_aho.append(dinAho)
       
    """ Devuelve el progreso """

    def get_progreso(self,string):
        return self.progres[string]

    """ Add progress """
    def add_progreso(self, string):
        self.progres.append(string)

    """ Cambia el número de usuarios """
    def set_numUsuarios(self,int):
        self.num_usuarios = int
    
    """ Cambia el nombre """
    def set_marca(self,string):
        self.marca = string
    
    """ Cambia el tipo """
    def set_tipo(self,string):
        self.tipo_tab = string

    """ Cambia la capacidad """
    def set_capa(self,int):
        self.num_cigar = int

    """ Cambia el precio """
    def set_precio(self,int):
        self.precio = int

    """ Cambia el numero de cigarros """
    def set_cigar(self,int):
        self.num_cigar = int


    """ Imprime la lista de los usuarios:
        - Nombre usuario
        - Marca de tabaco
        - Tipo
        - Num. cigarros
        - Progreso y dinero ahorrado 
    """

    def to_s(self,i,lista):
        var = {"Nombre":lista.get_nombre(i),"marca": self.get_marca(i),"Tipo": self.get_tipo(i),"Num. cigarillos": lista.get_cigar(i),
        "Progreso": self.get_progreso(i),"Dinero Ahorrado": str(self.get_dinAho(i))+self.get_moneda() }
        return var

    """ Imprime Nombre,progreso y dinero ahorrado """
    def to_Simple(self,i,lista):
        var = {"Nombre" : lista.get_nombre(i),"Progreso": self.get_progreso(i),
        "Dinero Ahorrado": str(self.get_dinAho(i))+self.get_moneda()}
        return var

    """ crea sistema """
    def crea_sistema(self,usuario,num_usu,lista):
        dic = lista
        
        usuarios = self.set_numUsuarios(num_usu)

        for i in dic:
            if(i['name'] != None):
                self.lista_tabaco.append(self.add_marca(i['name']))
            else:
                self.lista_tabaco.append(self.add_marca(" "))

            if(i['tipo'] != None):
                self.lista_tabaco.append(self.add_tipo(i['tipo']))
            else:
                self.lista_tabaco.append(self.add_tipo(" "))

            if(i['capacidad'] != None):
                self.lista_tabaco.append(self.add_numCigar(i['capacidad']))
            else:
                self.lista_tabaco.append(self.add_numCigar(" "))

            if(i['precio'] != None):
                self.lista_tabaco.append(self.add_marca(i['precio']))

            if(i['moneda'] != None):
                self.set_moneda(i['moneda'])
            
            
        for i in range(num_usu):
            if(usuario.get_cigar(i) != 0):
                self.lista_tabaco.append(self.add_dinAho(usuario.get_cigar(i),usuario.get_marca(i),usuario.get_tipo(i) ,usuario.get_diaSin(i)))
                self.lista_tabaco.append(self.add_progreso(usuario.get_progreso(i)))

if __name__ == "__main__":
    with open('../json/datos.json','r') as usuarios:
        lista_tabaco = json.load(usuarios)
    
    usuario = Usuario()
    usuario.crea_usu(lista_tabaco)

    #for i in usuario:
    # for i in range(usuario.num_usuarios):
    #     print(usuario.to_s(i))

    with open('../json/datos_tabaco.json','r') as marcas:
       lista_tabaco = json.load(marcas)

    serv = Servicio() 
    serv.crea_sistema(usuario,usuario.num_usuarios,lista_tabaco)

    # for i in range(serv.get_numUsuarios()):
    #     print (serv.to_s(i,usuario))
    
    for i in range(serv.get_numUsuarios()):
        print (serv.to_Simple(i,usuario))