import requests
from pprint import pprint, pp

class Stalcraft:
    @staticmethod
    def get_item_price_history_demoapi(
            item: str, region: str, token: str) -> dict:
        url: str = f"https://dapi.stalcraft.net/{region}/auction/{item}/history"
        response = requests.get(
            url=url, headers=
            {"Authorization": f"Bearer {token}"})
        pp(response.json())
        return response.json()

    @staticmethod
    def get_active_item_lots_demoapi(item: str, region: str, token: str):
        url: str = f"https://dapi.stalcraft.net/{region}/auction/{item}/lots"
        response = requests.get(
            url=url, headers=
            {"Authorization": f"Bearer {token}"})
        pp(response.json())
        return response.json()
