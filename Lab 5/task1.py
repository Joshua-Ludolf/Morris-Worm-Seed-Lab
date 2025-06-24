#!/bin/env python3

'''
	Name: Joshua Ludolf
	Class: CSCI 4321 - Computer Security
'''

from scapy.all import *

print(f'SNIFFING PACKETS..........')

def print_packet(pkt):
	print(f'Source IP:{pkt[IP].src}')
	print(f'Destination IP:{pkt[IP].dst}')
	print(f'Protocol:{pkt[IP].proto}')
	print(f'\n')
	
	
pkt = sniff(iface='br-f780cb00a22f', filter='ip', prn=print_packet)
