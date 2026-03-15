import requests
from pprint import pprint, pp
from dotenv import load_dotenv
import os

# env
load_dotenv()
app_token = os.getenv("app_token")

# vars
item_id = "zzjgn"
region = "ru"

# response
response = requests.get(headers={"Authorization": app_token},
    url=f"https://dapi.stalcraft.net/{region}/auction/{item_id}/history")

# print results
pp(response.json())
