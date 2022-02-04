for tc in range(1,11):
    _ = input()
    board = []
    max_value = 0
    for i in range(100):
        now = list(map(int,input().split()))
        board.append(now)
        value = sum(now)
        if max_value < value:
            max_value = value
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += board[j][i]
        if max_value < temp:
            max_value = temp
    print('#{0} {1}'.format(tc,max_value))