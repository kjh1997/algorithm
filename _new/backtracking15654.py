n,m = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
arr = []

def dfs(s):
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return
    for i in data:
        if i in arr: continue
        arr.append(i)
        dfs(i)
        arr.pop()
dfs(1)