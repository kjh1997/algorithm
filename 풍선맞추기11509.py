import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))

arrow = [0] * 1000001
res = 0
for i in data:
    if arrow[i] <=0: res +=1; arrow[i-1]+=1
    else: 
        arrow[i-1]+=1; 
        arrow[i]-=1
print(res)