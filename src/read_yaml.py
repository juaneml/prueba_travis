#!/usr/bin/env python3
import sys
sys.path.append('../')
import yaml
with open('../data.yaml') as f:
    lista = yaml.load(f)
    print (lista)