# coucou for Raspberry-Pi

### What is this? ####

Whenever my DHCP server changes the IP address of my raspberry-Pi I have to look for it using nmap or similar. Static IP is not an option for me, and I don't want to be searching for my Raspberry-Pi everytime, so here comes coucou.py : )

This little script runs at boot and sends broadcast messages every 10 seconds. So you just have to turn on wireshark and wait for the broadcast message to reach you.

If you don't have wireshark, you can run tcpdump:

``` sudo tcpdump dst 255.255.255.255 and port 65535 -n -c 1 ```

Or netcat...

``` nc -l -p 65535 -u -v ```

Or you can run this coucou-catcher in python:

``` python
#!/usr/bin/env python

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',65535))
m=s.recvfrom(1024)
print m[1][0]

```
