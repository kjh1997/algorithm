N = int(input())


num= N
a=[[0]*N for i in range(N)]
x= -1
y=0
cnt = 0
print(a)
while True:
    for i in range(num):
        if cnt == N**2: break
        if num  !=i: x+=1
        cnt += 1
        a[y][x] = cnt
        
        print(x,y, num, cnt)
    
    num -= 1
    for i in range(num):
        if cnt == N**2: break
        if num !=i:  y+=1
        cnt += 1
        a[y][x] = cnt
        
        
        print(x,y, num, cnt)
        
    for i in range(num):
        if cnt == N**2: break    
        if num !=i: x-=1
        cnt += 1
        a[y][x] = cnt
        
        print(x,y, num, cnt)

    num -= 1    
    for i in range(num):
        if cnt == N**2: break    
        if  num !=i: y-=1

        cnt += 1
        a[y][x] = cnt
        print(x,y, num, cnt)
    if cnt == N**2: break    
    
print(a)