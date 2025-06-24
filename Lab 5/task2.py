#!/bin/env python3

'''
	Name: Joshua Ludolf
	Class: CSCI 4321 - Computer Security
'''

from scapy.all import *

a = IP()
a.dst = '10.0.2.3'
b = ICMP()
p = a/b
send(p)
