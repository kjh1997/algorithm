n = int(input())
scv = list(map(int, input().split()))
dp = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
while len(scv) < 3:
    scv.append(0)

def dfs(x, y, z):
    if x == 0 and y == 0 and z == 0:
        return 0
    if dp[x][y][z]:
        return dp[x][y][z]
    dp[x][y][z] = 1 + min(dfs(max(x-9, 0), max(y-3, 0), max(z-1, 0)), dfs(max(x-9, 0), max(y-1, 0), max(z-3, 0)), dfs(max(x-3, 0), max(y-9, 0), max(z-1, 0)),
                          dfs(max(x-3, 0), max(y-1, 0), max(z-9, 0)), dfs(max(x-1, 0), max(y-3, 0), max(z-9, 0)), dfs(max(x-1, 0), max(y-9, 0), max(z-3, 0)))
    return dp[x][y][z]

print(dfs(scv[0], scv[1], scv[2]))
# from collections import deque
# n = int(input())
# arr=[0 for i in range(3)]
# temp = list(map(int,input().split()))
# for i in range(n): arr[i] =temp[i]
# q=deque()
# q.append(([arr[0],arr[1],arr[2]],0))
# visit = []
# if n ==1: print(max(arr)//9+1 if max(arr)%9 !=0 else max(arr))
# else:
#     while q:
#         board = q.popleft()
#         if board in visit: continue
#         visit.append(board)
#         if max(board[0]) <=0:
#             print(board[1])  
#             break
#         for j in range(3):
#             if temp[j] <=0: continue
#             temp=board[0].copy()
#             temp[j] -= 9
#             temp[j-1] -= 3
#             temp[j-2] -= 1
#             q.append((temp,board[1]+1))
            
#             temp=board[0].copy()
#             temp[j] -= 9
#             temp[j-2] -= 3
#             temp[j-1] -= 1
#             q.append((temp,board[1]+1))
