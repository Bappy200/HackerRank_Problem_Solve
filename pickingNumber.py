#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    longestLen = 0
    startNumberIndex = 0
    i = 0
    aLength = len(a)
    while i < aLength:
        if abs(a[startNumberIndex] - a[i]) <= 1:
            i += 1
            continue
        else:
            index = i
            deff = index - startNumberIndex - 1
            startNumberIndex = i
            if deff > longestLen:
                longestLen = deff
        i += 1
    if longestLen == 0:
        return aLength
    return longestLen


if __name__ == '__main__':


    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)



    print(result)
