from collections import deque
n,m = map(int,input().split())
graph ={}
for i in range(1, n+1):
    graph[i]=[]

for _ in range(m):
    a,b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
arr= [0 for i in range(n+1)]
re = 9999999999
for peo in graph:
    visit=[False for _ in range(n+1)]
    result = 0
    for p2 in graph:
        if p2 == peo: continue
        q = deque()
        q.append(([peo],0))
        while q:
            data, cnt= q.popleft()
            if p2 in data:
                result += cnt
                break
            for i in data:
                if visit[i] == False:
                    visit[i] == True
                    q.append((graph[i], cnt+1))
    arr[peo]=result
print(arr.index(min(arr[1:])))
