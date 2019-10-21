import psycopg2
#import pprint
import sys

class Conexion:
	def conexion(self):
		try:
            connection = psycopg2.connect(user = "postgres",password ="bar",host = "localhost", database = "travis_ci_test")
			#connection = psycopg2.connect(user = "postgres",password = "j9u4a1n",host = "127.0.0.1",database = "sistema")
            
			cursor = connection.cursor()
			# Print PostgreSQL Connection properties
			#print ( connection.get_dsn_parameters(),"\n")

			# Print PostgreSQL version
			cursor.execute("select * from usuarios;")
			#record = cursor.fetchone()
			record = cursor.fetchall()
			#pprint.pprint(record)
			#print("You are connected to - ", record,"\n")
			return True
		except (Exception, psycopg2.Error) as error :
			print ("Error while connecting to PostgreSQL", error)
			#finally:
			#closing database connection.
			if(connection):
				cursor.close()
				connection.close()
		
			print("PostgreSQL connection is closed")
			return False

	if __name__ == "__main__":
		conexion(0)



