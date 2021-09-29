import psycopg2
from lib_scraping import *

def connect_db() :
    from sqlalchemy import create_engine

    postgres_address = 'localhost'
    postgress_port = '5432'
    postgres_username = 'postgres'
    postgres_password = 'juhari123'
    postgres_database = 'data_trademap'
    postgres = ('postgresql://{username}:{password}@{address}:{port}/{dbname}'.format(username=postgres_username, \
                                                                                      password=postgres_password,
                                                                                      address=postgres_address,
                                                                                      port=postgress_port,
                                                                                      dbname=postgres_database))

    # untuk mengkoneksikan ke database yang digunakan
    con = create_engine(postgres)
    return con 

def get_code_country(connect_db ):
    con = connect_db()
    df = pd.read_sql_query('select * from code_negara', con )

    kode_negara = {}
    for i in range( len(df)) :
        kode_negara[df.code[i]] = df.nama[i]
      
    kombinasi_negara = df.code[df.code!='360']

    return con, kode_negara, kombinasi_negara


def get_key(val, kode_negara):
    for key, value in kode_negara.items():
         if val == value:
             return key
 
    return "key doesn't exist"
 
# Driver Code
 
 

 