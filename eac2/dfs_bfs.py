from collections import deque

def dfs(graph, s):
    q = deque()
    q.append(s)
    cnt = 1
    visit = []
    while q:
        n = q.popleft()
        if n not in visit:
            cnt +=1
            q.extend(graph[n])
            visit.append(n)
        else: cnt_list.append(cnt)
    return cnt
T= int(input())
for test in range(1,1+T):
    cnt_list = []
    m,n = map(int,input().split())
    node =[]
    for i in range(n):
        node.append((input().split(" ")))
    graph = {}
    for i in node:
        if i[0] not in graph: graph[i[0]] = [i[1]]
        if i[1] not in graph:  graph[i[1]] = [i[0]]
        if i[1] not in graph[i[0]]: graph[i[0]].append(i[1])
        if i[0] not in graph[i[1]]: graph[i[1]].append(i[0])
    lengths = []
    for i in graph:
        lengths.append(dfs(graph, i)-1)
    print(cnt_list)
    if len(lengths) == 0: print(f'#{test} {1}')
    else: print(f"#{test} {min(cnt_list)}")

