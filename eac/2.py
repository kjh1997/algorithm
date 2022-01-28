T = int(input())
for test_case in range(1, T + 1):
    data = list(map(int, input().split(" ")))
    a = sum(data)/ 10
    print(f'#{test_case} {round(a)}')