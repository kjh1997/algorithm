from collections import deque

def bfs(cur):
    q = deque()
    q.append(cur)
    graph[cur] = 0
    while q:
        cur = q.popleft()
        for n in [cur-1, cur+1, cur+a, cur-a, cur+b, cur-b, cur*a, cur*b]:
            if (0 <= n <= 100000) and graph[n] == -1:
                q.append(n)
                graph[n] = graph[cur]+1
                if n == m:
                    print(graph[n]); exit()

a, b, n, m = map(int, input().split())
graph = [-1]*100001 
bfs(n)
print(graph[m])