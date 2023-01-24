import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = sorted(list(map(int,input().split())))

visit = [0]*(n+1)
path ={}
def dfs(arr,depth):
    if len(arr)==m: 
        if str(arr) not in path:
            path[str(arr)]=0
            print(*arr) 
            return
    
    for i in range(depth,len(data)):
        if visit[i] == 0:
            visit[i] = 1
            dfs(arr+[data[i]],i+1)
            visit[i] = 0
for i in range(len(data)-m+1):
    visit[i] = 1
    dfs([data[i]], i)
    visit[i] = 0



