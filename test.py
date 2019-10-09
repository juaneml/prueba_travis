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
        

def conexion():
    try:
        connection = psycopg2.connect(user = "postgres",password = " ",host = "127.0.0.1",port = "5432",database = "travis_ci_test")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        #cursor.execute("select * from tblTest;")
        record = cursor.fetchone()
        #record = cursor.fetchall()
        #pprint.pprint(record)
        print("You are connected to - ", record,"\n")

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return record
if __name__ == '__main__':
    unittest.main()