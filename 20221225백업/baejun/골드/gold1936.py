from collections import deque
import math
def bfs(start, end):
    q = deque()
    q.append([start,0])
    v = [0 for i in range(10000)]
    v[start] = 1
    while q:
        now,cnt = q.popleft()
        strNow=str(now)
        if now == end: return cnt
        for i in range(4):
            for j in range(10):
                temp = int(strNow[:i] + str(j)+strNow[i+1:])
                if v[temp]==0 and prime_board[temp] and temp >= 1000:
                    v[temp]=1
                    q.append([temp,cnt+1])
    return None

prime_board=[True]*10000
def prime_cal():
    for i in range(2,100+1):
        if prime_board[i]==True:
            for j in range(i*2, 10000,i):
                prime_board[j]=False
prime_cal()


arr = []
for i in range(int(input())):
    s,e = map(int,input().split())
    r = bfs(s,e)
    print(r if r != None else "Impossible")





