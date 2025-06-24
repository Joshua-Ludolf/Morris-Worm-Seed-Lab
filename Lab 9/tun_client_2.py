#!/usr/bin/env python3

import fcntl
import struct
import os
import select
from scapy.all import *

IP_A = "10.9.0.11"
PORT = 9090
TUNSETIFF = 0x400454ca
IFF_TUN = 0x0001
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000

# Create a tun interface
tun = os.open("/dev/net/tun", os.O_RDWR)
ifr = struct.pack('16sH', b'ludolf%d', IFF_TUN | IFF_NO_PI)
ifname_bytes = fcntl.ioctl(tun, TUNSETIFF, ifr)
ifname = ifname_bytes.decode('UTF-8')[:16].strip("\x00")
print("Interface Name {}".format(ifname))

# Set up the tun interface and routing
os.system("ip addr add 192.168.53.99/24 dev {}".format(ifname))
os.system("ip link set dev {} up".format(ifname))

# Set up routing
os.system("ip route add 192.168.60.0/24 dev {}".format(ifname))

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



# Assuming `tun` and `sock` are already created
while True:
    # Use select to monitor both tun and socket file descriptors
    ready, _, _ = select.select([sock, tun], [], [])
    for fd in ready:
        if fd is tun:
            # Read a packet from the tun interface
            packet = os.read(tun, 2048)
            if packet:
                pkt = IP(packet)
                print("From TUN interface: {} --> {}".format(pkt.src, pkt.dst))
                # Send the packet via the socket
                sock.sendto(packet, (IP_A, PORT))
        elif fd is sock:
            # Read a packet from the socket
            data, (ip, port) = sock.recvfrom(2048)
            pkt = IP(data)
            print("From socket: {} --> {}".format(pkt.src, pkt.dst))
            # Send the packet to the TUN interface
            os.write(tun, data)
