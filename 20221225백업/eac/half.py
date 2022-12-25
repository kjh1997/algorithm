T = int(input())
for test_case in range(1, T + 1):
    data , chk = sorted(list(input())),0
    if len(data) == 4 and len(set(data)) == 2: print(f"#{test_case} Yes")
    else: print(f"#{test_case} No")
    