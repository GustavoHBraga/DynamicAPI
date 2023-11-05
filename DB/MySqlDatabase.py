import mysql.connector
import sys

sys.path.append(r'./config')
from DatabaseConfig import DatabaseConfig as configDatabase

class MysqlClient:
  def __init__(self, database):
    
    self._host = configDatabase.MYSQL_HOST
    self._user = configDatabase.MYSQL_USER
    self._pass = configDatabase.MYSQL_PASSWORD
    self._database = database

  def connectionDatabase(self):
        conn = mysql.connector.connect(user=self._user, password=self._pass, database=self._database, host=self._host)
        return conn

class Mysql:
    _instance = None
    _database = None
    def __init__(self):
        pass
    
    @classmethod
    def get_instance(self, database):
        if self._instance is None and self._database is None or self._database != database:
            conn = MysqlClient(database).connectionDatabase()
            self._instance = conn
            self._database = database
        return self._instance

if __name__ == "__main__":

    # Extract the database
    connection = Mysql().get_instance("money_api")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM money_api.category;")
    
    # Transforms the data into a dictionary (JSON representation)
    import json
    columns = [col[0] for col in cursor.description]
    results = []
    
    for row in cursor:
        results.append(dict(zip(columns, row)))

    print(json.loads(json.dumps(results)))
    