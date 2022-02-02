score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(int(input())):
    N,K = map(int, input().split())
    s_g = []
    for i in range(N): 
        a,b,c = map(int, input().split())
        s_g.append(a*0.35 + b*0.45 + c*0.2)
    k_s = s_g[K-1] 
    data = sorted(s_g, reverse=True).index(k_s)//int((N/10))
    print(f'#{tc+1} {score[data]}')

    
