# a = "a"
# res = ''.join(format(ord(i), '08b') for i in a)
# o = ord(a)
# print(bin(o))

# primero = "A"
# segundo = "B"

# print((ord("z")-ord("x")))

# board = []
# board1 = []
# for i in range(2):
#     for j in range(3):
#         board.append([0])
#     board.append([])

# print(board)

# board = [[i for i in range(3)] for j in range(2)]

# print(board)

# data = [4, 2, 3, 2, 1]
# res = data[0]
# for d in data:
#     if d < res:
#         res = d
# print(res)
# x = 1
# while x < 10:
#     print('*')
#     x = x << 1

# nums = [1, 2, 3]
# data = ('Peter',) * (len(nums) - nums[::-1][0])
# print(data)

# my_list = [0, 1, 2, 3]
# x = 1
# for elem in my_list:
#     x *= elem
# print(x)

# w = [7, 3, 23, 42]
# x = w[1:]
# y = w[1:]
# z = w
# y[0] = 10
# z[1] = 20
# print(w)

# nums = []
# vals = nums
# vals.append(1)

# my_list = [3,1,-2]
# print(my_list[my_list[-1]])

# vals = [0,1,2]
# vals.insert(0,1)

# del vals[1]

# print(vals)

# my_list = []
# for i in range(-1,2):
#     my_list.append(i)

# print(my_list)

# var = 10
# for i in range(10):
#     for j in range (2,10,1):
#         if var%2 == 0:
#             continue
#         var += 1
#     var += 1
# else:
#     var += 1

# print(var)

# a = [1,2,3,4,5]
# for v in range(len(a)):
#     a.insert(1,a[v])
# print(a)

# for i in "Jhon":
#     if i =="o":
#         pass
#     print(i,end=", ")

# x = 0

# for i in range(10):
#     for j in range(-1,-10,-1):
#         x+=1
# print(x)

# nums = [1,2,3]
# vals = nums[-1:-2]

# print(False + True + True)

# x = '\''
# print(len(x))

# a = [1,2,3,4,5,6,7,8,9]
# print(a[::2])

t = [[3-i for i in range(3)] for j in range(3)]

s = 0

for i in range (3):
    s += t[i][i]

print(s)