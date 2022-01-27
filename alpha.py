T = int(input())
for test_case in range(1, T + 1):
    data = sorted(input())
    for i in range(len(data)-1,0,-1):
        if data[i-1] == data[i]: del data[i-1:i+1]
        
    result=""
    if data == []: result = "Good"
    else: 
        for i in data: result += i
    print(f"{test_case} {result}")