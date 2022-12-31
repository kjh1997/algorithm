import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

cost = [[10e9] * N for i in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1],c)

for i in range(N):
    cost[i][i]=0
    for j in range(N):
        for k in range(N):
            cost[j][k]= min(cost[j][k], cost[j][i] + cost[i][k])

for i in cost:
    for j in range(N):
        if i[j] == 10e9:
            i[j]=0
        print(i[j], end=" ")
    print()


