T = int(input())
for t in range(1, T + 1):
    a=list(map(int,input().split()))
    s,e =0,0
    if a[0]<a[2]:s=a[2]
    else: s=a[0]
    if a[1]<a[3]:e=a[1]
    else: e=a[3]

    if e-s<0: print(f'#{t} {0}')
    else: print(f'#{t} {e-s}')
    