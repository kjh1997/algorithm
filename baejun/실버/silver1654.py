k,n = map(int,input().split())
arr = [int(input()) for i in range(k)]
s,e = 1,max(arr)
while (s<=e):
    mid = (s+e)//2
    cnt =0
    for i in range(k):
        cnt += arr[i]//mid
    if cnt >= n:
        s = mid+1
    else:
        e = mid-1
print(e)