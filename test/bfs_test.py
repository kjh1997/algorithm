def dfs(v, cnt):
    for j in data[v]:
        print(j)
        if not visit[j]:
            visit[j] = 1
            result.append(cnt+1)
            dfs(j, cnt+1)
            visit[j]=0

T = int(input())
for test_case in range(1, T+1):
    global result
    result = []
    N,M= map(int,input().split())
    graph = [list(map(int,input().split())) for i in range(M)]
    
    data = {}
    if N>1:
        for i in graph:
            if i[0] not in data: data[i[0]] = [i[1]]
            else: data[i[0]].append(i[1])
            if i[1] not in data: data[i[1]] = [i[0]]
            else: data[i[1]].append(i[0])
        N+=1
        visit = [0] *N
        for i in data:
            visit[i] = 1
            dfs(i, 1)
            visit[i] = 0
        print(f'#{test_case} {max(result)}')
    else:
        print(f'#{test_case} {1}')
