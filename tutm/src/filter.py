from scapy.all import *
from scapy.layers.inet import *

def read_rules(blSrcIp):
    with open("../data/whitelist.txt", "r") as file:
        blSrcIp=file.readlines();

def packet_callback(packet):
    # extracting the src and dst ipv4 addresses
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    # extracting the ports
    src_port = packet[IP].sport
    dst_port = packet[IP].dport

    blSrcIp=[]
    read_rules(blSrcIp=blSrcIp)

    # Filtering rules
    for i in blSrcIp:
            # Allow the packet
        if src_ip == blSrcIp[i] and dst_port == 80:
            print(f"Blocked packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
        else:
            print(f"Allowed packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
            
# Sniff network traffic and apply the packet_callback function
sniff(prn=packet_callback, store=0)
