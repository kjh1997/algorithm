for tc in range(1, int(input()) + 1):
    N,K = map(int,input().split())
    data = input()
    d_l = int(len(data)/4) 
    result=[]
    for i in range(d_l+1):
        for j in range(4):
            result.append(int(data[j*d_l:j*d_l+d_l],base=16))
        data=data[1:]+data[0]
    print(f'#{tc} {sorted(set(result))[-K]}')