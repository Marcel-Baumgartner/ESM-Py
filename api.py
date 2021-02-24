#! /bin/python3

def listusers():

    import requests

    # api-endpoint
    URL = "https://api.masusniper.de/listusers.php"

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    result = r.text
    lines = result.split("<br>")

    servers = []

    for s in lines:
        if s != "":
            servers.append(s)

    return servers

def adduser(discord, minecraft, server, description):
    import requests

    request = "https://api.masusniper.de/adduser.php?discord=" + discord + "&minecraft=" + minecraft + "&server=" + server + "&description=" + description

    r = requests.get(url=request)

    return r.text

def deleteuser(id):

    import requests

    request = "https://api.masusniper.de/deleteuser.php?id=" + id

    r = requests.get(url=request)

    return r.text

def getuserid(minecraft):

    import requests

    # api-endpoint
    URL = "https://api.masusniper.de/getuserid.php?minecraft=" + minecraft

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    result = r.text

    id = result.replace("<br>", "")

    return id

def addserver(owner, version, type, bungee, port, domain, ram):
    import requests

    # api-endpoint
    URL = "https://api.masusniper.de/getuserid.php?minecraft=" + minecraft