#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):
    # Write your code here
    if p < n // 2:
        result = p // 2 
        return result
    elif p == n // 2:
        result = p // 2 
        return result
    elif n == p+1 and n % 2 == 0:
        return 1
    else:
        numberOfPage = n - p
        result = numberOfPage // 2
        return result


if __name__ == '__main__':
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
