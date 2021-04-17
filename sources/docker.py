from bs4 import BeautifulSoup
import requests
from utils import getName, getGlobalStatus


def getMetrics() -> dict:
    soup = BeautifulSoup(
        requests.get(
            "https://status.docker.com/",
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
            },
        ).text,
        features="html.parser",
    )

    metrics = {}
    base = ""

    resp = soup.find("div", {"id": "statusio_components"})
    for i in resp.findAll("div", recursive=False):
        d = i.findAll("p")
        metrics[base + getName(d[0].text)] = getStatus(d[1].text)

    metrics[base + "global"] = getGlobalStatus(metrics)
    return metrics


def getStatus(data: str) -> int:
    if data == "Operational":
        return 0
    else:
        return 2
