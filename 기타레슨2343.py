import sys

input = sys.stdin.readline

n,m = map(int,input().split())
data= list(map(int,input().split()))
s,e= max(data), sum(data)

while s<=e:
    mid= (s+e)//2
    tmp = 0
    cnt = 0
    arr = []
    for i in range(n):
        if tmp + data[i] >= mid:
            arr.append(tmp + data[i])
            cnt +=1
            tmp =0            
        else:
            tmp += data[i]
 
    if cnt> m:
        s = mid +1

    elif cnt<m: 
        e = mid-1
    else:
        print(max(arr)); exit()
    

