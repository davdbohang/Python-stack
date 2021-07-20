# # 1. Basics
# for x in range(0, 151, 1):
#     print(x)

# # 2. Multiples of 5
# for fives in range(5, 1001, 1):
#     if fives % 5:
#         continue
#     print(fives)

# 3. Counting the Dojo Way
# for cd in range(1, 101, 1):
#     if cd%5 != 0:
#         print(cd)
#         continue
#     if cd%10 == 0:
#         print("Dojo")
#         continue
#     if cd%5 == 0:
#         print("Coding")

# 4. Sum of off integers from 0 to 500k
# sumodds = 0
# for x in range(1, 500000, 1):
#     if x % 2 != 0:
#         sumodds = x + sumodds
# print(sumodds)

# 5. Counting down by 4s from 2018
# for x in range(2018, 0, -4):
#     print(x)

# 6. Flexible Counter

lowNum = int(input(" Please enter your low number: "))
highNum = int(input(" Please enter your high number: "))
mult = int(input(" Please enter your multiple: "))

for x in range(lowNum, highNum, 1):
    if x % mult == 0:
        print(x)