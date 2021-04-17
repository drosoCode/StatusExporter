import requests
from utils import getName, getGlobalStatus


def getMetrics() -> dict:
    data = requests.get(
        "https://twitchstatus.com/api/status",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
        },
    ).json()
    base = "twitch_"

    metrics = {
        base + "website_status": getStatus(data["web"]["servers"][0]["status"]),
        base + "website_latency": getStatus(data["web"]["servers"][0]["loadTime"]),
        base + "api_status": getStatus(data["web"]["servers"][1]["status"]),
        base + "api_latency": getStatus(data["web"]["servers"][1]["loadTime"]),
        base + "tmi_status": getStatus(data["web"]["servers"][2]["status"]),
        base + "tmi_latency": getStatus(data["web"]["servers"][2]["loadTime"]),
    }

    for s in data["ingest"]["servers"]:
        metrics[base + "ingest_" + getName(s["description"]) + "_status"] = getStatus(
            s["status"]
        )
        metrics[base + "ingest_" + getName(s["description"]) + "_latency"] = getStatus(
            s["loadTime"]
        )

    for s in data["chat"]["servers"]:
        metrics[
            base
            + "chat_"
            + s["cluster"]
            + "_"
            + s["protocol"]
            + "_"
            + getName(s["server"])
            + "_status"
        ] = getStatus(s["status"])
        metrics[
            base
            + "chat_"
            + s["cluster"]
            + "_"
            + s["protocol"]
            + "_"
            + getName(s["server"])
            + "_latency"
        ] = s["lag"]

    metrics[base + "global"] = getGlobalStatus(metrics)
    return metrics


def getStatus(txt: str) -> int:
    if txt == "online":
        return 0
    else:
        return 2
