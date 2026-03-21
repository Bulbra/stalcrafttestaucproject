import time
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from pprint import pprint, pp
from dotenv import load_dotenv
import os
from stalcraftapi_model import Stalcraft

# env
load_dotenv()
app_token = os.getenv("token")
secret_token = os.getenv("secret_token")

# vars
item_id = "4l7p"
region = "ru"

def get_history():
    history = Stalcraft.get_item_price_history(
        item=item_id, region=region, is_demo=True, token=app_token)
    pp(history)


scheduler = BlockingScheduler()
scheduler.add_job(get_history, 'interval', seconds=5)
scheduler.start()
