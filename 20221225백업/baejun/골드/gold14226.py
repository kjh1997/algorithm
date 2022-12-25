from collections import deque
s = int(input())
board = [[0]*(1001) for _ in range(1001)]
def bfs():
    board[1][0] = 0
    q = deque([(1, 0)])
    while q:
        sc, clip = q.popleft()
        if sc == s:
            print(board[s][clip])
            break
        if board[sc][sc] == 0:
            board[sc][sc] = board[sc][clip]+1
            q.append((sc, sc))
        if 2 <= sc+clip <= 1000 and board[sc+clip][clip] == 0:
            board[sc+clip][clip] = board[sc][clip]+1
            q.append((sc+clip, clip))
        if 2 <= sc-1 <= 1000 and board[sc-1][clip] == 0:
            board[sc-1][clip] = board[sc][clip]+1
            q.append((sc-1, clip))
bfs()