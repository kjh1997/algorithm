from collections import deque
n=int(input())
board = []
for i in range(n):
    board.append(list(map(int,input().split())))
cnt =0
def bfs():
    global cnt
    q = deque()
    q.append((0,1,1)) # 마지막 인자값은 가로 세로 대각선을 나타냄. 각 1,0,-1 

    while q:
        a=q.pop()
        if a[0] == n-1 and a[1] == n-1: 
            cnt +=1
        else:
            if a[1] +1 <n and a[0]+1 <n and\
                board[a[0]][a[1]+1] != 1 and \
                board[a[0]+1][a[1]] != 1 and\
                board[a[0]+1][a[1]+1] != 1:
                q.append((a[0]+1,a[1]+1,0))

            if a[2] != -1:
                if a[1] +1 <n and board[a[0]][a[1]+1] != 1:
                    q.append((a[0],a[1]+1,1))

            if a[2] != 1: # 세로
                if a[0] +1 <n and board[a[0]+1][a[1]] != 1:
                    q.append((a[0]+1,a[1],-1))
bfs()
print(cnt)