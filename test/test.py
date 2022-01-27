T = int(input())
for test_case in range(1, T + 1):
    base_num, k = map(int,input().split())
    cnt = 0
    while True:
        if base_num% k != 0: base_num //= k
        else: base_num -= 1
        cnt += 1
        if base_num ==1: break
    print(f'#{test_case} {cnt}')