T = int(input())
for test_case in range(1, T + 1):
    D,L,N = map(int, input().split())
    a = D
    for i in range(1, N): a += D*(1+i*0.01*L); 
    print(f"#{test_case} {int(a)}")
