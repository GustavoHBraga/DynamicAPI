import mariadb
import os
import sys

sys.path.append(r'./config')
from DatabaseConfig import DatabaseConfig as configDatabase

class MariadbClient:
  def __init__(self, database):
    
    self._host = configDatabase.MARIADB_HOST
    self._user = configDatabase.MARIADB_USER
    self._pass = configDatabase.MARIADB_PASSWORD
    self._port = configDatabase.MARIADB_PORT
    self._database = database

  def connectionDatabase(self):
        conn = mariadb.connect(user=self._user, password=self._pass, database=self._database, host=self._host, port=self._port)
        return conn


class Mariadb:
    _instance = None
    _database = None
    def __init__(self):
        pass
    
    @classmethod
    def get_instance(self,database):
        if self._instance is None and self._database is None or self._database != database:
            conn = MariadbClient(database).connectionDatabase()
            self._instance = conn
            self._database = database
        
        return self._instance
    


if __name__ == "__main__":
    
    # Extract the database
    connection = Mariadb().get_instance("DP_WORKSHOP")
    cursor = connection.cursor()
    cursor.execute("select pt.ProductName, pt.ProductDescription from product as pt")
    
    # Transforms the data into a dictionary (JSON representation)
    import json
    columns = [col[0] for col in cursor.description]
    results = []
    
    for row in cursor:
        results.append(dict(zip(columns, row)))

    print(json.dumps(results))