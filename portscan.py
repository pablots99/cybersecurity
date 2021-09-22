#!bin/python

from os import error
import sys
import socket
from datetime import date, datetime


if(len(sys.argv) != 2):
	 "syntax: python3 portscanner.py <ip>"
	 exit(0)

target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4

print("Scanning target:",target)

starttime = datetime.now()


try:
	for port in range(0,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET => ipv4 SOCK_STREAM => port
		socket.setdefaulttimeout(1)
		res = s.connect_ex((target, port))
		if res == 0:
			print("port:",port,"open")
		s.close()
except KeyboardInterrupt:
	print("program interrupted")
	sys.exit()
except socket.gaierror:
	print("host name could not be resolved")
	sys.exit()
except socket.error:
	print("couldn't connect to server",error)
	exit()

print("time:",datetime.now() - starttime)
