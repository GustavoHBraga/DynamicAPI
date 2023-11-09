#  💻📍 DynamicAPI
Este projeto é uma API desenvolvida para ser altamente dinâmica e modular, capaz de se adaptar a diferentes configurações e bancos de dados sem a necessidade de alterar o código-fonte.
<br>
<br>

# 📃 Características:

<ul> <b>Dinamismo</b>: Configurações totalmente controláveis via arquivos JSON.</ul>
<ul> <b>Modularidade</b>: Fácil integração com diferentes bancos de dados como MariaDB, MySQL e Oracle.</ul>
<ul> <b>Escalabilidade</b>: Desenvolvida para suportar crescimento e demandas crescentes com facilidade.</ul>

<br>

# 📃 Arquitetura
<ul> A arquitetura do projeto foi construída seguindo alguns padrões de design para garantir sua modularidade e extensibilidade.</ul>

<br>

### 🎨 Padrões de Design:

<br>
<ul><b>Singleton</b>: Utilizado na gestão de conexões com a base de dados para garantir uma única instância da conexão por base de dados.</ul>
<ul><b>Command</b>: O projeto usa uma forma do padrão Command para encapsular uma solicitação como um objeto, permitindo assim a parametrização dos clientes com diferentes solicitações.</ul>
<ul><b>Adapter</b>: Este padrão é aplicado na forma de adaptadores específicos para cada tipo de banco de dados, permitindo que eles possam ser utilizados de maneira intercambiável.</ul>
<ul><b>Strategy</b>: Permite que o algoritmo de serialização JSON seja escolhido em tempo de execução, dependendo do tipo de dados que está sendo processado.</ul>

<br>
<br>

# 📋 Configuração e Execução:

### Pré-requisitos:
Antes de iniciar, certifique-se de ter instalado:
- Python 3.8 ou superior
- Gerenciador de pacotes pip
- Banco(s) de dados de sua escolha

<br>

```bash
# Clonar o repositório
git clone https://github.com/GustavoHBraga/DynamicAPI.git

# Entrar no diretório do projeto
cd DynamicAPI

# Instalar as dependências
pip install -r requirements.txt
```

- Criar arquivo .env:

```bash
############# MYSQL CONNECTIONS ##########
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"

############# MARIADB CONNECTIONS ##########
MARIADB_HOST = "localhost"
MARIADB_PORT = 3305
MARIADB_USER = "root"
MARIADB_PASSWORD = "root"

############ ORACLE CONNECTIONS ############
ORACLE_INSTANCE = ".\Databases\instantclient_19_20"
ORACLE_HOST_AND_SERVICE = "localhost/localhost"
ORACLE_USER = "root"
ORACLE_PASSWORD = "root"
```

- Exemplo de configuração do arquivo json (config-routes.json):

```json
{
    "Configurations":{

        "Api_configurations": [
            {
                "Instance": "Mysql",
                "Database": "money_api",
                "Description": "List all categories in the product",
                "QueryFile": "./query_files/Mysql/category.sql",
                "Route": "/v1/categories"
            },
            {
                "Instance": "Mysql",
                "Database": "bdvendas",
                "Description": "List all categories in the product",
                "QueryFile": "./query_files/Mysql/fornecedores.sql",
                "Route": "/v1/fornecedores"
            },
            {
                "Instance": "Mariadb",
                "Database": "DP_WORKSHOP",
                "Description": "List all categories in the product",
                "QueryFile": "./query_files/MariaDB/product.sql",
                "Route": "/v1/product"
            },
            {
                "Instance": "Mariadb",
                "Database": "DP_WORKSHOP",
                "Description": "List all categories in the product",
                "QueryFile": "./query_files/MariaDB/product-v2.sql",
                "Route": "/v2/product"
            }
        ]

    }
}
```

- Exemplo de arquivo sql para realizar as consultas:

```sql
select pt.ProductName, pt.Price, pt.ProductDescription from product as pt
```

- Estrutura para armazenar os arquivos de consultas (Query):

![image](https://github.com/GustavoHBraga/DynamicAPI/assets/70377322/e743451c-c988-48d4-bfd0-a1c08e4eba65)


## USO
- Para iniciar a API, execute o seguinte comando:
<br>

```bash
python -m uvicorn app:app --reload

ou

python app.py
```
<br>

- Navegue até http://localhost:8082/docs para ver a documentação interativa da API (gerada pelo Swagger UI). Segue abaixo um exemplo:
<br>

![image](https://github.com/GustavoHBraga/DynamicAPI/assets/70377322/254e8839-d0ca-40f1-8942-1cf5604e7081)


