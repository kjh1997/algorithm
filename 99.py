T = int(input())
for test_case in range(1, T + 1):
    a = int(input())
    result = ""
    if a > 81:
        result = "No"
    else:
        for i in range(9,0,-1):
            x = a / i 
            if x <= 9:
                if int(x) == x:
                    for j in range(1,10):
                        if x/j == 1:
                            result = "Yes"
                            break
                    else:
                        result = "No"
                if result == "Yes":
                    break
                else:
                    result = "No"
                    continue
            elif x > 9:
                continue
    
    print(f'#{test_case} {result}')