import sys
input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))

ans = [[] for i in range(N+1)]
def tree(arr, depth):
    mid = len(arr)//2
    ans[depth].append(arr[mid])
    if len(arr)==1: return
    tree(arr[:mid],depth+1)
    tree(arr[mid+1:],depth+1)

tree(data,1)
for i in range(1,N+1):
    print(*ans[i])