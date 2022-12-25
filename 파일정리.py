import sys

input = sys.stdin.readline
data = []
data = {}
for i in range(int(input())):

    d = input().strip().split(".")[1]
    if d not in data: data[d]=1
    else: data[d]+=1

data = sorted(data.items())
for i,j in data:
    print(i,j)

