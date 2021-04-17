from sources.genericStatusPage import getMetrics as _getMetrics


def getMetrics():
    return _getMetrics("https://www.cloudflarestatus.com/api/v2/summary.json")
