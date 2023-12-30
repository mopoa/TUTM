# Simple packet filtering using sockets
import socket

virusSign=[]

def firewall(packet):
    
    # remember this part 
    # u need to add rule or connect the gui
    # remembeeeeeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrr
    
    return True  # Allow all traffic

def main():
    # Set up a socket to capture network traffic
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))

    while True:
        packet, _ = s.recvfrom(65535)
        if firewall(packet):
            # Process the packet further or allow it to pass
            print("Packet allowed:", packet)

if __name__ == "__main__":
    main()

