import sys
n = int(input())
tr=[[] for i in range(n)]
re=[["_" for i in range(i+1)] for i in range(n)]
for i in range(n):
    tr[i] =list(map(int,input().split()))
re[0][0] = tr[0][0]
def dp():
    for i in range(1,len(tr)):
        for j in range(len(re[i])):
            if j ==0:
                re[i][j] = re[i-1][0]+ tr[i][0]
            elif j == len(re[i])-1:  
                re[i][j] = re[i-1][j-1]+ tr[i][j]
            else:
                re[i][j] = max(re[i-1][j-1],re[i-1][j]) + tr[i][j]
    print(max(re[-1]))

dp()

