T = int(input())
for test_case in range(1, T + 1):
    data = list(map(int, input().split(" ")))
    a = 0
    for i in data:
        if i %2 !=0:a += i 
    print(f'#{test_case} {a}')