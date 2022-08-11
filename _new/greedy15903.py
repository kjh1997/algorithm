card, n = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range(n):
    arr.sort()
    r = arr[0] + arr[1]
    arr[0],arr[1]=r,r
print(sum(arr))