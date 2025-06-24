#!usr/bin/python3

'''
	Name: Joshua Ludolf
	Class: CSCI 4321 - Computer Security
'''

from scapy.all import *

ip = IP(src = "10.9.0.6", dst = "10.9.0.5")

tcp = TCP(sport = 9090, dport = 514, flags = "SA", seq = 269591059)

pkt = ip/tcp

ls(pkt)

send(pkt, verbose = 0)



