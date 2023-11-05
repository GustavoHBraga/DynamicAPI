import json
from decimal import Decimal
import datetime

def get_api_configurations(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            return data.get("Configurations", {}).get("Api_configurations", [])
    
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def custom_serializer(obj):

    if isinstance(obj, Decimal):
        return float(obj) # Converta Decimal para float
    
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()  # Converta datetime para uma string ISO 8601

    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def convert_to_json(cursor):
    columns = [col[0] for col in cursor.description]
    results = [dict(zip(columns, row)) for row in cursor]
    return json.loads(json.dumps(results, default=custom_serializer))
  
if __name__ == "__main__":
  get_api_configurations('./Config/config-routes.json')
