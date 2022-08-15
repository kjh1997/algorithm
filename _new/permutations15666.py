from itertools import permutations
n,m=map(int,input().split())
arr = list(map(int,input().split()))
data = set(permutations(arr, m))
data = sorted(data)
for i in data: print(' '.join(map(str, i)))