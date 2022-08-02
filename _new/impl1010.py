# from itertools import combinations
from math import factorial
n = int(input())
def combination(n,r):
    return factorial(n)/(factorial(n-r)*factorial(r))

for _ in range(n):
    x,y=map(int,input().split())
    print(int(combination(y,x)))
