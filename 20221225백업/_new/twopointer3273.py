import sys
N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
data.sort()
dest = int(sys.stdin.readline())
s,e=0,N-1
result = 0
while s!=e:
    tmp = data[s]+data[e]
    if tmp == dest:
        result +=1
        s+=1
    if tmp < dest:
        s+=1
    if tmp > dest:
        e -=1
print(result)


