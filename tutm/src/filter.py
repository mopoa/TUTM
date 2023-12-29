from scapy.all import *
from scapy.layers.inet import *
def packet_callback(packet):
    # Extract source and destination IP addresses
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    # Extract source and destination ports
    src_port = packet[IP].sport
    dst_port = packet[IP].dport

    # Implement your filtering logic here
    if src_ip == 'allowed_ip' and dst_port == 80:
        # Allow the packet
        print(f"Allowed packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
    else:
        # Drop or log the packet
        print(f"Blocked packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")

# Sniff network traffic and apply the packet_callback function
sniff(prn=packet_callback, store=0)
