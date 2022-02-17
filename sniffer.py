import os
from collections import Counter
from scapy.all import sniff



packet_counts = Counter()

capturedPacketsSize = 0

## Define our Custom Action function
def custom_action(packet):
    # Create tuple of Src/Dst in sorted order
    global capturedPacketsSize
    global packet_counts
    capturedPacketsSize += len(packet)
    key = tuple(sorted([packet[0][1].src, packet[0][1].dst]))
    packet_counts.update([key])
    return "Packet #{0}: {1} ==> {2}".format(sum(packet_counts.values()), packet[0][1].src, packet[0][1].dst)



print("_____.:|Calculating Bite-rate|:._____")
host_addr = input("Please enter the destination address to sniff the packet: " + " ")

while 1:
    print("Analysing Multicast packets")
    pkt = sniff(iface="eth0", filter="host " + host_addr, prn=custom_action, timeout=1)
    print("\n".join("{0} <--> {1} :{2}".format(key[0], key[1], count) for key, count in packet_counts.items()))
    packet_counts.clear()
    print("Byterate for this moment is equal to: {0} Bytes per second".format(capturedPacketsSize))
    if capturedPacketsSize > 0:
        print(50 * "-")
        print("Packet captured succesfully!")
        print(50 * "-")
        print("What do you want to do next?")
        print(50 * "-")
        print("Exit the sniffer  (1)")
        print(50 * "-")
        input_sub = input("Please select you input: " + " ")
        if input_sub == "1":
            print(50 * "-")
            print("Exiting sniffer, thank you for using the program!")
            print(50 * "-")
            input("Press any key to exit the sniffer....")
            os.system("clear")
            exit()
