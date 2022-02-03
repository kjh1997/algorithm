from collections import deque 
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1] 
def bfs(maze, tc): 
    q = deque()
    q.append((1,1)) 
    cnt = 0
    while q: 
        x, y = q.popleft() 
        for i in range(len(dy)): 
            mx, my = x + dx[i], y + dy[i] 
            if mx < 0 or my < 0 or mx >= 100 or my >= 100: continue 
            if maze[mx][my] == 1: continue 
            if maze[mx][my] == 0: 
                maze[x][y] += 100
                q.append((mx, my)) 
            if maze[mx][my] ==3:
                print(f'#{tc} 1')
                cnt =1
                break
        if cnt == 1: break
        
    if cnt == 0: print(f'#{tc} 0')
    return

for tc in range(1,11):
    start = input()
    maze = [list(map(int,input())) for i in range(100)] 
    bfs(maze, tc)