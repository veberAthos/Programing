#--------------------------------------#
#           MODULE 3 PROJECT           #
#--------------------------------------#
#
# USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE
#
# veberathos@gmail.com
# 03/16/2023

import re

menu = """
#--------------------------------------#
#           MODULE 3 PROJECT           #
#--------------------------------------#
#
# USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE
#
# veberathos@gmail.com
# 03/16/2023

Select which section to run:
1. While
2. Binary converter
3. List without duplicate
4. Subnetting Calculator
5. Regex Challenge
6. Run All
0. Exit
"""

# 1. While [20%]
# In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it 
# remains unproven) which can be described in the following way:
#   1. take any non-negative and non-zero integer number and name it c0;
#   2. if it's even, evaluate a new c0 as c0 ÷ 2;
#   3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
#   4. if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.
# Of course, it's an extremely complex task to use a computer in order to prove the hypothesis for 
# any natural number (it may even require artificial intelligence), but you can use Python to check 
# some individual numbers. Maybe you'll even find the one which would disprove the hypothesis.
# Write a program which reads one natural number and executes the above steps as long as c0 
# remains different from 1. We also want you to count the steps needed to achieve the goal. Your 
# code should output all the intermediate values of c0, too.
# Hint: the most important part of the problem is how to transform Collatz's idea into a while loop -
# this is the key to success.
# Test your code using the data we've provided.
def WHILE():
    print("#---------------------//---------------------#")
    print("1. While: ")

    c0 = int(input("Enter any non-negative and non-zero integer number: "))

    steps = int()

    while True:
        if c0 == 1:
            break
        elif c0%2 == 0:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 + 1

        print(int(c0))
        steps += 1

    print("Steps = ",steps)

    print("#---------------------//---------------------#\n")
    return

# 2. Binary converter [20%]
# You need to create code in which:
# a. Ask the user about which data would like to convert (1- Binary to Decimal 2- Decimal to 
# Binary)
# b. Ask the user for the number (Binary or Decimal based on the first decision)
# c. Display the conversion.
# You need to perform the following conversion:
# Binary to Decimal
# Decimal to Binary
# Note: You can use int(binary) for doing binary to decimal xor bin(decimal) for doing decimal to 
# binary (Both are not allowed)

def binaryConverter():
    print("2. Binay converter: ")

    print("""Please select which operation to perform:
    1. Binary to Decimal
    2. Decimal to Binary""")

    sel = input("Option: ")

    if sel == "1":
        print("1. Binary to Decimal selected")
        binary = input("Enter binary value: ")
        binRev = binary [::-1]
        # print(binary," -> ",binRev)
        decimal = 0
        for i in range(len(binRev)):
            if binRev[i] == "1":
                decimal = decimal + 2**i
        print(f"Binary: {binary}\t->\tDecimal: {decimal}")
    elif sel == "2":
        print("2. Decimal to Binary selected")
        decimal = int(input("Enter Decimal value: "))
        quotient = decimal
        remainder = ""
        binary = ""

        while True:
            remainder = remainder + str(quotient%2)
            quotient = quotient//2
            if quotient == 0:
                break

        binary = remainder [::-1]
        print(f"Decimal: {decimal}\t->\tBinary: {binary}")
    else:
        print("Wrong option selected")

    print("#---------------------//---------------------#\n")
    return

# 3. List without duplicate [20%]
#
def listWoDupl():
    print("3. List without duplicate: ")

    menu = """
    Do you want to enter a list? if not we'll use the predefined. Y/N: """

    preDef = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

    userList = []
    userListStr = ""

    while True:
        print(menu,end="")
        select = input().lower()
        if select == "y":    
            userListStr = input("Enter list of numbers separed by , : ")

            userList = re.split(",",userListStr)
            # print(userListStr," ",userList)

        elif select == "n":
            userList = preDef[:]
        else:
            print("Wrong option")

        temporal = userList[:]
        temporal.sort()
        temporal2 = []

        for i in range(len(temporal)):
            if i < len(temporal)-1:
                if temporal[i] != temporal[i+1]:
                    temporal2.append(temporal[i])
            else:
                temporal2.append(temporal[i])
        
        print("Original List was: ",userList)
        print("List values are: ",temporal2)

        select = input("Do you want to make another list? Y/N: ").lower()

        if select == "y":
            print("Let's continue!")
            continue
        elif select == "n":
            print("Bye!")
            break
        else:
            print("I'm gona reset the program either way... :)")

    print("#---------------------//---------------------#\n")
    return

# 4. Subnetting Calculator (based) [20%]:
# You will write a code that performs the following:
    # 1. Ask the user to ingress ip address (format 192.168.10.1)
    # 2. Ask the user to ingress subnet mask (format: 255.255.255.128)
    # 3. Display the following information:
    # a. Subnet ID
    # b. Number of Hosts
    # c. Broadcast ID
    # d. First Usable IP address
    # e. Last Usable IP address

def subnetCalc():
    print("4. Subnetting Calculator (based): \n")

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
    
    print("#---------------------//---------------------#\n")
    return

# Write a RegEx for matching with all your email account and replace to format 

# username: <username> domain: <domain>

def extraRegex():
    print("Extra Regex: \n")

    print("-----> version 1")

    email = input("Please enter your email: ")

    userDir = re.split("@",email)

    print (f"username: <{userDir[0]}> domain: <{userDir[1]}>")

    print("-----> version 2")

    userList = []
    while True:
        email2 = input("Please enter your email: ")

        user = re.split("@",email2)

        userDir2 = {
            "username": user[0],
            "domain": user[1]
        }
        
        userList.append(userDir2)

        control = input("Do you want to enter another email? Y/N: ").lower()
        if control == "y":
            print("Lets continue!")
            continue
        else:
            break

    print("All username and domains: ")

    for i in userList:
        print ("username: <{0}> domain: <{1}>".format(i["username"],i["domain"]))
    return

while True:
    print(menu)

    opt = input("Choice: ")

    if not re.match(r"[0-6]",opt):
        print("Error, option incorrect. Try again")
        continue
    elif opt.find("1") != -1:
        WHILE()
        if input("Press any key to continue"):
            continue
    elif opt.find("2") != -1:
        binaryConverter()
        if input("Press any key to continue"):
            continue
    elif opt.find("3") != -1:
        listWoDupl()
        if input("Press any key to continue"):
            continue
    elif opt.find("4") != -1:
        subnetCalc()
        if input("Press any key to continue"):
            continue
    elif opt.find("5") != -1:
        extraRegex()
        if input("Press any key to continue"):
            continue
    elif opt.find("6") != -1:
        WHILE()
        binaryConverter()
        listWoDupl()
        subnetCalc()
        extraRegex()
        if input("Press any key to continue"):
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
