#!/bin/env python3

'''
    Name: Joshua Ludolf
    Class: CSCI 4321 - Computer Security
'''

from scapy.all import*

def spoof_pkt(pkt):
	if ICMP in pkt and pkt[ICMP].type == 8:
		a = IP()
		a.src = pkt[IP].dst
		a.dst = pkt[IP].src
		a.ihl = pkt[IP].ihl
		b = ICMP()
		b.type = 0
		b.id = pkt[ICMP].id
		b.seq = pkt[ICMP].seq
		data = pkt[Raw].load
		p = a/b/data
		a.show()
		b.show()
		send(p)
		
pkt = sniff(filter = 'icmp', prn=spoof_pkt)
