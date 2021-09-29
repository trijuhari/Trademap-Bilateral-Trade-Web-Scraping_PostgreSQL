import psycopg2


def create_db():

	#connect to postgresql
	con = psycopg2.connect(host= '127.0.0.1', dbname ='postgres', user ='postgres', password='juhari123')
	con.set_session(autocommit = True)
	cur = con.cursor()

	cur.execute("DROP DATABASE IF EXISTS trademap")
	cur.execute ("CREATE DATABASE trademap WITH ENCODING 'utf8' TEMPLATE template0")


	# close connection to default database
	con.close()
	# connect to sparkifydb
	con = psycopg2.connect(host= '127.0.0.1', dbname ='sparkifydb', user ='postgres', password='juhari123')
	cur = con.cursor()
	return con, cur

 

def main():
	create_db()
	 
if __name__ == '__main__':
	
	main()