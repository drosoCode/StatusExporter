from sources.genericStatusPage import getMetrics as _getMetrics


def getMetrics():
    return _getMetrics("https://www.githubstatus.com/api/v2/summary.json")
