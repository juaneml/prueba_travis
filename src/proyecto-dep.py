#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hug
import json



from principal import Servicio
from principal import Usuario
import sys
import os
import logging
import hug
from hug.middleware import LogMiddleware
from pythonjsonlogger import jsonlogger
from datatime import datetime
import requests
sys.path.append('../src/')

"""Define logger en JSON"""
# @hug.middleware_class()
# class CustomLogger(LogMiddleware):
        
#     def __init__(self):
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         logHadler = logging.StreamHandler()
#         formatter = jsonlogger.JsonFormatter()
#         logHandler.setFormatter(formatter)
#         logger.addHandler(logHadler)
#         super().__init__(logger=logger)
    
#     def _generate_combined_log(self, request, response):
#         """Given a request/response pair, generate a logging format similar to the NGINX combined style."""
#         current_time = datetime.utcnow()
#         return {'remote_addr':request.remote_addr,
#                 'time': current_time,
#                 'method': request.method,
#                 'uri': request.relative_uri,
#                 'status': response.status,
#                 'user-agent': request.user_agent }


with open('../json/datos.json','r') as usuarios:
        lista_usuarios = json.load(usuarios)
        
        usuario = Usuario()
        usuario.crea_usu(lista_usuarios)

        for i in range(usuario.get_numUsuarios()):
        lista_usuarios.append(usuario.to_s(i))

    with open('../json/datos_tabaco.json','r') as marcas:
        lista_tabaco = json.load(marcas)

        serv = Servicio() 
        serv.crea_sistema(usuario,usuario.get_numUsuarios(),lista_tabaco)

        for i in range(serv.get_numUsuarios()):
        lista_tabaco.append(serv.to_Simple(i,usuario))    
    

@hug.cli()
# @hug.get('/')
# def getEstado():
#     salida = {"status": "OK"}
#     return salida

@hug.get('/status')
def status():
    status = {"status": "OK"
    }
    return status

# rutas para comprobación

@hug.get('/lista_usuarios')
def lista_usus():
    
    salida = lista_usuarios
    return str(salida)

@hug.get('/datos_calculados')
def lista_tab():
    salida = lista_tabaco
    
    return salida

@hug.get('/moneda')
def moneda():
    #print(serv.to_Simple(1))
    salida = serv.get_moneda()
    return str({"Euro",salida})

@hug.post()
def method_post():
    salida={'Sistema': 'versión 0.5'}
    return str(salida)

@hug.get('/version')
def post():
    return method_post()

if 'PORT' in os.environ :
    port = int(os.environ['PORT'])
else:
    port = 8000

api = hug.API(__name__)

if __name__ == '__main__':
    api.http.serve(port ) #
# if __name__ == '__main__':

#     una.interface.cli()
#     all.interface.cli()