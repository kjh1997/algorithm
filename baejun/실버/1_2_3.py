import sys
sys.setrecursionlimit(10**7)
data=[0]*101
def dp(n):
    if n==1:return 1
    if n==2:return 2
    if n==3:return 4
    data[n]=dp(n-1)+dp(n-2)+dp(n-3)
    return data[n]
for _ in range(int(input())):
    print(dp(int(input())))
