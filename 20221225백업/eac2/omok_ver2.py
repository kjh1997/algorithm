for tc in range(1, int(input())+ 1):
    N = int(input())
    b = [list(map(str,input())) for _ in range(N)]
    cnt =0
    for i in range(N):
        for j in range(N-4):
            for k in range(5): 
                if b[i][j+k] !='o': break
                if k == 4: cnt+=1
    for i in range(N):
        for j in range(N-4):
            for k in range(5):
                if b[j+k][i] !='o': break
                if k == 4: 
                    cnt+=1
    for i in range(N-4):
        for j in range(N-4):
            for k in range(5): 
                if b[i+k][j+k] !='o': break
                if k == 4: cnt+=1
    for i in range(N-4): 
        for j in range(N-4):
            for k in range(5): 
                if b[i+k][-k-j-1] !='o': break
                if k == 4: cnt+=1
    if cnt !=0:print(f'#{tc} YES')
    else: print(f'#{tc} NO')