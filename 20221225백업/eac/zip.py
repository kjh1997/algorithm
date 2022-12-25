T = int(input())
for test_case in range(1, T + 1):
    num  = int(input())
    data, result, result2 = [], [], []    
    for i in range(num): data.append(list(map(str, input().split())))
    for i in data:
        for j in range(int(i[1])): result.append(i[0])   
    cnt = 0
    if sum([int(i[1]) for i in data ])//10 == sum([int(i[1]) for i in data ])/10: cnt =( sum([int(i[1]) for i in data ]) // 10)
    else: cnt = (sum([int(i[1]) for i in data ]) // 10) + 1   
    for i in range(cnt): result2.append([])
    cnt = 0
    for j in result:
        if len(result2[cnt]) // 10 == len(result2[cnt]) / 10 and len(result2[cnt]) != 0 : cnt +=1
        result2[cnt].append(j)
    print(f"#{test_case}")
    for i in range(len(result2)):
        print("".join(result2[i]))
