#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    countValidPairs = 0
    arLen = len(ar)
    for i in range(arLen):
        for j in range(i+1, arLen):
            if i < j:
                sum = ar[i] + ar[j]

                if sum % k == 0:
                    countValidPairs += 1
                    print("Sum {0}, i: {1}, j: {2}".format(sum, ar[i], ar[j]))
                    print(countValidPairs)
    return countValidPairs

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)


