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

def getserver(id):

    import requests

    URL = "https://api.masusniper.de/getserver.php?id=" + id

    r = requests.get(url=URL)

    result = r.text

    server = result.replace("<br>", "")

    return server

def addserver(owner, version, type, bungee, port, domain, ram):
    import requests

    # api-endpoint
    URL = "https://api.masusniper.de/getuserid.php?owner=" + owner + "&version" + version + "&type" + type + "&bungee" + bungee + "&port" + port + "&domain" + domain + "&ram" + ram

    r = requests.get(url=URL)

    result = r.text

    return result

def getram(id):
    import requests

    URL = "https://api.masusniper.de/getram.php?id=" + id

    r = requests.get(url=URL)

    result = r.text

    ram = result.replace("<br>", "")

    return ram

def gettype(id):
    import requests

    URL = "https://api.masusniper.de/gettype.php?id=" + id

    r = requests.get(url=URL)

    result = r.text

    type = result.replace("<br>", "")

    return type

def getport(id):
    import requests

    URL = "https://api.masusniper.de/getport.php?id=" + id

    r = requests.get(url=URL)

    result = r.text

    port = result.replace("<br>", "")

    return port

def getbungee(id):
    import requests

    URL = "https://api.masusniper.de/getbungee.php?id=" + id

    r = requests.get(url=URL)

    result = r.text

    bungee = result.replace("<br>", "")

    return bungee

def getdomain(id):
    import requests

    URL = "https://api.masusniper.de/getdomain.php?id=" + id

    r = requests.get(url=URL)

    result = r.text

    domain = result.replace("<br>", "")

    return domain

def getversion(id):
    import requests

    URL = "https://api.masusniper.de/getversion.php?id=" + id

    r = requests.get(url=URL)

    result = r.text

    version = result.replace("<br>", "")

    return version

def geturl(version):
    import requests

    URL = "https://api.masusniper.de/geturl.php?name=" + version

    r = requests.get(url=URL)

    result = r.text

    url = result.replace("<br>", "")

    return url

def getminecraft(id):
    import requests

    URL = "https://api.masusniper.de/getminecraft.php?id=" + id

    r = requests.get(url=URL)

    result = r.text

    minecraft = result.replace("<br>", "")

    return minecraft
