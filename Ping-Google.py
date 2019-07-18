import os

hostname = "8.8.8.8" #example
response = os.system("ping -n 1 " + hostname)

#and then check the response...
if response == 0:
    print(hostname, 'is up!')
else:
    print(hostname, 'is down!')