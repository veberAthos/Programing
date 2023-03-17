#---------------------------------#
#         MODULE 2 PROJECT        #
#---------------------------------#
#
# USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE
#
# veberathos@gmail.com
# 03/10/2023

# 1. Arrows (30%): You need to create code in which the expected output is the following:
print("#---------------------//---------------------#")
print("1. Arrow: ")
arrow = """
    *           *           *           *
   * *         * *         * *         * *
  *   *       *   *       *   *       *   *
 *     *     *     *     *     *     *     *
***   ***   ***   ***   ***   ***   ***   ***
  *   *       *   *       *   *       *   *
  *   *       *   *       *   *       *   *
  *****       *****       *****       *****
"""

print(arrow)
print("#---------------------//---------------------#\n")

# 2. Currency converter (30%): You need to create code in which:
# a. Ask the user to ingress a currency value.
# b. Display the result after the conversion.
# You need to perform the following conversion:
# US Dollar to COP
# COP to US Dollar
# Euro to COP
# COP to Euro

print("2. Currency converter: ")
USDtoCOP = 4763.40
COPtoUSD = round(1/USDtoCOP,5)

EURtoCOP = 5068.47
COPtoEUR = round(1/EURtoCOP,5)

# print(USDtoCOP,COPtoUSD,EURtoCOP,COPtoEUR,sep="\t")
print("Please enter a currency value: ")
cop = input("Colombian Peso(s): ")
usd = input("Dollar(s): ")
eur = input("Euro(s): ")

if cop:
    print("\nCOP to others here:")
    cop = float(cop)
    print("$ {0} COP is equivalent to: $ {1} USD and $ {2} EUR\n".format(cop,round(cop*COPtoUSD,2),round(cop*COPtoEUR,2)))

if usd:
    print("USD to COP here:")
    usd = float(usd)
    print("$ {0} USD is equivalent to: $ {1} COP\n".format(usd,round(usd*USDtoCOP,2)))

if eur:
    print("EUR to COP here:")
    eur = float(eur)
    print("$ {0} EUR is equivalent to: $ {1} COP\n".format(eur,round(eur*EURtoCOP,2)))

print("#---------------------//---------------------#\n")

# 3. Day clock (40%)
# You will write a code that performs the following:
# 1.	Ask the user to ingress seconds.
# 2.	Ask the user to ingress minutes.
# 3.	Ask the user to ingress hours.
# 4.	Ask the user to ingress days.
# 5.	Display the output in the following format:
#       Day number (day)
#       hh:mm:ss

# 1.	This clock will work like a normal clock which means the following:
# a.    The seconds' number will not overpass 59 seconds (but the user can ingress a value over 59)
# b.    The minutes' number will not overpass 59 minutes (but the user can ingress a value over 59)
# c.    The hours' number will not overpass 23 hours (but the user can ingress a value over 23)



# Data for testing
# 1.	Seconds: 15, Minutes: 45, Hours: 9, Day: 7    
#    Expected output: Day number 7  9:45:15
# 2.	Seconds: 75, Minutes: 30, Hours: 15, Day: 14    
#   Expected output: Day number 14  15:31:15
# 3.	Seconds: 45, Minutes: 169, Hours: 16, Day: 20    
#   Expected output: Day number 20  18:49:45
# 4.	Seconds: 175, Minutes: 69, Hours: 100, Day: 1    
#   Expected output: Day number 5  5:11:55

print("2. Day Clock (40%): ")

sec = int(input("Enter seconds value: "))
min = int(input("Enter minutes value: "))
hrs = int(input("Enter hours value: "))
day = int(input("Enter days value: "))

clockMin = sec//60 + min%60
clockHrs = min//60 + hrs%24
clockSec = sec%60
day = day + hrs//24

print("\n---> Day number {0} {1}:{2}:{3}\n".format(day,clockHrs,clockMin,clockSec))

print("#---------------------//---------------------#\n")