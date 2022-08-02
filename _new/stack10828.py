import sys
input = sys.stdin.readline
stack=[]
for i in range(int(input())):
    a = list(map(str, input().split()))
    if a[0] =='push': 
        stack.append(a[1])

    if a[0] =='top':
        print(-1  if len(stack)==0 else stack[-1] )
        
    if a[0] =='size':
        print(len(stack))

    if a[0] =='empty':
        print(1 if len(stack)==0 else 0)

    if a[0] =='pop':print(-1 if len(stack)==0 else  stack.pop())
