T = int(input())
for test_case in range(1, T + 1):
    a=input()
    for i in range(2,10):
        if a[:i]== a[i:i+i]: result=i; break
        print(a[:i], print(a[i:i+i]))
    print(f'#{test_case} {result}')