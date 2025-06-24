#!/bin/env python3

'''
    Name: Joshua Ludolf
    Class: CSCI 4321 - Computer Security
'''

from scapy.all import *

def traceroute(dest_ip):
    # Create lists to store results
    router_ips = []
    ttl = 1
    
    while True:
        # Create IP packet with destination IP and set TTL
        ip_packet = IP(dst=dest_ip, ttl=ttl)
        # Create ICMP Packet
        icmp_packet = ICMP()
        # Send packet and receive the response
        response = sr1(ip_packet/icmp_packet, verbose=0, timeout=2)
        if response is None:
            print(f'No response for TTL = {ttl}')
            break
        else:
            # Get the IP address of the router
            router_ip = response.src
            print(f'TTL = {ttl} | Router IP = {router_ip}')
            router_ips.append(router_ip)
            
            # Check if the destination is reached
            if response.type == 0:
                print(f'Destination reached.')
                break
        
        # Increment TTL
        ttl += 1
        
    return router_ips

# Destination IP address
destination_ip = '1.2.3.4'

# Perform traceroute
routers = traceroute(destination_ip)
print(f'Routers in the path: {routers}')
