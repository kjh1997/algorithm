n,k = map(int,input().split())
arr = [False for i in range(n+1)]
cnt=0
for i in range(2,n+1):
    for j in range(i,n+1,i):
        if arr[j] == False:
            cnt +=1
            arr[j]=True
        if cnt ==k: print(j); exit()