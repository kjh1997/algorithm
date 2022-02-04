for tc in range(10):
    N=int(input())
    m=[list(map(str,input())) for _ in range(8)]
    l,cnt=len(m)-N+1,0
    for y in range(l): #세로
        for x in range(8):
            if list(m[y+i][x] for i in range(N)) == list(reversed(list(m[y+i][x] for i in range(N)))): cnt+=1
    for y in range(8): #가로
        for x in range(l):
            if list(reversed(m[y][x:x+N]))==m[y][x:x+N]: cnt+=1
    print(f'#{tc+1} {cnt}')