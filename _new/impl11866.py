from collections import deque
re=[]
q= deque()
a,b= map(int,input().split())
for i in range(1,a+1):
    q.append(i)

while q:
    cnt = 0
    for i in range(b):
        a = q.popleft()
        if i ==b-1:
            re.append(a)
        else:
            q.append(a)
print("<",end="")
for i in re[:-1]: 
    print(i,end=", ")
print(re[-1],end="")
print(">", end="")
