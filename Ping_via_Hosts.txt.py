import sys
import os
import platform
import subprocess

plat = platform.system()
scriptDir = sys.path[0]
hosts = os.path.join(scriptDir, 'hosts.txt')
hostsFile = open(hosts, "r")
lines = hostsFile.readlines()
for line in lines:
    line = line.strip( )
    if plat == "Windows":
        response = os.system("ping -n 1 " + line )
       
    if response == 0:
        print(line, 'is up!')
    else:
        print(line, 'is down!')
hostsFile.close()
