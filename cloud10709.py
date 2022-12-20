from sys import stdin
n,m = map(int,stdin.readline().split())
data = [[0]*m for i in range(n)]

for _ in range(n):
    cur = list(stdin.readline())
    c = -1
    for i in range(m):
        if cur[i] != "c": 
            if c != -1: c+=1
            data[_][i] = c
            
        else: 
            c = 0
            data[_][i] = c
    print(*data[_])
