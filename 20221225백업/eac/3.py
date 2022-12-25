

T = int(input())
for test_case in range(1, T + 1):
    data, result = list(map(int, input().split())), ""
    if data[0] > data[1]: result = ">"
    elif data[0] < data[1]: result = "<"
    else: result = "="
    print(f'#{test_case} {result}')