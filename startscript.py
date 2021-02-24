import sys
import api
import os

def start(user):
    from mcstatus import MinecraftServer

    userid = api.getuserid(user)
    serverid = api.getserver(userid)
    domain = api.getdomain(serverid)
    port = api.getport(serverid)

    ip = domain + ":" + port

    if (len(sys.argv) < 2):
        print("Syntax esm start <ip>")
        exit(0)
    try:
        server = MinecraftServer.lookup(ip)
        status = server.status()

        print("Server is already running")

        motd = str(status.description)

        if motd.find("[EEC]4") == -1:
            print("Server is online")
        else:
            print("Wanted Error")
            x = (1 / 0)

        print("[EEC]3")
    except:
        print("Checking for memory")

        # Get free memory

        cacheFile = str(random.randint(1, 999999)) + ".cache"
        os.system("cat /proc/meminfo > " + cacheFile)

        cache = open(cacheFile)

        lines = cache.readlines()

        cache.close()
        os.system("rm " + cacheFile)

        line = lines[1]

        line = line.replace(" ", "")
        line = line.replace("kB", "")

        freeA = int(line.split(":")[1])

        freeA = freeA / 1024 # "Free" Memory

        line = lines[2]

        line = line.replace(" ", "")
        line = line.replace("kB", "")

        freeC = int(line.split(":")[1]) # Buffered Memory (because you can also use bufferd / cached memory)

        freeC = freeC / 1024

        free = freeA + freeC

        needed = int(api.getram(serverid))

        if (free > needed):
            print("Server can start")
            bootstarp(serverid, userid)
            print("[EEC]0")
        else:
            print("Not enought memory")
            print("[EEC]1")

def bootstarp(serverid, userid):

    print("Starting Bootstrap")

    version = api.getversion(serverid)
    url = api.geturl(version)

    minecraft = api.getminecraft(userid)
    type = api.gettype(serverid)
    ram = api.getram(serverid)

    if type == "paper":
        # Update Serversoftware
        print("Downloading server jar ...")
        urllib.request.urlretrieve(url, '/home/' + minecraft + "/server.jar")

        # Update Config Files
        print("Downloading paper.yml ...")
        urllib.request.urlretrieve("https://api.masusniper.de/configs/paper.yml", '/home/' + minecraft + "/paper.yml")

        # Look if is bungee
        bungee = api.getbungee(serverid)

        if bungee == "1":
            print("Downloading spigot-proxy.yml ...")
            urllib.request.urlretrieve("https://api.masusniper.de/configs/spigot-proxy.yml", '/home/' + minecraft + "/paper.yml")
        else
            print("Downloading spigot.yml ...")
            urllib.request.urlretrieve("https://api.masusniper.de/configs/spigot.yml", '/home/' + minecraft + "/paper.yml")

        # Update server.properties

        lines = []

        f = open("/home/" + minecraft + "/server.properties", "r")
        for x in f:
            lines.append(x)
        f.close()

        f = open("/home/" + minecraft + "/server.properties", "w")
        for x in lines:
            f.write(x + "\n")
        f.close()

        os.system("sudo ./start_server " + minecraft + " " + ram)
    else:
        print("No update links set for server type " + type)