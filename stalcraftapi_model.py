import requests
from pprint import pprint, pp

class Stalcraft:
    @staticmethod
    def get_item_price_history(
            item: str, region: str, token: str) -> dict:
        url: str = f"https://eapi.stalcraft.net/{region}/auction/{item}/history"
        response = requests.get(
            url=url, headers=
            {"Authorization": f"Bearer {token}"})
        pp(response.json())
        return response.json()
