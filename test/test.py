
from collections import deque

def find_v(data):
    global num, cnt, idx
    q=data
    while True:
        if q[0] == max(q): 
            cnt +=1
            if idx[0] == m: 
                break
            else:
                idx.pop(0)
                q.pop(0)
        else: 
            idx.append(idx.pop(0))
            q.append(q.pop(0))

for i in range(int(input())):
    n,m = map(int,input().split())
    board = list(map(int, input().split()))
    idx=[i for i in range(n)]
    
    cnt,num=0,board[m]
    find_v(board)
    print(cnt)
