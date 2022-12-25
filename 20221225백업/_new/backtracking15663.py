from itertools import combinations_with_replacement
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
data = list(combinations_with_replacement(arr, m))

data = list(set(data))
data.sort()
for i in data: 
    print(' '.join(map(str,(i))) )