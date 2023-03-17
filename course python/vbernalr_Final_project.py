#--------------------------------------#
#           FINAL PROJECT              #
#--------------------------------------#
#
# USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE
#
# veberathos@gmail.com
# 03/17/2023

import re

menu = """
#--------------------------------------#
#           FINAL PROJECT              #
#--------------------------------------#
#
# USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE
#
# veberathos@gmail.com
# 03/17/2023

To continue press any key, to exit press 0: """

def ipCheck(ip):
    match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip)
    
    if not match:
        print(f"The IP address/Subnet mask {ip} is not valid")
        return False

    ip = str(ip)

    octets = ip.split(".")

    for ip_octet in octets:
        if int(ip_octet) < 0 or int(ip_octet) > 255:
            print(f"The IP address/Subnet mask {ip} is not valid")
            return False
    
    # print(f"The IP address/Subnet mask {ip} is valid")
    
    return True


while True:
    print(menu,end="")

    if input().find("0") == -1:
        print("Enter IP address and Mask, both in decimal form:\n")

        netHost = input("Host in the Network: ")
        mask = input("Network Mask: ")

        netID = []
        broadcast = []
        blockSize = 0
        broadcastnum = 0

        if ipCheck(netHost) and ipCheck(mask):
            netOct = netHost.split(".")
            maskOct = mask.split(".")

            netOct = [int(i) for i in netOct]
            maskOct = [int(i) for i in maskOct]

            # print(netOct)
            # print(maskOct)

            for i in range(4):
                netID.append(netOct[i] & maskOct[i])

            for i in range(4):
                if maskOct[i] == 255:
                    broadcast.append(netID[i])
                elif maskOct[i] == 0:
                    broadcast.append(255)
                else:
                    blockSize = 256-maskOct[i]
                    broadcast.append(blockSize)
                    while True:
                        broadcastnum = broadcastnum + blockSize
                        if broadcastnum > netID[i]:
                            broadcast[i] = broadcastnum - 1
                            break
            
            # print(broadcast)
            
            print(f"Network ID: \t\t\t{netID[0]}.{netID[1]}.{netID[2]}.{netID[3]}")
            print(f"Number of hosts: \t\t{(broadcast[3]-1)-(netID[3]+1)}")
            print(f"Broadcast ID: \t\t\t{broadcast[0]}.{broadcast[1]}.{broadcast[2]}.{broadcast[3]}")
            print(f"First Usable IP adress: \t{netID[0]}.{netID[1]}.{netID[2]}.{netID[3]+1}")
            print(f"Last Usable IP adress: \t\t{broadcast[0]}.{broadcast[1]}.{broadcast[2]}.{broadcast[3]-1}")
        if input():
            continue
    else:
        ext = input("Are you sure to exit? Y/N: ").lower()
        if ext == "y":
            print("Bye!")
            break
        elif ext == "n":
            print("Let's continue!")
            continue
        else:
            print("Wrong answer, I'm gona start all over")
            continue
