T = int(input())
for test_case in range(1, T + 1):
    x = []
    b = int(input())
    for i in range(b[0]):
        data =list(map(int, input().split(" ")))
        x.append(data[0]*0.35 + data[1] * 45 + data[2] * 0.20)
    
    x = sorted(x)
    print(f"#{test_case} {chr(b[1]+96).upper()}")

        


