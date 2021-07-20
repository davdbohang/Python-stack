# 1. Biggie Size
# x = [-1,1,-2,2,-3,3,-4,4]
# def biggie_size(x):
#     for i in range(0, len(x), 1):
#         if x[i] > 0:
#             x[i] = "big"
#     print(x)
# biggie_size(x)

# 2. Count Positives
# x = [1,2,-3,4,-5]
# def count_positives(x):
#     total = 0
#     for i in range (0,len(x),1):
#         if x[i] > 0:
#             total += 1
#     x[len(x)-1] = total
# count_positives(x)
# print(x)

# 3. Sum total
# x = [1,2,3,4,5,6,-4]
# def sum_total(x):
#     sum = 0
#     for i in range (0, len(x), 1):
#         sum += x[i]
#     return sum
# print(sum_total(x))

# 4. Average
# x = [1,2,3,4,5]
# def average(x):
#     sum = 0
#     for i in range (0, len(x), 1):
#         sum += x[i]
#     return sum/ len(x)
# print(average(x))

# 5. Length
# x = [1,1,1,1,2,2,2,22,3,3,]
# # print(len(x))
# def length(x):
#     total = 0
#     for i in range (0, len(x), 1):
#         total += 1
#     return total
# print(length(x))

# 6. Minimum
# x = [5,2,3,-7,8]
# def minimum(x):
#     if len(x) < 1:
#         return False
#     min = x[0]
#     for i in range (0, len(x), 1):
#         if x[i] < min:
#             min = x[i]
#     return min
# print(minimum(x))

# 7. Maximum
# x = [4,1,2,4,5,6,12,0]
# def maximum(x):
#     if len(x) < 1:
#         return False
#     max = x[0]
#     for i in range (0, len(x), 1):
#         if x[i] > max:
#             max = x[i]
#     return max
# print(maximum(x))

# 8. Ultimate Analysis
x = [3,4,5,6,67,7,9]

def sum_total(x):
    sum = 0
    for i in range (0, len(x), 1):
        sum += x[i]
    return sum
print(sum_total(x))

def average(x):
    sum = 0
    for i in range (0, len(x), 1):
        sum += x[i]
    return sum/ len(x)
print(average(x))

def minimum(x):
    if len(x) < 1:
        return False
    min = x[0]
    for i in range (0, len(x), 1):
        if x[i] < min:
            min = x[i]
    return min
print(minimum(x))

def maximum(x):
    if len(x) < 1:
        return False
    max = x[0]
    for i in range (0, len(x), 1):
        if x[i] > max:
            max = x[i]
    return max
print(maximum(x))

def ultimate(x=''):
    sumtotal = sum_total(x)
    avg = average(x)
    low = minimum(x)
    high = maximum(x)
    listall = ("Sum is "+ str(sumtotal), "Average is "+ str(avg), "Min is "+ str(low), "Max is "+ str(high))
    return listall
print(ultimate(x))

# 9. Reverse List
# x = [1,2,3,4,5,6,7,8,9,1,5]
# def reverse(x):
#     for i in range (0, len(x)/2, 1):
#         temp = x[i]
#         x[i] = x[len(x)-1-i]
#         x[len(x)-1-i] = temp
#     return x
# print(reverse(x))