# import sys
# input = sys.stdin.readline

# N = int(input())

# def cal(x,y):
#     global arr,data
#     cur = {x:[],y:[]}
#     for i in range(N):
#         for j in range(i+1):
#             if i != j:
#                 if i not in cur and j not in cur:
#                     print(x,y,i,j,arr[x][y],arr[y][x],arr[i][j],arr[j][i], data)
#                     data = min(data, abs((arr[x][y]+arr[y][x])-(arr[i][j]+arr[j][i])))



# arr = [list(map(int,input().split())) for _ in range(N)]
# data = 10e9
# for i in range(N):
#     for j in range(i+1):
#         if i != j:
#             cal(i,j)

# print(data)

import sys
input = sys.stdin.readline

def dfs(depth, idx):
    global n, ans
    if depth == n//2:
        t1, t2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] == 0 and visit[j] == 0:
                    t1 += arr[i][j]
                elif visit[i] == 1 and visit[j] == 1:
                    t2 += arr[i][j]

        ans = min(ans, abs(t1-t2))
        return

    for i in range(idx, n):
        if not visit[i]:
            visit[i] = 1
            dfs(depth+1, i+1)
            visit[i] = 0

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
visit = [0] * n
ans = 1e10
dfs(0, 0)
print(ans)
