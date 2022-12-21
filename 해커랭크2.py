
import math
import os
import random
import re
import sys


n = int(input().strip())

arr = []

def diagonalDifference(arr):
    a,b=0,0
    for i in range(len(arr)):
        a += arr[i][i]
        b += arr[i][-(i+1)]
        print(a,b)
    
    return abs(a-b)





for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
result = diagonalDifference(arr)
print(result)