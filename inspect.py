T = int(input())
for test_case in range(1, T + 1):
    data , check= list(input()) , 1
    if len(data) // 2 != len(data) / 2: data.pop(len(data)//2)
    for i in range(len(data)//2):
        if data[i] != data[(len(data)-1-i)]:
            check = 0
            break 
    print(f'#{test_case} {check}')

            