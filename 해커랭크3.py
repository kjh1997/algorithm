#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    N=len(arr)
    positive_count=0
    negative_count=0
    zero_count=0

    for number in arr:
        if(number>0):
            positive_count+=1
        elif(number==0):
            zero_count+=1
        elif(number<0):
            negative_count+=1

    print("{0:.6f}".format(positive_count/N))
    print("{0:.6f}".format(negative_count/N))
    print("{0:.6f}".format(zero_count/N))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
