T = int(input())
for test_case in range(1, T + 1):
    a, minute, hour = list(map(int,input().split())),  a[1]+a[3], a[0]+a[2]
    if minute >= 60: minute-=60; hour +=1 
    if hour >= 13: hour -= 12
    print(f"#{test_case} {hour} {minute}")
    