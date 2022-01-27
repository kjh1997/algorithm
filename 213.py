import time
test = int(input())
for i in range(test):
    N = int(input())
    
    x = 0
    y = 0 
    cnt = 0
    a = [[0]*N for i in range(N)]
    
    while True:
        # 5 4 4 3 / 3 2 2 1 / 1
        for i in range(N): # 시작 가로 오른 > 왼
            print(1)
            cnt +=1 
            a[y][x] = cnt
            if i != 0: x+=1
             
         #   print(x,y)
           # print(cnt)
            if cnt == N**2: break
        N -=1

        for i in range(N): # 세로 위 > 아래
            print(2)
            if cnt == N**2: break 
         #   print(i, y)
            time.sleep(3)
            cnt +=1
            a[y][x] = cnt
            if i != 0: y+=1
            print(cnt)
        for i in range(N): # 가로 왼 > 오른
            print(3)
            if cnt == N**2: break
           # print(i, y)
            time.sleep(3)

            cnt +=1
            a[y][x] = cnt
            if i != 0: x-=1
        N -=1

        for i in range(N): # 세로 아래 > 위
            print(4)
            if cnt == N**2: break
            1#print(i, y)
            time.sleep(3)

            a[y][x] = cnt
            cnt +=1 
            if i != 0: y-=1
            

