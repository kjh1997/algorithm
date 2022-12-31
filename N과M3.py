import sys
input = sys.stdin.readline

N,M= map(int,input().split())

def bt(arr):
    if len(arr)==M: print(*arr); return
    for i in range(1,N+1):
        arr.append(i)
        bt(arr)
        arr.pop()

bt([])




