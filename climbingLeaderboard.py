#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def get_rank(ranked, player):
    ranked_number = 1

    for i in range(len(ranked)-1):
        if ranked[i] == player:
            return ranked_number

        if ranked[i] != ranked[i+1]:
            ranked_number += 1

    return ranked_number


def climbingLeaderboar(ranked, player):
    # Write your code here
    player_rank = []
    for i in player:
        ranked.append(i)
        for j in range(len(ranked)-2, -1, -1):

            if ranked[j] > i:
                ranked[j+1] = i
                print("in if = ", i, j, ranked)
                break
            else:
                print("in else = ", i, j, ranked)
                ranked[j + 1], ranked[j] = ranked[j], ranked[j + 1]
        print("rank ", ranked)
        player_rank.append(get_rank(ranked, i))
        print(player_rank)

    print(ranked, player_rank)
    return player_rank


if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboar(ranked, player)
    print(result)