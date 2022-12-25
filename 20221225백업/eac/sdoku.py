T = int(input())
for test_case in range(1, T + 1):
    data = []
    result = ""
    check = 0
    for i in range(9): data.append(list(map(int,input().split())))z
    x_change = []
    for i in range(9):
        data2 = []
        for j in range(9): data2.append(data[j][i])
        x_change.append(data2)

    for i in range(9):
        if len(set(data[i])) != 9:  check=1
        if sum(data[i]) != 45: 
            check=1  
            break
        if len(set(x_change[i])) != 9: check =1
        if sum(x_change[i]) != 45: 
            check=1  
            break
    for i in range(0,9,3):
        if check == 1: break
        sum_arr = []
        for j in range(9):
            sum_arr.append(sum(data[j][i:i+3]))
            if (j+1) // 3 == (j+1) / 3:
                if sum(sum_arr[:3]) != 45:
                    sum_arr = []
                    check = 1
                    break
                else:
                    sum_arr = []
                    check = 0
        if check == 1: break
    if check ==0 : result = 1
    else: result = 0
    print(f"#{test_case} {result}")