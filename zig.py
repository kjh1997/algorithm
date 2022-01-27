T = int(input())
for test_case in range(1, T + 1):
    num, result = int(input()), 0
    for i in range(1,num+1):  
        if i //2 == i/2:  result -= i  
        else: result += i
    print(f"#{test_case} {result}")
