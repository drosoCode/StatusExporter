from sources.genericStatusPage import getMetrics as _getMetrics


def getMetrics():
    return _getMetrics("https://reddit.statuspage.io/api/v2/summary.json")
