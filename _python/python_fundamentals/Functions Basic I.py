# 1

# def a():
#     return 5
# print(a())
# the output should be 5


# 2
# def a():
#     return 5
# print(a()+a())
# the output should be 10

# 3
# def a():
#     return 5
#     return 10
# print(a())
# the output should be only 5


# 4
# def a():
#     return 5
#     print(10)
# print(a())
# the output should be only 5


# 5
# def a():
#     print(5)
# x = a()
# print(x)
# the output should be 5 and undefined because the function didn't return a value


# 6
# def a(b, c):
#     print(b+c)


# print(a(1, 2) + a(2, 3))
# the value isn't returned again so it will only print 3,5


# 7
# def a(b, c):
#     return str(b)+str(c)


# print(a(2, 5))
# the output will be 25 as a string


# 8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7


# print(a())
# the output will be 100,10


# 9
# def a(b, c):
#     if b < c:
#         return 7
#     else:
#         return 14
#     return 3


# print(a(2, 3))
# print(a(5, 3))
# print(a(2, 3) + a(5, 3))
# the output will be 7,17,21


# 10
# def a(b, c):
#     return b+c
#     return 10


# print(a(3, 5))
# the output will be 8


# 11
# b = 500
# print(b)


# def a():
#     b = 300
#     print(b)


# print(b)
# a()
# print(b)
#  the output will be 500, 500, 300, 500


# 12
# b = 500
# print(b)


# def a():
#     b = 300
#     print(b)
#     return b


# print(b)
# a()
# print(b)
# the put put will be 500, 500 , 300 ,500


# 13
# b = 500
# print(b)


# def a():
#     b = 300
#     print(b)
#     return b


# print(b)
# b = a()
# print(b)
# the output will be 500, 500, 300,300


# 14
# def a():
#     print(1)
#     b()
#     print(2)


# def b():
#     print(3)


# a()
# the out put will be 1,3,2


# 15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10


# def b():
#     print(3)
#     return 5


# y = a()
# print(y)
# the output will be1,3,5,10
