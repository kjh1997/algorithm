from collections import deque
a,b=map(int,input().split())
q=deque()
q.append((a,0))
while q:
    cur, cnt = q.popleft()
    x = int(str(cur)+str(1))
    y= cur*2
    if cur == b: print(cnt+1); exit()
    if y <= b: q.append((y,cnt +1))
    if x<=b: q.append((x,cnt +1))
print(-1)



