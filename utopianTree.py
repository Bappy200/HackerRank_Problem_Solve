#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    height = 1
    is_spring = True

    if n == 0:
        return height

    for i in range(n):
        if is_spring:
            height *= 2
            is_spring = False
        else:
            height += 1
            is_spring = True

    return height


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        print(result)


