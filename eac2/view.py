for tc in range(10):
    re=0
    _ = input()
    d = list(map(int, input().split()))
    for i in range(2,len(d)-1):
        if max(d[i-2:i+3]) != d[i]: continue
        else:
            b=d[i-2:i+3]
            m=max(b)
            re += b.pop(b.index(m))-max(b)
    print(f'#{tc+1} {re}')