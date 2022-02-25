import psycopg2
from psycopg2 import Error

# try:
    
#     connection = psycopg2.connect(user="postgres",
#                                   password="qwerty",
#                                   host="127.0.0.1",
#                                   port="5432",
#                                   database="Store")

    
#     cursor = connection.cursor()
#     cursor.execute("select * from public.Inventory;")
#     # record = cursor.fetchone()
#     record = cursor.fetchall()
#     print("Data in - ", record, "\n")

# except (Exception, Error) as error:
#     print("Error while connecting to PostgreSQL", error)


def query_exec(query):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="qwerty",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="Store")
        cur = connection.cursor()
        cur.execute(query)
        return cur.fetchall()
    except (Exception, Error) as error:
        print("Connection made, querry failed", error)
    finally:
        if (connection):
            cur.close()
            connection.close()
            print("PostgreSQL connection is closed")

