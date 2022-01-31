T = int(input())
for test_case in range(1, T + 1):
    TC = int(input())
    data = list(map(int, input().split()))
    print(f'{TC} {max(set(data), key = data.count)}')
