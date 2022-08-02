from collections import deque
n = int(input())
map = [list(map(int,input().split())) for i in range(n)] 
copy_map =[0 for i in range(n)]
maxh=0
print(map)
for i in range(n):
    max_h=max(map[i])
    if maxh < max_h: maxh=max_h

def bfs(board, h):
    q=deque()

    



for i in range(n):
    copy_map[i]=map[i].copy()
