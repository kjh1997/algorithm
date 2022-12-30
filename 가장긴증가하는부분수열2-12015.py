import sys
from bisect import bisect_left

N = int(input())
data = list(map(int,input().split()))
lis = []
for num in data:
    if not lis:
        lis.append(num)
        continue
    if num > lis[-1]:
        lis.append(num)
    else:
        idx = bisect_left(lis,num)
        lis[idx]=num
print(len(lis))