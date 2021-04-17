import requests
from utils import getName, getGlobalStatus


def getMetrics(url: str) -> dict:
    data = requests.get(url).json()
    metrics = {}
    base = getName(data["page"]["name"]) + "_"

    for c in data["components"]:
        metrics[base + getName(c["name"])] = getStatus(c["status"])
    metrics[base + "global"] = getGlobalStatus(metrics)
    return metrics


def getStatus(txt: str) -> int:
    if txt == "partial_outage":
        return 1
    elif txt == "operational":
        return 0
    else:
        return 2
