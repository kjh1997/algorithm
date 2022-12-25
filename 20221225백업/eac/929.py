T = int(input())
for test_case in range(1, T + 1):
    a = int(input())
    chk, mul, base =  0, [], a
    if a <= 10: 
        result = "Yes"
    else:    
        for i in range(9,0,-1):
            if chk == 1: break
            if len(mul) != 1:
                for j in range(9,0,-1):
                    if a // j == a / j and j != 1:
                        mul.append(j)
                        a /= j
                        break
                    elif j == 1:
                        chk=1
                        break                    
            if len(mul) == 0:chk =1;  break; 
            if chk == 1: break
            if a // i == a / i and i != 1: mul.append(i); break
            elif i == 1: chk=1;  break 
        if chk == 1: result = "No"
        else: 
            if base == mul[0] * mul[1]:result = "Yes"
            else: result = "No"
    print(f"#{test_case} {result}")