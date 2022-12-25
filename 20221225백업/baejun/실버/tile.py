import sys
sys.setrecursionlimit(10000)
n = int(input())
a = [0]*1001
def facto(n):
    if n==1: return 1
    elif n==2: return 2
    elif a[n] !=0: return a[n]
    else:
        a[n]=(facto(n-1)+facto(n-2)) % 10007
        return a[n]
print(facto(n))