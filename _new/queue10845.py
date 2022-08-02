import sys
input = sys.stdin.readline
q=[]

for i in range(int(input())):
    a = list(map(str, input().split()))
    if a[0] =='push': 
        q.append(a[1])

    if a[0] =='pop':
        print(-1  if len(q)==0 else q.pop(0) )
        
    if a[0] =='size':
        print(len(q))

    if a[0] =='empty':
        print(1 if len(q)==0 else 0)

    if a[0] =='front':print(-1 if len(q)==0 else  q[0])
    if a[0] =='back':print(-1 if len(q)==0 else  q[-1])
