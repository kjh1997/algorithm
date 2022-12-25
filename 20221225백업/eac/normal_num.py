T = int(input())
for test_case in range(1, T + 1):
    num=int(input())
    data,cnt = list(map(int, input().split())),0
    for i in range(1, len(data)-1):
        if data[i-1] < data[i] < data[i+1] or data[i+1] < data[i] <data[i-1]: cnt += 1
    print(f"#{test_case} {cnt}")