import cx_Oracle

import sys
sys.path.append(r'./config')
from DatabaseConfig import DatabaseConfig as configDatabase

class OracleClient:
    def __init__(self):
        
        dotenv.load_dotenv(dotenv_path=r".\.env")
        cx_Oracle.init_oracle_client(configDatabase.ORACLE_INSTANCE)

        self._login = configDatabase.ORACLE_USER
        self._pass = configDatabase.ORACLE_PASSWORD
        self._service = configDatabase.ORACLE_HOST_AND_SERVICE
        
    def connectionDatabase(self):
        conn = cx_Oracle.connect(self._login,self._pass,self._service)
        return conn

class OracleDabase:
    _instance = None
    
    def __init__(self):
        pass
    
    @classmethod
    def get_instance(self):
        if self._instance is None:
            conn = OracleClient().connectionDatabase()
            self._instance = conn
        
        return self._instance
