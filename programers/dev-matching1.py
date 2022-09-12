def solution(rows, columns, queries):
    answer = []
    board = []
    for row in range(rows):
        board.append( [i for i in range(columns*row+1, (row+1)*columns+1 )])
    for query in queries:
        
    print(board)
    
    
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))