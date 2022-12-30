import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
maxNum = max(data)
prime = [True] * (maxNum+1)
prime[1]=False
for i in range(2,int(maxNum**0.5)+1):
    if prime[i] == True:
        for j in range(i+i,maxNum+1,i):
            prime[j]=False
cnt = 0
for i in data:
    if prime[i]==True: cnt+=1

print(cnt)