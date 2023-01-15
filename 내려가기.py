# import sys
# input = sys.stdin.readline

# n = int(input())

# data = [list(map(int,input().split())) for i in range(n)]

# maxdp = [data[0].copy()]+[[0]*n for i in range(n-1)]
# mindp = [data[0].copy()]+[[0]*n for i in range(n-1)]

# for i in range(1,n):
#     for j in range(3):
#         if j==0:
#             mindp[j] = data[j]+min(mindp[j],mindp[j+1])
#             maxdp[j] = data[j]+max(maxdp[j],maxdp[j+1])
#         elif j == 1:
#             mindp[j] = data[j]+min(mindp[j],mindp[j-1],mindp[j+1])
#             maxdp[j] = data[j]+max(maxdp[j],maxdp[j-1],maxdp[j+1]) 
#         else:
#             mindp[j] = data[j]+min(mindp[j],mindp[j-1])
#             maxdp[j] = data[j]+max(maxdp[j],maxdp[j-1]) 
            

# print(max(maxdp[n-1]),min(mindp[n-1]))



import sys
input = sys.stdin.readline

n = int(input())


maxdp =[0]*3
mindp =[0]*3
maxtmp =[0]*3
mintmp =[0]*3

for i in range(n):
    a,b,c = map(int,input().split())
    for j in range(3):
        if j==0:
            mintmp[j] = a+min(mindp[j],mindp[j+1])
            maxtmp[j] = a+max(maxdp[j],maxdp[j+1])
        elif j == 1:
            mintmp[j] = b+min(mindp[j],mindp[j-1],mindp[j+1])
            maxtmp[j] = b+max(maxdp[j],maxdp[j-1],maxdp[j+1]) 
        else:
            mintmp[j] = c+min(mindp[j],mindp[j-1])
            maxtmp[j] = c+max(maxdp[j],maxdp[j-1]) 
    for j in range(3):
        maxdp[j]=maxtmp[j]
        mindp[j]=mintmp[j]
    

print(max(maxdp),min(mindp))
