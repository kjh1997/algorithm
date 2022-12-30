import sys
input = sys.stdin.readline
dic = {}
N = int(input())
arr = list(map(int,input().split()))
arrset = sorted(list(set(arr)))
for i in range(len(arrset)):
    dic[arrset[i]] = i
for i in range(len(arr)):
    arr[i] = dic[arr[i]] 
print(*arr)