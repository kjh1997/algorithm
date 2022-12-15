def dfs(cur, cnt):
    visit[cur] = 1
    for n in x[cur]:
        if visit[n] == 0:
            cnt =dfs(n, cnt + 1)
    return cnt

for _ in range(int(input())):
    N, M = map(int, input().split())
    x = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().split())
        x[u].append(v)
        x[v].append(u)
    visit = [0]*(N+1)
    visit[1] = 0
    cnt = dfs(1, 0)
    print(cnt)