import requests
from utils import getName, getGlobalStatus


def getMetrics() -> dict:
    data = requests.get(
        "https://admin.microsoft.com/api/servicestatus/index",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
        },
    ).json()

    metrics = {}
    base = "office_"

    for s in data["Services"]:
        metrics[base + getName(s["Id"])] = getStatus(s["IsUp"])
    metrics[base + "global"] = getGlobalStatus(metrics)
    return metrics


def getStatus(up: bool) -> int:
    return 0 if up else 2
