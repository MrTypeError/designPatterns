from backend import query_exec


class Store():
    def __init__(self):
        # self.cursor = connect_db()
        pass
    
    def checkData(self, query):
        query_exec(query)

q = Store()
print(q.checkData("select * from Inventory;"))