import requests
from utils import getName, getGlobalStatus
from playwright.sync_api import sync_playwright


def getMetrics() -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://www.google.com/appsstatus")
        page.wait_for_selector(".aad-body.aad-service")

        data = page.evaluate(
            """
            () => {
                return [
                    Array.from(document.querySelectorAll('.aad-body.aad-service')).map(x => x.textContent),
                    Array.from(document.querySelectorAll('.aad-body.aad-icon')).map(x => x.childNodes[0].classList[0])
                ]
            }
            """
        )
        browser.close()

    metrics = {}
    base = "google_"

    for i in range(len(data[0])):
        metrics[base + getName(data[0][i]).replace("\xa0", "_")] = getStatus(data[1][i])

    metrics[base + "global"] = getGlobalStatus(metrics)
    return metrics


def getStatus(data: str) -> int:
    if data == "aad-green-circle":
        return 0
    elif data == "aad-yellow-circle":
        return 1
    else:
        return 2
