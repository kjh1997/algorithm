import sys
from collections import deque


dx = [1,1,1,0,0,-1,-1,-1]
dy=[1,0,-1,-1,1,1,0,-1]

while True:
    w, h = map(int, sys.stdin.readline().split())
    if (w, h) == (0, 0):
        break

    m = []
    for _ in range(h):
        m.append(list(map(int, sys.stdin.readline().split())))
    
    visited = [[False for _ in range(w)] for _ in range(h)]
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1 and not visited[i][j]:
                q = deque([(i, j)])
                cnt += 1

                while q:
                    x, y = q.popleft()
                    visited[x][y] = True

                    for k in range(8):
                        if x+dx[k] < 0 or x+dx[k] >= h or y+dy[k] < 0 or y+dy[k] >= w:
                            continue
                        if m[x+dx[k]][y+dy[k]] == 1 and not visited[x+dx[k]][y+dy[k]]:
                            q.append((x+dx[k], y+dy[k]))
                            visited[x+dx[k]][y+dy[k]] = True
    print(cnt)