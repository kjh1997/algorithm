T = int(input())
for test_case in range(1, T + 1):
    a=int(input())
    data = [[0]*a for i in range(a)]
    data[0][0] = 1
    for i in range(1, a):
        for j in range(i+1):
            cnt = 0
            try: 
                if data[i-1][j] != 0: cnt += data[i-1][j]
            except: pass
            try: 
                if data[i-1][j-1] != 0: cnt += data[i-1][j-1]
            except: pass
            data[i][j]=cnt
        
    print(f"#{test_case}")
    for i in data:
        x = ""
        for j in i: 
            if j != 0: x += str(j) +" "
            else: break
        print(x)