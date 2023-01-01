import sys
input = sys.stdin.readline
print = sys.stdout.write
tc = int(input())
x=[]
y=[]
for i in range(tc):
    x.append(int(input()))
    y.append(int(input()))
mx,my= max(x),max(y)
data = [[0]*(my+1) for _ in range(mx+1)]
for i in range(my+1):
    data[0][i]=i

for i in range(1,mx+1):
    for j in range(my+1):
        data[i][j]=data[i-1][j]+data[i][j-1]

for i in range(tc):
    print(str(data[x[i]][y[i]])+"\n")


