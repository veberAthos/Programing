#--------------------------------------#
#           REGEX CHALLENGE            #
#--------------------------------------#
#
# USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE
#
# veberathos@gmail.com
# 03/15/2023

# Write a RegEx for matching with all your email account and replace to format 

# username: <username> domain: <domain>

import re

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