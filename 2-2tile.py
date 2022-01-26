T = int(input())
for test_case in range(1, T + 1):
    width,length = map(int,input().split(" "))
    tile = []
    for i in range(width):
        tile.append(list(input("").split()))
    for j in range(width):
        if j == width -1:
            continue
        for i in range(length):
            if length -1 == i:
                continue
            if tile[j][0][i] =="#":
                if tile[j+1][0][i] == '#' and tile[j+1][0][i+1] == '#' and tile[j][0][i+1] == '#':
                   
                    tile[j][0] = tile[j][0][:i] + "." + tile[j][0][i+1:]
                    tile[j+1][0] = tile[j+1][0][:i] + "." + tile[j+1][0][i+1:]
                    tile[j+1][0] = tile[j+1][0][:i+1] + "." + tile[j+1][0][i+2:]
                    tile[j][0] = tile[j][0][:i+1] + "." + tile[j][0][i+2:]
                  #  print(tile)
    flag = 0
    for i in range(len(tile)):
       # print(tile[i][0], tile[i].count('#'))
        if tile[i][0].count('#') != 0:
            
            flag += 1
    result = ""
    if flag == 0:
        result = "YES"
    else:
        result = "NO"
    print(f'#{test_case} {result}')