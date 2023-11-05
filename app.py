from fastapi import FastAPI
import Utils.ExecuteQuery as ExecuteQuery
import Utils.JsonParameter as Config

app = FastAPI()

def create_route(route,instance,query_file,database):
    
    @app.get(route)
    async def get_data():
        if instance.upper() == "ORACLE":
            return await ExecuteQuery.getFromOracle(query_file)

        if instance.upper() == "MARIADB":
            return await ExecuteQuery.getFromMariadb(query_file,database)

        if instance.upper() == "MYSQL":
            return await ExecuteQuery.getFromMysql(query_file,database)
        
for api_config in Config.get_api_configurations('./routes/config-routes.json'):
    description = api_config["Description"]
    route = api_config["Route"] 
    query_file = api_config["QueryFile"]
    instance = api_config["Instance"]
    database = api_config["Database"]

    create_route(route, instance, query_file, database)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8082, reload=True, workers=4)