from functools import wraps
import psycopg2


DB_INFO={
        "user":"postgres",
        "password":"qwerty",
        "host":"127.0.0.1",
        "port":"5432",
        "database":"store"
        }

# connection methods
def execute_db(connect_data):
    """ decorator for postgres db connection """
    def wrap(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            try:
                connection=psycopg2.connect(**connect_data)
                cursor=connection.cursor()
                dbVar=func(cursor,*args,**kwargs)
            finally:
                connection.commit()
                connection.close()
            return dbVar
        return wrapper
    return wrap


def read_db(connect_data):
    """ decorator for postgres db connection """
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
# connection methods ends

### dont delete Tests
@read_db(DB_INFO)
def func(cursor):
    cursor.execute("SELECT 1+1")
    return cursor.fetchall()

@read_db(DB_INFO)
def func2(cursor,val):
    cursor.execute("SELECT 1+1 ")
    return cursor.fetchall()
### dont delete end 


# transaction methods
@execute_db(DB_INFO)
def insert_one(cursor, data):
    """insert into Inventory
        (
            iD,name,expdt,procdt,qty,createdDate 
        )
        values
        (01,'Laptop','2026-08-12',now(),10,now());
    """
    print(data)
    a='''insert into Inventory
        (iD,name,expdt,procdt,qty,createdDate )
        values ({id},'{name}','{expdt}','{procdt}',{qty},now());'''
    a=a.format(id = data.get("id"), name = data.get("name"), expdt= data.get("expdt"), procdt= data.get("procdt"),qty = data.get("qty"))
    cursor.execute(a)
    return True

@execute_db(DB_INFO)
def delete_all(cursor):
    cursor.execute("delete from public.Inventory where id>'0';")

@read_db(DB_INFO)
def show_all(cursor):
    cursor.execute("select * from public.Inventory;")
    return cursor.fetchall()
    
@execute_db(DB_INFO)
def update_one(cursor, data):
    """update inventory 
    SET  expdt = '2025-06-22' ,
    qty = 40
    where iD='1';"""
    b='''update inventory 
        SET  expdt = '{expdt}',
        qty = {qty}
        where iD='{id}';'''
    b=b.format(expdt= data.get("expdt"),qty=data.get("qty"),id =int(data.get("id")))
    cursor.execute(b)
    return b

@execute_db(DB_INFO)
def delete_one(cursor, data):
    """
    UPDATE inventory 
    SET   isdeleted= true 
    where iD='1';
    """
    c='''update inventory 
        SET  isdeleted = {isdeleted}
        where iD='{id}';'''
    c=c.format(isdeleted= data.get("isdeleted"),id = data.get("id"))
    cursor.execute(c)
    return c

@execute_db(DB_INFO)
def insert_many(cursor,data_set):
    """take a list of dict and iterate the list and call inset_one everytime
    if you dont complete this i will harras you till you complete htis
    """
    for i in range(len(data_set)):
        insert_one(data_set[i])

@execute_db(DB_INFO)
def softDeleteAll_db(cursor, data):
    """
    UPDATE inventory 
    SET   isdeleted= true 
    where iD>='1';
    """
    c='''
        UPDATE inventory 
        SET   isdeleted={isdeleted} 
        where iD>='1';'''
    c=c.format(isdeleted=data.get("isdeleted"))
    cursor.execute(c)
    return c
#transaction methods ends

data={
    "isdeleted":"true"
}
# val_temp=softDeleteAll_db(data)

# calls
data={
    "id":2,
    "name":"SD",
    "expdt":"2025-10-22",
    "procdt":"2021-05-20",
    "qty":"10",
    "createdDate":"2021-10-20",
}
# val=insert_one(data)

data={
    "id":2,
    "expdt":"2025-12-22",
    "qty":"11",
}
# temp=update_one(data)

data={
    'isdeleted':'true',
    'id':2,
}
# val2=delete_one(data)

data_set=[{
                "id":1,
                "name":"Apple",
                "expdt":"2025-10-22",
                "procdt":"2021-05-20",
                "qty":"10",
                "createdDate":"2021-10-20",
            },
            {
                "id":2,
                "name":"Nokia",
                "expdt":"2025-11-22",
                "procdt":"2021-09-20",
                "qty":"200",
                "createdDate":"2021-10-20",
            },
            {
                "id":3,
                "name":"Samsung",
                "expdt":"2025-12-22",
                "procdt":"2021-06-20",
                "qty":"100",
                "createdDate":"2021-10-20",
            },
            ]
# insert_many(data_set)