import sys
input = sys.stdin.readline
data = []
for i in range(int(input())):    data.append(list(map(str,input().split())))
data = sorted(data, key = lambda x: (int(x[0])))
for i in data:    print(*i)