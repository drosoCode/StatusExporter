from sources.genericStatusPage import getMetrics as _getMetrics


def getMetrics():
    return _getMetrics("https://status.python.org/api/v2/summary.json")
