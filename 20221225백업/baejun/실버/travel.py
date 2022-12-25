def bfs(start):
    global board, a, n,cnt
    stack=[start]
    print("?")
    while stack:
        a=stack.pop(0)
        cnt +=1
        v[a-1]=1
        stack.extend(board[a])
        print(stack)
        if 0 not in v:

            break



for tc in range(int(input())):
    n,m=map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(m)]
    board.insert(0,[])
    v=[0]*n
    cnt =0
    print(len(board))
    