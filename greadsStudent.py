#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    gradesResult = []
    for i in grades:
        if i < 38:
            gradesResult.append(i)
        else:
            numberModule = i % 5
            if numberModule == 0:
                gradesResult.append(i)
            elif numberModule > 2:
                if numberModule == 3:
                    gradesResult.append(i + 2)
                else:
                    gradesResult.append(i + 1)
            else:
                gradesResult.append(i)
    return gradesResult


if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
