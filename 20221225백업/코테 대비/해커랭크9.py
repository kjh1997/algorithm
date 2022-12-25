#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
from itertools import permutations
def nonDivisibleSubset(k, s):
    data = permutations(s)
    res = set()
    for i in data:
        if (i[0]+i[1]) % k == 0:
            res.add(i[0])
            res.add(i[1])
    print(res)
    
    return len(s)
    

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)
