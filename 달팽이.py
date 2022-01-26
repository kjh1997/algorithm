T = int(input())
for test_case in range(1, T + 1):
    data = int(input())
    a = []
    for i in range(data): a.append([])
    for i in range(data):
        for j in range(data):
            a[i].append(0)

    cnt = 1
    cnt2 = 0
    x = 0
    y = 0
    while True:
        if cnt == data**2: break
        for i in range(data): # 시작 오른 > 왼
            if cnt == data**2: break
            a[y][x] = cnt
            cnt +=1
            data -= 1
            if i == data:break
            x +=1
            
            print(x)

        for i in range(data): # 세로 아래로
            if cnt == data**2: break
            a[y][x] = cnt
            cnt += 1
            if i == data:continue

            y +=1


        for i in range(data): # 가로 왼쪽으로
            if cnt == data**2: break
            a[y][x] = cnt
            cnt += 1
            if i == data:continue

            x += 1



        data -= 1
        for i in range(data): # 세로 위로 
            if cnt == data**2: break
            a[y][x] = cnt
            cnt += 1
            y -= 1
        if cnt == data**2: break
print(a)

    
