# import sys

# n,m = map(int,sys.stdin.readline().split())

# x = list(map(int,sys.stdin.readline().split()))
# y = list(map(int,sys.stdin.readline().split()))
# a,b=0,0
# result = []
# while a != n or b != m:
#     if a==n: 
#         result.append(y[b])
#         b +=1
#     elif b == m:
#         result.append(x[a])
#         a +=1
    
#     elif x[a] < y[b]:
#         result.append(x[a])
#         a +=1
#     elif x[a] > y[b]:
#         result.append(y[b])
#         b +=1
# print(*result)

import sys


n,m = map(int,sys.stdin.readline().split())

x = list(map(int,sys.stdin.readline().split()))
y = list(map(int,sys.stdin.readline().split()))
x.extend(y)
x.sort()
print(*x)