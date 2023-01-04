import sys
input = sys.stdin.readline
n = int(input())
arr = [True] * (n+1)
def getPrimeNum():
    for i in range(2, int(n**0.5)+1):
        for j in range(i+i, n+1, i):
            arr[j]=False
    return [i for i in range(2,n+1) if arr[i] == True]
data = getPrimeNum()
for i in range(1,len(data)):
    data[i]=data[i]+data[i-1]
data = [0]+data
res=0
s,e=0,0
while e <= len(data):
    if data[e]-data[s] == n:
        res +=1
        e +=1
        continue
    if data[e]-data[s] <n: e +=1
    elif data[e]-data[s] <n: s+=1
    

print(res)  

