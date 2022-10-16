# def     timeConversion(s):
#     hour = int(s[0:2])
#     minuteSecond = s[2:8]
#     amPm = s[8:11]
#
#     if amPm == "AM":
#         convertHour = hour
#         if convertHour == 12:
#             convertHour = 0
#
#         if convertHour < 10:
#             convertHour = "0" + "{}".format(convertHour)
#         return convertHour + minuteSecond
#     else:
#         convertHour = 12 + hour
#         if convertHour == 24:
#             convertHour //= 2
#
#         return "{}".format(convertHour) + minuteSecond
#
#         print(timeConversion("04:59:59AM"))
#
#
#
#     # print( "8"+ "{}".format(34))
#
#


# !/bin/python3


import os
import random
import re


#      GFTRauD;Os\'posW[UGC
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
#
# def kangaroo(x1, v1, x2, v2):
#     bigKangarooDistance = 0
#     smallKangarooDistance = 0
#     distanceBetweenBigSmall = 0
#     smallJump = 0
#     bigJump = 0
#
#     kangarooX1 = x1 + v1
#     kangarooX2 = x2 + v2
#
#     if kangarooX1 == kangarooX2:
#         return "YES"
#
#     if kangarooX1 > kangarooX2:
#         bigKangarooDistance = kangarooX1
#         smallKangarooDistance = kangarooX2
#         distanceBetweenBigSmall = bigKangarooDistance - smallKangarooDistance
#         smallJump = v2
#         bigJump = v1
#     else:
#         bigKangarooDistance = kangarooX2
#         smallKangarooDistance = kangarooX1
#         distanceBetweenBigSmall = bigKangarooDistance - smallKangarooDistance
#         smallJump = v1
#         bigJump = v2
#
#     while bigKangarooDistance > smallKangarooDistance:
#         bigKangarooDistance += bigJump
#         smallKangarooDistance += smallJump
#         tempDistanceBetweenBigSmall = bigKangarooDistance - smallKangarooDistance
#
#
#         if tempDistanceBetweenBigSmall > distanceBetweenBigSmall:
#             return "NO"
#         elif tempDistanceBetweenBigSmall == distanceBetweenBigSmall
#         elif bigKangarooDistance == smallKangarooDistance:
#             print("YES")
#             return "YES"
#         else:
#             distanceBetweenBigSmall = tempDistanceBetweenBigSmall
#     else:
#         print(bigKangarooDistance, smallKangarooDistance)
#         return "NO"
#
#
# if __name__ == '__main__':
#
#     first_multiple_input = input().rstrip().split()
#
#     x1 = int(first_multiple_input[0])
#
#     v1 = int(first_multiple_input[1])
#
#     x2 = int(first_multiple_input[2])
#
#     v2 = int(first_multiple_input[3])
#
#     result = kangaroo(x1, v1, x2, v2)
#
#     print(result)

a = "2 5 1 3 4 4 3 5 1 1 2 1 4 1 3 3 4 2 1".split(" ")
a = [int(i) for i in a]
print(a[12: 19])
