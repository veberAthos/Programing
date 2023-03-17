#---------------------------------#
#      DATA TYPE OPERATION        #
#---------------------------------#
#
# USE AT YOUR OWN RISK. NOT FOR COMMECIAL OR PRODUCTION USE
#
# veberathos@gmail.com
# 03/09/2023

# Data Type Operations
# Perform the basic arithmetic operation (+, -,*, /) with the following data type

# str with str, int, float, bool

# int with str, int, float, bool

# float with str, int, float, bool

# bool with str, int, float, bool

# Writing down the results data type
#------------------------------------------------
print("-> + <-:")

print("str with str, int, float, bool")
print("0"+"1")      # prints: 01, str
# print("0"+1)      # TypeError: can only concatenate str (not "int") to str
# print("0"+1.0)    # TypeError: can only concatenate str (not "float") to str
# print("0"+True)   # TypeError: can only concatenate str (not "bool") to str

print("int with str, int, float, bool")
# print(10+"1")     # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(10+10)        # prints: 20, int
print(10+10.0)      # prints: 20.0, float
print(10+True)      # prints: 11, int

print("float with str, int, float, bool")
# print(10.0+"10.0")# TypeError: unsupported operand type(s) for +: 'float' and 'str'
print(10.0+10)      # prints: 20.0, float
print(10.0+10.0)    # prints: 20.0, float
print(10.0+True)    # prints: 11.0, float

print("bool with str, int, float, bool")
# print(True+"10.0")# TypeError: unsupported operand type(s) for +: 'bool' and 'str'
print(True+10)      # prints: 11, int
print(True+10.0)    # prints: 11.0, float
print(False+True)   # prints: 1, int

#------------------------------------------------

print("-> - <-:")

print("str with str, int, float, bool\n")
# print("0"-"1")    # TypeError: unsupported operand type(s) for -: 'str' and 'str'
# print("0"-1)      # TypeError: unsupported operand type(s) for -: 'str' and 'int'
# print("0"-1.0)    # TypeError: unsupported operand type(s) for -: 'str' and 'float'
# print("0"-True)   # TypeError: unsupported operand type(s) for -: 'str' and 'bool'

print("int with str, int, float, bool")
# print(10-"1")     # TypeError: unsupported operand type(s) for -: 'int' and 'str'
print(10-10)        # prints: 0, int
print(10-10.0)      # prints: 0.0, float
print(10-True)      # prints: 9, int

print("float with str, int, float, bool")
# print(10.0-"10.0")# TypeError: unsupported operand type(s) for -: 'float' and 'str'
print(10.0-10)      # prints: 0.0, float
print(10.0-10.0)    # prints: 0.0, float
print(10.0-True)    # prints: 9.0, float

print("bool with str, int, float, bool")
# print(True-"10.0")# TypeError: unsupported operand type(s) for -: 'bool' and 'str'
print(True-10)      # prints: -9, int
print(True-10.0)    # prints: -9.0, float
print(False-True)   # prints: -1, int

#------------------------------------------------

print("-> * <-:")

print("str with str, int, float, bool")
# print("0"*"1")    # TypeError: can't multiply sequence by non-int of type 'str'
print("0"*1)        # prints: 0, str
# print("0"*1.0)    # TypeError: can't multiply sequence by non-int of type 'float'
print("0"*True)     # prints: 0, str

print("int with str, int, float, bool")
print(10*"1")       # prints: 1111111111, str
print(10*10)        # prints: 100, int
print(10*10.0)      # prints: 100.0, float
print(10*True)      # prints: 10, int

print("float with str, int, float, bool")
# print(10.0*"10.0")# TypeError: can't multiply sequence by non-int of type 'float'
print(10.0*10)      # prints: 100.0, float
print(10.0*10.0)    # prints: 100.0, float
print(10.0*True)    # prints: 10.0, float

print("bool with str, int, float, bool")
print(True*"10.0")  # prints: 10.0, str
print(True*10)      # prints: 10, int
print(True*10.0)    # prints: 10.0, float
print(False*True)   # prints: 0, int

#------------------------------------------------

print("-> / <-:")

print("str with str, int, float, bool")
# print("0"/"1")    # TypeError: unsupported operand type(s) for /: 'str' and 'str'
# print("0"/1)      # TypeError: unsupported operand type(s) for /: 'str' and 'int'
# print("0"/1.0)    # TypeError: unsupported operand type(s) for /: 'str' and 'float'
# print("0"/True)   # TypeError: unsupported operand type(s) for /: 'str' and 'bool'

print("int with str, int, float, bool")
# print(10/"1")     # TypeError: unsupported operand type(s) for /: 'int' and 'str'
print(10/10)        # prints: 1.0, float
print(10/10.0)      # prints: 1.0, float
print(10/True)      # prints: 10.0, float

print("float with str, int, float, bool")
# print(10.0/"10.0")# TypeError: unsupported operand type(s) for /: 'float' and 'str'
print(10.0/10)      # prints: 1.0, float
print(10.0/10.0)    # prints: 1.0, float
print(10.0/True)    # prints: 10.0, float

print("bool with str, int, float, bool")
# print(True/"10.0")# TypeError: unsupported operand type(s) for /: 'bool' and 'str'
print(True/10)      # prints: 0.1, float
print(True/10.0)    # prints: 0.1, float
print(False/True)   # prints: 0.0, float