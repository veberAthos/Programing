#---------------------------------#
#           WHILE LOOP            #
#---------------------------------#
#
# USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE
#
# veberathos@gmail.com
# 03/14/2023

# Your task is to write a program which reads the number of blocks the builders have, 
# and outputs the height of the pyramid that can be built using these blocks.

# Note: the height is measured by the number of fully completed layers
# - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.

# Test your code using the data we've provided.

# Sample input: 6

# Expected output: The height of the pyramid: 3

# Sample input: 20

# Expected output: The height of the pyramid: 5

# Sample input: 1000

# Expected output: The height of the pyramid: 44

# Sample input: 2

# Expected output: The height of the pyramid: 1

blockQty = int(input("Enter how many blocks the builders have: "))
height = 0
used = 1

while used <= blockQty:
	height += 1
	blockQty -= used
	used += 1

print("The height of the pyramid: ",height)
