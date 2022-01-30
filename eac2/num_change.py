T = int(input())
for test_case in range(1, T + 1):
    a,b=map(int,input().split())
    if a+b>=24:a=a+b-24
    else: a= a+b
    print(f'#{test_case} {a}')