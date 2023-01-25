import sys
input = sys.stdin.readline
n,m=map(int,input().split())
data = list(map(int,input().split()))
data.sort()
def dfs(depth):
    if depth == m: print(*arr); return
    
    for i in data:
        arr.append(i)
        dfs(depth+1)
        arr.pop()

for i in data:
    arr= [i]
    dfs(1)




