#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    sticks.sort()
    print(sticks)
    maxidx = len(sticks)-1
    answer = list()
    while maxidx > 1:
        if sticks[maxidx -2] + sticks[maxidx + 1] > sticks[maxidx]:
            

if __name__ == '__main__':

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)
    print(result)