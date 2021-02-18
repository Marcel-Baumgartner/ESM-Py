# Note: Only a library for ESM-Py

# Imports
#from pip._internal import main as pipmain
import os

# Methods

def pinstall(packagename):
 #pipmain(['install', packagename])
 os.system("pip3 install --user " + packagename)