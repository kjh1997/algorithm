from collections import deque
n, h = map(int,input().split())
visit=[False for i in range(n+1)]
v= [0 for i in range(n+1)]
graph={}
for i in range(1,n+1):
    graph[i]=[]
for i in range(h):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
q = deque()
q.append(1)
visit[1]=1
while q:
    cnt = 1
    k = q.popleft()
    move = graph[k]
    print(move)
    
    for m in move:
        if visit[m] == False:
            q.append(m)
            visit[m] = cnt
    cnt +=1
print(visit)    

