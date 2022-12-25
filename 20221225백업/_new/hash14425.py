import sys
n,m = map(int,sys.stdin.readline().split())
S= set(sys.stdin.readline() for i in range(n))
cnt =0
for i in range(m):
    i = sys.stdin.readline()
    if i in S: cnt +=1
print(cnt)