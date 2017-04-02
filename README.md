# coucou for Raspberry-Pi

### What is this? ####

Whenever my DHCP server changes the IP address of my raspberry-Pi I have to look for it using nmap or similar. Static IP is not an option for me, and I don't want to be searching for my Raspberry-Pi everytime, so here comes coucou.py : )

This little script runs at boot and sends broadcast messages every 10 seconds.So you just have to turn on wireshark and wait for the broadcast message to reach you.
