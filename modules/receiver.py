import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")


def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

    params = {}

    if offset:
        params["offset"] = offset

    response = requests.get(url, params=params)

    return response.json()
