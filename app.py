import time
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from pprint import pprint, pp
from dotenv import load_dotenv
import os
from stalcraftapi_model import Stalcraft

# env
load_dotenv()
app_token = os.getenv("app_token")
secret_token = os.getenv("secret_token")

# vars
item_id = "4l7p"
region = "ru"

def my_func():
    pp(Stalcraft.get_item_price_history(
        item=item_id, region=region, token=app_token))

scheduler = BlockingScheduler()
scheduler.add_job(my_func, 'interval', seconds=5)
scheduler.start()
