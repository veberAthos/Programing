#---------------------------------#
#       DATA TYPE OUTPUT          #
#---------------------------------#
#
# USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE
#
# veberathos@gmail.com
# 03/08/2023

# 1. Write one code, using the print() function whose expected output will be:

# "It's"

# ""the first""

# """exercise"""

# No restriction about the numbers of print()

# Extra: Try to do with only one print and without \

# print('"'+"It's"+'"','""'+"the firts"+'""','"""'+"exercise"+'"""',sep="\n")

msg = ["It's", "the first", "exercise"]

for i in range(len(msg)):
    print('"'*(i+1),msg[i],'"'*(i+1))


#---------------------------------------------------------------

# 2. What is the result of the following operation?

# print("test" + 1)
    # TypeError: can only concatenate str (not "int") to str
# print("test" + " 1")
    # prints-> test 1
# print("test" * 2)
    # prints-> testtest

print('print("test" + 1)')
print('TypeError: can only concatenate str (not "int") to str')
print('print("test" + " 1")')
print("test" + " 1")
print('print("test" * 2)')
print("test" * 2)