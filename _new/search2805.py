n,l = map(int,input().split())
arr = list(map(int,input().split()))
s = 0
e = max(arr)
while True:
    mid = (s+e)//2
    rest = 0
    for i in arr:
        if i - mid > 0:
            rest += (i-mid)

    if rest == l or s>e:
        print(mid); exit()
    elif rest > l:
        s = mid +1
    elif rest < l: 
        e = mid-1


