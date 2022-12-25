def dfs(node, depth):
    result.append(depth)
    for j in data[node]:
        if not visited[j]:
            visited[j] = 1
            print(visited)
            dfs(j, depth + 1)
            visited[j] = 0
T = int(input())
for tc in range(1, T+1):
    global result
    result = []
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for i in range(M)]
    data = [[] for i in range(N)]
    if N > 1:
        for i in range(len(graph)):
            data[graph[i][0]-1].append(graph[i][1]-1)
            data[graph[i][1]-1].append(graph[i][0]-1)
        visited = [0] * N
        for node in range(len(data)):
            visited[node] = 1
            dfs(node, 1)
            visited[node] = 0
        print('#{} {}'.format(tc, max(result)))
    else:
        result = 1; print('#{} {}'.format(tc, result))
    