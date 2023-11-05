from . import JsonParameter as json_tool

import sys
sys.path.append(r'./DB')
import MariaDbDatabase as Mariadb
import OracleDataBase as Oracledb
import MySqlDatabase as Mysql

def read_query_file(file):
    return open(file,'r').read()

async def getFromMariadb(query,database):
    query_str = read_query_file(query)
    connection = Mariadb.Mariadb().get_instance(database)
    cursor = connection.cursor()
    cursor.execute(query_str)
    return json_tool.convert_to_json(cursor)

async def getFromOracle(query):
    query_str = read_query_file(query)
    connection = Oracledb.OracleDabase().get_instance()
    cursor = connection.cursor()
    cursor.execute(query_str)
    return json_tool.convert_to_json(cursor)

async def getFromMysql(query, database):
    query_str = read_query_file(query)
    connection = Mysql.Mysql().get_instance(database)
    cursor = connection.cursor()
    cursor.execute(query_str)
    return json_tool.convert_to_json(cursor)