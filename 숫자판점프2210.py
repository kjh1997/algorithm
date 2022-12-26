import sys
from collections import deque
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, root):
    if len(root) == 6: 
        result.add(root)
        return   
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k] 
        if 0 <= ddx < 5 and 0 <= ddy < 5:
            dfs(ddx, ddy, root + arr[ddx][ddy])

arr = [list(map(str, input().strip().split())) for i in range(5)]

result = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, arr[i][j])
print(len(result))