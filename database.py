# Note: Only a library for ESM-Py

# Imports

from xml.dom import minidom

# Methods

def get_ips(filename):
    xmldoc = minidom.parse(filename)
    itemlist = xmldoc.getElementsByTagName('server')

    result = []

    i = 0

    for s in itemlist:
        result.append(s.attributes['ip'].value)
        i = i + 1

    return result

def getuserfromip(filename, ip):
    xmldoc = minidom.parse(filename)
    itemlist = xmldoc.getElementsByTagName('server')

    result = "404"

    for s in itemlist:
        if(s.attributes['ip'].value == ip):
            result = s.attributes['owner'].value

    return result

def getramfromuser(filename, user):
    xmldoc = minidom.parse(filename)
    itemlist = xmldoc.getElementsByTagName('server')

    result = "404"

    for s in itemlist:
        if(s.attributes['owner'].value == user):
            result = s.attributes['ram'].value

    return result
