# #1 
# def a():
#     return 5
# print(a())

# # prediction: 5
# # output: 5 correct

# #2
# def a():
#     return 5
# print(a()+a())
# # prediction: 10
# # output: 10 correct

#3
# def a():
#     return 5
#     return 10
# print(a())
# # prediction: 
# 5
# 10
# # output:
# 5 incorrect: did not return 10

#4
# def a():
#     return 5
#     print(10)
# print(a())
# # prediction: 5
# # output: 5 correct

#5
# def a():
#     print(5)
# x = a()
# print(x)
# # prediction: 5
# # output: incorrect
# # 5
# # none

#6
# def a(b,c):
#     print(b+c)
# # print(a(1,2) + a(2,3))
# # prediction: 8
# # output: 'TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType''

#7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))
# # prediction: 25
# # output: 25 correct

#8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())
# # prediction: 100
# # output: incorrect
# # 10
# # 100

#9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))
# # prediction:
# # 7
# # 14
# # 21
# # output: correct

#10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))
# # prediction: 8
# # output: correct

#11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

#prediction:
# 500
# 500
# 300
# 500
# output: correct

#12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)
# # 500
# # 500
# # 300
# # 500
# # output: correct

#13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)
# # 500
# # 500
# # 300
# # 300
# # output: correct

#14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()
# # 1
# # 3
# # 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# 1
# 3
# 5
# 10
# 1
# 3
# 5
# 10
# output: incorrect- only printed out 1 sequence