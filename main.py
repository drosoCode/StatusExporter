#!/usr/bin/python3

import yaml
from importlib import import_module
import os
import time
import datetime
import croniter
from prometheus_client import Gauge, start_http_server


def importSource(src: str):
    if not os.path.exists("sources/" + src + ".py"):
        return None
    return import_module("sources." + src)


def getData(sources):
    data = {}
    for s in sources:
        print(s[0])
        if s[1] is not None:
            data.update(s[0].getMetrics(**s[1]))
        else:
            data.update(s[0].getMetrics())
    return data


# load configuration
with open("config.yaml", "r") as f:
    config = yaml.full_load(f)

# import sources
sources = []
for src, params in config["sources"].items():
    sources.append((importSource(src), params))

data = getData(sources)
# create prometheus gauges
gauges = {}
for i in data.keys():
    gauges[i] = Gauge(i, i)

# start metrics server
start_http_server(config["system"]["port"])

# main update loop
cron = croniter.croniter(config["system"]["cron"], datetime.datetime.now())
while True:
    # update gauges
    for name, value in getData(sources).items():
        gauges[name].set(value)

    # sleep to next cron
    nxt = cron.get_next(datetime.datetime)
    print("Next update:", nxt)
    sleepTime = (nxt - datetime.datetime.now()).total_seconds()
    time.sleep(sleepTime)
