def getName(name: str, removeDetails=True) -> str:
    name = (
        name.lower()
        .strip()
        .replace(" ", "_")
        .replace("-", "_")
        .replace(",", "_")
        .replace(":", "_")
        .replace(".", "_")
        .replace("'", "_")
        .replace('"', "")
        .replace("&", "")
        .replace("/", "_")
    )

    if removeDetails:
        pos = name.find("(")
        while pos != -1:
            name = name[0:pos] + name[name.find(")", pos) + 1 :]
            pos = name.find("(")

        pos = name.find("[")
        while pos != -1:
            name = name[0:pos] + name[name.find("]", pos) + 1 :]
            pos = name.find("[")
    else:
        name = (
            name.replace("(", "_").replace(")", "_").replace("[", "_").replace("]", "_")
        )

    while name.find("__") != -1:
        name = name.replace("__", "_")

    last = len(name) - 1
    if name[last:] == "_":
        name = name[0:last]

    if name[0:1] == "_":
        name = name[1:]

    return name.strip().encode("ascii", "ignore").decode()


def getGlobalStatus(data: dict) -> int:
    nbOk = 0
    for k in data:
        nbOk += int(data[k] == 0)
    return round(nbOk / len(data) * 100)
