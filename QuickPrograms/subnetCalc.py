#---------------------------------#
#       SUBNET CALCULATOR         #
#---------------------------------#
#
# USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE
#
# veberathos@gmail.com
# 03/07/2023

import sys
import re

print("""
#---------------------------------#
#       SUBNET CALCULATOR         #
#---------------------------------#

USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE

veberathos@gmail.com
03/07/2023
""")

def ipCheck(ip):
    match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip)
    
    if not match:
       print(f"The IP address {ip} is not valid")
       return False
    
    ip = str(ip)

    octets = ip.split(".")

    for ip_octet in octets:
       if int(ip_octet) < 0 or int(ip_octet) > 255:
           print(f"The IP address {ip} is not valid")
           return False
    
    print(f"The IP address {ip} is valid")
    
    return True

# def checkClass(netID):
#     if netID[0] > 223:
#         return [255,255,255,255]
#     elif netID[0] > 191:
#         return [255,255,255,0]
#     elif netID[0] > 127:
#         return [255,255,0,0]
#     else:
#         return [255,0,0,0]


maskDict = {
    "8": "255.0.0.0",
    "9": "255.128.0.0",
    "10": "255.192.0.0",
    "11": "255.224.0.0",
    "12": "255.240.0.0",
    "13": "255.248.0.0",
    "14": "255.252.0.0",
    "15": "255.254.0.0",
    "16": "255.255.0.0",
    "17": "255.255.128.0",
    "18": "255.255.192.0",
    "19": "255.255.224.0",
    "20": "255.255.240.0",
    "21": "255.255.248.0",
    "22": "255.255.252.0",
    "23": "255.255.254.0",
    "24": "255.255.255.0",
    "25": "255.255.255.128",
    "26": "255.255.255.192",
    "27": "255.255.255.224",
    "28": "255.255.255.240",
    "29": "255.255.255.248",
    "30": "255.255.255.252",
    "31": "255.255.255.254",
    "32": "255.255.255.255"    
}

print("Enter at least one IP and Mask(prefix):\n")

netID = input("Network ID: ")
mask = input("Network Mask(prefix): ")
netHost = input("Host in the Network: ")

#print(netID,mask,netHost,sep="\n")

# print(ipCheck(netID))


if ipCheck(netID) and re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",mask):
    if int(mask) <= 8:
        netType = "A"
    elif int(mask) <= 16:
        netType = "B"
    elif int(mask) <= 24:
        netType = "C"
    elif int(mask) <= 28:
        netType = "D"
    elif int(mask) <= 32:
        netType = "E"
    else:
        print(f"Error, {mask} is not a valid subnet mask prefix!")
        sys.exit()
    


#     print("netID: \t",netID)
#     print(f"Mask: {mask}(prefix), {maskDict[mask]}")
    # print(f"Firts usable host: \t{netID+1}")
    # print(f"Last usable host: \t{netID+1}")

