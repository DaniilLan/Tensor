import os

import requests


def get_region():
    try:
        response = requests.get('https://api.sypexgeo.net/json/')
        data = response.json()
        region = data['region']['name_ru']
        return region.replace("область", "обл.")
    except Exception as e:
        return f"Ошибка: {e}"

print(os.path.join(os.path.dirname(__file__), "test_downloads"))