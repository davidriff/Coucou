#!/usr/bin/env python

import socket
import time


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

host = '255.255.255.255';
port = 65535;


msg="Hey stranger... Coucou : )"

while True:
	s.sendto(msg, (host, port))
	time.sleep(15)
