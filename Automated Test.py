import sys
import os
import platform
import subprocess
from datetime import datetime

plat = platform.system()
scriptDir = sys.path[0]

firewalls = os.path.join(scriptDir, 'firewalls.txt')
firewallsFile = open(firewalls, "r")
firelines = firewallsFile.readlines()

hosts = os.path.join(scriptDir, 'hosts.txt')
hostsFile = open(hosts, "r")
hostlines = hostsFile.readlines()

def firewalls():

    for line in firelines:
        line = line.strip( )
        if plat == "Windows":
            response = os.system("ping -n 1 " + line)

        if response == 0:
            log.write(line + ' is up!\n')
            print(line + ' is up!')
        else:
            log.write(line + ' is down!\n')
            print(line + ' is down!')

firewallsFile.close()

def Servers():

    for line in hostlines:
        line = line.strip( )
        if plat == "Windows":
            response = os.system("ping -n 1 " + line)

        if response == 0:
            log.write(line + ' is up!\n')
            print(line + ' is up!')
        else:
            log.write(line + ' is down!\n')
            print(line + ' is down!')

hostsFile.close()

if __name__ == "__main__":
    now = datetime.now() #zfill below fills in zeros to the left if a single digit
    filename = str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2) + "_" + str(now.hour).zfill(2) + str(now.minute).zfill(2) + "_Ping_Results.txt"
    try:
        with open(filename, 'r') as f: #if file is already present, don't overwrite and append _1 to filename
            filename = str(now.year) + str(now.month).zfill(2) + str(now.day).zfill(2) + "_" + str(now.hour).zfill(2) + str(now.minute).zfill(2) + "_Ping_Results_1.txt"
    except:
        pass

    log = open(filename, 'w+')
    firewalls()
    Servers()
    log.close()
