#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    catADistance = 0
    catBDistance = 0
    if z > x:
        catADistance = z - x
    else:
        catADistance = x - z

    if z > y:
        catBDistance = z - y
    else:
        catBDistance = y - z

    if catBDistance == catADistance:
        return "Mouse C"
    elif catBDistance > catADistance:
        return "Cat A"
    else:
        return "Cat B"


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result)


