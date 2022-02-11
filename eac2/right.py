r=[]
for t in range(1,int(input())+1):
    a=list(map(int,input().split()))
    e,s=min(a[1],a[3]), max(a[0],a[2])
    if e-s<0: r.append(0)
    else: r.append(e-s)
for j,i in enumerate(r):print(f'#{j+1} {i}')