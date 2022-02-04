for tc in range(int(input())):
    a=int(input())
    m = [list(map(int,input())) for _ in range(a)]
    r, cnt,l=0,0,len(m)
    for n,i in enumerate(m):
        if n < l//2+1: r+= sum(i[l//2-n :l//2+n+1 ])
        else:
            cnt +=1
            r+= sum(i[cnt:l-cnt])
    print(f'#{tc+1} {r}')
