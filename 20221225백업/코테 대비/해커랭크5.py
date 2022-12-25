#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    count = Counter(arr)
    count = sorted(count.items(),key=lambda x : (x[1],x[0]), reverse=True)
    a = count[0][1]
    for i in range(len(count)):
        if a != count[i][1]:return count[i-1][0]

if __name__ == '__main__':
   

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
