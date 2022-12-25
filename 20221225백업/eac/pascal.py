T = int(input())
for test_case in range(1, T + 1):
    tri = int(input())
    a = []
    for i in range(tri): a.append([])
    a[0].append(1)
    for i in range(1,tri):
        for j in range(i+1): a[i].append(0)
        for j in range(j+1):
            if j - 1 < 0: a[i][j] = a[i-1][j]
            else:  
                try:  a[i][j] =a[i-1][j] + a[i-1][j-1]   
                except:  a[i][j] = a[i-1][j-1]
    print(f"#{test_case}")
    for i in a:
        x = ""
        for j in i: x += str(j) +" "
        print(x)

        
            