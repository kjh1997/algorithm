T = int(input())
for test_case in range(1, T + 1):
    width,length = map(int,input().split(" "))
    tile = [list(input("").split()) for i in range(width)]
    chk = 0
    # 타일 입력 받음.
    for j in range(width):
        if chk == 1: break
        for i in range(length):
            if chk == 1: break
            if length -1 == i:  continue # 해당 범위를 초과하지 않게, 막아줌
            if tile[j][0][i] =="#":
                # 위치에 타일이 위치하면 2*2 타일로 교체하기 위해, 2*2 만큼의 범위가 다 깨진 타일인지 확인.
                try:
                    if tile[j+1][0][i] == '#' and tile[j+1][0][i+1] == '#' and tile[j][0][i+1] == '#':
                        tile[j][0] = tile[j][0][:i] + "." + tile[j][0][i+1:]
                        tile[j+1][0] = tile[j+1][0][:i] + "." + tile[j+1][0][i+1:]
                        tile[j+1][0] = tile[j+1][0][:i+1] + "." + tile[j+1][0][i+2:]
                        tile[j][0] = tile[j][0][:i+1] + "." + tile[j][0][i+2:]
                    else: chk=1
                # 만약 2*2 범위에 타일이 위치하지 않으면, 교체가 불가능하므로 for문 종료.
                except:
                    chk=1
    print("chk",chk)
    flag, result = 0, ""
    for i in range(len(tile)):
        if tile[i][0].count('#') != 0: 
            flag += 1
    if chk == 0: result = "YES"
    else:  result = "NO"
    print(f'#{test_case} {result}')