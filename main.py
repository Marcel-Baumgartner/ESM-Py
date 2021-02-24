#! /bin/python3

# This script is made for Endelon Hosting
# Made by Marcel Baumgartner

# Imports

import sys
import os
import os.path
import subprocess
from os import path
import packagemanager
import database
from datetime import datetime
programmpath = os.getcwd()
import random
import api

# Config

serversFile = "servers.xml"
wait = 180
stopcommand = "./stop_server.sh "
startcommand = "./start_server.sh "

# End Config

def __main__ ():

    __libcheck__()

    if(len(sys.argv) < 2):
        print("Systax: <scan|ram|add|delete|status|start>")
        exit(0)
    else:
        print("Starting ESM-Py with mode " + sys.argv[1])

    if ("True" == str(path.exists("./timecache"))):
        print("./timecache already exists")
    else:
        try:
            os.mkdir("timecache")
        # Create folder for time files
        except OSError:
            print("Error creating ./timecache/ folder")
            exit()
        else:
            print("Sucessfully createt ./timecache folder")

    mode = sys.argv[1]

    if(mode == "scan"):
        __scan__()
    else:
        if (mode == "ram"):
            __ram__()
        else:
            if (mode == "start"):
                __start__()
            else:
                print("Unknown mode " + mode)

def __libcheck__ ():
    print("Checking for needed libararies")

    # Used Libs

    packagemanager.pinstall("mcstatus")
    packagemanager.pinstall("requests")
    packagemanager.pinstall("urllib")


    # End Used Libs

def __ram__ ():

    cacheFile = str(random.randint(1, 999999)) + ".cache"
    os.system("ps aux | head -1; ps aux | sort -rnk 4 | head -5 > " + cacheFile)

    cache = open(cacheFile)

    output = cache.read()

    cache.close()
    os.system("rm " + cacheFile)

    print(output)

def __start__():

    from mcstatus import MinecraftServer

    if(len(sys.argv) < 2):
        print("Syntax esm start <ip>")
        exit(0)

    if(database.existip("servers.xml", sys.argv[2]) == False):
        print("[EEC]2")
        exit(0)

    try:
        server = MinecraftServer.lookup(sys.argv[2])
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

        # Get needed memory

        ip = sys.argv[2]

        user = database.getuserfromip("servers.xml", ip)
        needed = int(database.getramfromuser("servers.xml", user))

        if (free > needed):
            print("Server can start")
            os.system(startcommand + user + " " + str(needed))
            print("[EEC]0")
        else:
            print("Not enought memory")
            print("[EEC]1")

def __scan__ ():
    print("Scanning Servers")

    from mcstatus import MinecraftServer

    servers = database.get_ips(serversFile)

    for ip in servers:

        print(ip)

        try:
            owner = database.getuserfromip(serversFile, ip)

            server = MinecraftServer.lookup(ip)
            status = server.status()

            players = status.players.online

            motd = str(status.description)

            if motd.find("[EEC]4") == -1:
                print("Server is online")
            else:
                print("Wanted Error")
                x = (2 / 0)

            # Read current DateTime

            currentdatetime = datetime.now()

            if (players > 0):
                print("Saving time")
                towrite = currentdatetime.strftime("%d-%m-%Y-%H:%M:%S")

                # Save current time and date

                file = open('./timecache/' + owner, 'w')

                file.write(towrite)
                file.close()
            else:
                file = open("./timecache/" + owner, "r")
                txt = file.read()
                file.close()
                txt = txt.replace("\n", "")
                readdatetime = datetime.strptime(txt, "%d-%m-%Y-%H:%M:%S")

                print(txt)

                # Calculate the difference

                diffdatetime = currentdatetime - readdatetime

                diff = diffdatetime.seconds / 60

                if (diff > wait):
                    print("Difference:  " + str(diff))
                    print("Stopping ...")
                    os.system(stopcommand + owner)

                    towrite = currentdatetime.strftime("%d-%m-%Y-%H:%M:%S")

                    # Save current time and date

                    file = open('./timecache/' + owner, 'w')

                    file.write(towrite)
                    file.close()
                else:
                    print("Not now")
        except:
            print("Saving time")
            currentdatetime = datetime.now()
            towrite = currentdatetime.strftime("%d-%m-%Y-%H:%M:%S")

            # Save current time and date

            file = open('./timecache/' + owner, 'w')

            file.write(towrite)
            file.close()



# Call main method
__main__()
