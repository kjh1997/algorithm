import sys
input = sys.stdin.readline
tc = int(input())
data = [ int(input()) for i in range(tc)]
dp = [0,1]
while dp[-1] < 1e10: dp.append(sum(dp[-2:]))

for i in data:
    result=[]
    for j in dp[::-1]:
        if i ==0: break
        if i - j < 0: continue
        else: 
            i -= j
            result.append(j)
    print(" ".join(map(str,result[::-1])))