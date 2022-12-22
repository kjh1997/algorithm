import sys

input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N): arr.append(list(map(int,input().split())))
a,b,c=0,0,0
def sol(x,y,n):
    global a,b,c
    color = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != arr[i][j]:
                for k in range(3):
                    for l in range(3):
                        sol(x+k*n//3,y+l*n//3,n//3)
                return
    if color == -1: a +=1
    elif color == 0: b +=1
    elif color == 1: c +=1
sol(0,0,N)
print(a)
print(b)
print(c)



