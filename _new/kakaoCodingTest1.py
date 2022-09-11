def solution(board, moves):
    stack = []
    answer = 0
    l = len(board[0])
    for i in moves:
        for depth in range(laaaaaaaaaaaaaaaaaa):
            
            if  board[depth][i-1] != 0:
                tmp = board[depth][i-1]
                stack.append(tmp)
                board[depth][i-1]=0
                break
       # print(tmp, board, stack)
        if len(stack) >1 and stack[-1] == stack[-2]:
            print("??")
            stack.pop();stack.pop()
            answer+=1
            
    
    return answer
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],	[1,5,3,5,1,2,1,4]))