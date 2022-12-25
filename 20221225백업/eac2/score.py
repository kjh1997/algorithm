for tc in range(1, int(input())+1):
    d = list(map(int, input().strip()))
    m = len(d)//2
    if sum(d[m:]) == sum(d[:m]): print(f'#{tc} LUCKY')
    else: print(f'#{tc} READY')

