import socket

blackList=[]

def firewall(packet):
    
    for i in blackList:
        if packet == blackList[i]:
            return False;
    return True;

def main():
    #capturing
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003));

    while True:
        packet, _ = s.recvfrom(65535);
        if firewall(packet):# checking if the packet is allowed
            print("Packet allowed:", packet);

if __name__ == "__main__":
    main()

