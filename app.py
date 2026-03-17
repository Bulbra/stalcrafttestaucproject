import requests
from pprint import pprint, pp
from dotenv import load_dotenv
import os

# env
load_dotenv()
app_token = os.getenv("app_token")
secret_token = os.getenv("secret_token")

# vars
item_id = "4l7p"
region = "ru"

# response
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {app_token}",
}
response = requests.get(headers=headers,
    url=f"https://eapi.stalcraft.net/{region}/auction/{item_id}/history")
# print results
pp(response.json())
