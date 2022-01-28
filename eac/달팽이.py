T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num= N
    a=[[0]*N for i in range(N)]
    x,y,cnt= -1,0,0
    while True:
        for i in range(num):
            if cnt == N**2: break
            if num  !=i: x+=1
            cnt += 1
            a[y][x] = cnt
        num -= 1
        for i in range(num):
            if cnt == N**2: break
            if num !=i:  y+=1
            cnt += 1
            a[y][x] = cnt
        for i in range(num):
            if cnt == N**2: break    
            if num !=i: x-=1
            cnt += 1
            a[y][x] = cnt
        num -= 1    
        for i in range(num):
            if cnt == N**2: break    
            if  num !=i: y-=1
            cnt += 1
            a[y][x] = cnt
        if cnt == N**2: break    
        
    print(f"#{test_case}")
    
    for i in range(len(a)):
        x = ""
        for j in range(len(a[i])):
            x += "".join(str(a[i][j])) + " "
        print(x)