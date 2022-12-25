from collections import deque
import time
n,  k = map(int, input().split() )
board  = [list(map(int,input().split(" "))) for i in range(n)]
s, x_l, y_l =map(int,input().split())
data = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            data.append( { board[i][j] : [(i,j)]} )
queue = deque()
queue.extend(data)
cnt = 0
while len(queue) != 0:
    if cnt == k * s: break
    cnt += 1
    x = queue.popleft()
    x= x.popitem()
    y = x[1]
    key = x[0]
    data = []
    for j in y:
        try: 
            if board[j[0]][j[1]+1] == 0 and j[1] +1 < k : 
                board[j[0]][j[1]+1] = key 
                data.append((j[0],j[1]+1))  
        except: pass
        try: 
            if board[j[0]+1][j[1]] == 0  and j[0] +1 < k : 
                board[j[0]+1][j[1]] = key 
                data.append((j[0]+1,j[1]))
        except: pass
                                        
        try: 
            if board[j[0]-1][j[1]] == 0 and j[0] -1 >= 0: 
                board[j[0]-1][j[1]] = key 
                data.append((j[0]-1,j[1]))
        except: pass
        try: 
            if board[j[0]][j[1]-1] == 0 and j[1] -1 >= 0 : 
                board[j[0]][j[1]-1] = i 
                data.append((j[0],j[1]-1))
        except: pass
    
    if data == []: break
    queue.append({key:data})
    
print(board[x_l-1][y_l-1])