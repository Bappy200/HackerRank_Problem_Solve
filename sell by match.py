#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    itemCountDir = {}
    for i in ar:
        if not itemCountDir.get(i):
            conuntNumber = ar.count(i) // 2
            itemCountDir[i] = conuntNumber

    return sum(list(itemCountDir.values()))


if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
