import requests
from utils import getName


def getMetrics() -> dict:
    data = requests.get(
        "https://crowbar.steamstat.us/gravity.json",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
        },
    ).json()
    metrics = {}
    base = "steam_"

    for s in data["services"]:
        metrics[base + getName(s[0])] = s[1]
    metrics[base + "global"] = round(data["online"])
    return metrics
