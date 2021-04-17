import requests
from utils import getName, getGlobalStatus


def getMetrics() -> dict:
    data = requests.get(
        "https://status.playstation.com/data/statuses/region/SCEE.json",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
        },
    ).json()
    metrics = {}
    base = "psn_"

    for c in data["countries"]:
        metrics[base + getName(c["countryCode"])] = getStatus(c["status"])
        for s in c["services"]:
            metrics[
                base + getName(c["countryCode"]) + "_" + getName(s["serviceName"])
            ] = getStatus(s["status"])

    metrics[base + "global"] = getGlobalStatus(metrics)
    return metrics


def getStatus(status: list) -> int:
    if len(status) == 0:
        return 0
    else:
        return 2
