for tc in range(10):
    dump = int(input())
    b = list(map(int, input().split()))
    for i in range(dump):
        mi,ma=min(b),max(b)
        b[b.index(mi)] +=1
        b[b.index(ma)] -=1
    print(f'#{tc+1} {max(b)-min(b)}')