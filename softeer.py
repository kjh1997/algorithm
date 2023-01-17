import sys
input = sys.stdin.readline
ans = 0
for i in range(5):
    a,b = map(str,input().strip().split())  
    a,b= list(map(int,a.split(":"))),list(map(int,b.split(":")))
    ans += (b[0]*60 + b[1])-(a[0]*60 + a[1]) 
print(ans)