import sys
input = sys.stdin.readline

n= int(input())
ans=[]
stack = []
cnt = 1
tmp = True
for i in range(n):
    d = int(input())
    while cnt <= d:
        stack.append(cnt)
        cnt +=1
        ans.append("+")
    if stack[-1] == d: stack.pop(); ans.append("-")
    else: tmp=False;break    

if tmp: print(*ans)
else: print("NO")