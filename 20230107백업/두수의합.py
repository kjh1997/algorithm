import sys
input = sys.stdin.readline

def cal(arr,n,m):
    ans = 0
    tmp =10e9
    s,e=0,n-1
    while s != e:
        minum = arr[e]+arr[s]
        cur = (abs(m-minum))
        if cur < tmp: 
            tmp =cur
            ans = 0
        if minum < m:
            if cur == tmp: ans +=1
            s +=1
        elif minum > m:
            if cur == tmp: ans +=1
            e -= 1
        else:
            ans +=1
            s +=1
    return ans

tc = int(input())
for i in range(tc):
    n,m = map(int,input().split())
    data = list(map(int,input().split()))
    data.sort()
    print(cal(data,n,m))