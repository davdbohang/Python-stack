# 1. Countdown- 
# x = int(input("Please enter your number: "))
# for countdown in range(x, 0, -1):
#     print(countdown)

# 2. Print and Return-
# def print_and_return(a,b):
#     print(a)
#     return b
# print_and_return(1,2)

# 3. First plus Length
# x=[1,2,3,4,5,6,7,8]
# def first_plus_length(x):
#     sum = int(x[0]) + int(x[len(x)-1])
#     print(sum)
# first_plus_length(x)

# 4. Values Greater than Second
x = [1,2,5,3,4,2,6]
def values_greater_than_second(x):
    y = []
    for i in range(0, len(x), 1):
        if x[i] > x[1]:
            y.append(int(x[i]))
        else:
            continue
    print(len(y))
    print(y)    
values_greater_than_second(x)

# 5. This Length, that Value
# def length_and_value(size,value):
#     y = []
#     for i in range(0, size, 1):
#         y.append(int(value))
#     print(y)
# length_and_value(6,2)


