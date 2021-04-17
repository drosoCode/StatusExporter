from sources.genericStatusPage import getMetrics as _getMetrics
import requests


def getMetrics():
    metrics = _getMetrics("https://status.discord.com/api/v2/summary.json")
    data = requests.get(
        "https://discordstatus.com/metrics-display/ztt4777v23lf/day.json"
    ).json()
    metrics["discord_api_response_time_last"] = round(data["summary"]["last"])
    metrics["discord_api_response_time_mean"] = round(data["summary"]["mean"])
    return metrics