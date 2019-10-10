import unittest
import hug
import psycopg2
import pprint
import sys
import pytest

from pytest import ExitCode


def conexion():
    try:
    #postgresql_db.
        connection = psycopg2.connect(user = "postgres",password = "j9u4a1n",host = "127.0.0.1",port = "5432",database = "test")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        #print ( connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        cursor.execute("select * from tblTest;")
        #record = cursor.fetchone()
        record = cursor.fetchall()
        pprint.pprint(record)
        #print("You are connected to - ", record,"\n")

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
        assert conexion() == 200

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            #assert record == [(1, 10, 'Juan Esteban'), (2, 2, 'Tronco')]
            print("PostgreSQL connection is closed")
            #assert conexion() == "[(1, 10, 'Juan Esteban'), (2, 2, 'Tronco')]"

    return record

def error():
    assert conexion() == ""