import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    queue = sorted(set(scores), reverse = True)
    idx = len(queue) - 1
    answer = []
    
    for alice_score in alice:
        while queue[idx] <= alice_score and idx >= 0:
            print(idx)
            idx -= 1

        if idx < 0 :
            answer.append(1)
            continue
        answer.append(idx + 2)
        
    return answer
    


if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)
    print(result)