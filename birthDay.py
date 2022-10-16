#!/bin/python3

import math
import os
import random
import re



#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
def sumList(s, i, m):
    print("print i+m", i + m)
    im = i + m
    total = sum(s[i: im])

    print(total)
    print("print i+m", im)

    # condition = i + m
    # print("condition sumlist ",s[i], i,  s[condition], condition)
    # for j in range(i, condition):
    #     sum += s[j]
    #
    # print("sum ", sum)
    return total


def birthday(s, d, m):
    # Write your code here
    countMatch = 0

    print(len(s), m)
    conditionNumber = len(s) - m
    if len(s) == m:
        conditionNumber = 1


    print("m", m)
    print("CCC ",conditionNumber)
    for i in range(conditionNumber+1):
        print("i  ", i)
        sum = sumList(s, i, m)

        if sum == d:
            countMatch += 1
            print("countMatch ", countMatch)
    return countMatch


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    print("result", result)
