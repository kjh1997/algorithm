a,b=map(int,input().split())
arr = list(map(int,input().split()))
d=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            r = arr[i]+arr[j]+arr[k]
            if r<=b:
                d.append(r)
print(max(d))

        