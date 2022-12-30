import sys
input = sys.stdin.readline
data = []
for i in range(int(input())):    data.append(list(map(int,input().split())))
data = sorted(data, key = lambda x: (x[0],x[1]))
for i in data:    print(*i)