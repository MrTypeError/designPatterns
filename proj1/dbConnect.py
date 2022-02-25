from functools import wraps
import psycopg2


DB_INFO={
        "user":"postgres",
        "password":"qwerty",
        "host":"127.0.0.1",
        "port":"5432",
        "database":"Store"
        }

def connect_db(connect_data):
    def wrap(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            try:
                connection=psycopg2.connect(**connect_data)
                cursor=connection.cursor()
                dbVar=func(cursor,*args,**kwargs)
            finally:
                connection.close()
            return dbVar
        return wrapper
    return wrap

@connect_db(DB_INFO)
def func(cursor):
    cursor.execute("SELECT 1+1")
    return cursor.fetchall()

print(func())