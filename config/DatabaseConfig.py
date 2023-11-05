# config.py
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path=r"./.env")

# Definir as configurações como propriedades estáticas
class DatabaseConfig:
    MARIADB_HOST = os.getenv("MARIADB_HOST")
    MARIADB_USER = os.getenv("MARIADB_USER")
    MARIADB_PASSWORD = os.getenv("MARIADB_PASSWORD")
    MARIADB_PORT = int(os.getenv("MARIADB_PORT", "3306"))

    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_PORT = os.getenv("MYSQL_PORT","3306")

    ORACLE_USER = os.getenv("ORACLE_USER")
    ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD")
    ORACLE_HOST_AND_SERVICE = os.getenv("ORACLE_HOST_AND_SERVICE")
    ORACLE_INSTANCE = os.getenv("ORACLE_INSTANCE")