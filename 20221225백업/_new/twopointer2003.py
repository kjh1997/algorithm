import sys

n,m = map(int, sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
s=0
e = 1
cnt = 0
while e <=n and s<=e:
    tmp = sum(data[s:e])
    if tmp == m:
        e+=1
        cnt +=1

    if tmp > m:
        s += 1
    if tmp < m:
        e +=1
    print(s,e)
print(cnt)




