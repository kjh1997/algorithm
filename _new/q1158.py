from collections import deque
import sys

n,k  = map(int,input().split())

q = deque()
for i in range(1,n+1):
    q.append(i)
answer = []
while q:
    for i in range(k-1):
        tmp = q.popleft()
        q.append(tmp)
    tmp = q.popleft()
    answer.append(str(tmp))

print("<"+ ", ".join(answer) + ">")
