import sys

input = sys.stdin.readline
N,M = map(int,input().split())
arr = [[0]+ [0]*(N)]
for i in range(N):
    arr.append([0] + list(map(int,input().split())))

for i in range(1, N+1):
    for j in range(1, N):
        arr[i][j+1] += arr[i][j]

for j in range(1, N+1):
    for i in range(1, N):
        arr[i+1][j] += arr[i][j]

for i in range(M):
    x1,y1,x2,y2 = map(int,input().strip().split())
    print(arr[x2][y2]+ arr[x1-1][y1-1] - arr[x2][y1-1] - arr[x1-1][y2])