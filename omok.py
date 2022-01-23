T = int(input())
for test_case in range(1, T + 1):
    width = int(input())
    board = [[]]* width
    cnt = 0
    for i in range(width):
        board[i] = list(input())
    for i in range(width):
        if cnt >= 1:
            break
        for j in range(width):  
            if board[i][j] == "o":           
                for k in range(1,5):
                    try:
                        if board[i][j+k] != "o":
                            break
                        if k == 4 and board[i][j+k] == "o":
                            cnt +=1
                            break
                    except Exception as e:
                        break
                
                for k in range(1,5):        
                    try:
                        if board[i+k][j+k] != "o":
                            break
                        if k == 4 and board[i+k][j+k] == "o":
                            cnt +=1
                            break
                    except Exception as e:
                        break
            
                for k in range(1,5):    
                    try:
                        if board[i+k][j] != "o":
                            break
                        if k == 4 and board[i+k][j] == "o":
                            cnt +=1
                            break
                    except Exception as e:
                        break
            
                for k in range(1,5):
                    print(k)
                    try:
                        if board[i-k][j-k] != "o":
                            break
                        if k == 4 and board[i-k][j-k] == "o":
                            cnt +=1
                            break
                    except Exception as e:
                        break
            
                for k in range(1,5):  
                    try:  
                        if board[i-k][j] != "o":
                            break
                        if k == 4 and board[i-k][j] == "o":
                            cnt +=1
                            break
                    except Exception as e:
                        break
            
                for k in range(1,5):    
                    try:
                        if board[i][j-k] != "o":
                            break
                        if k == 4 and board[i][j-k] == "o":
                            cnt +=1
                            break
                    except Exception as e:
                        break
            
                for k in range(1,5):    
                    try:
                        if board[i+k][j-k] != "o":
                            break
                        if k == 4 and board[i+k][j-k] == "o":
                            cnt +=1
                            break
                    except Exception as e:
                        break
            
                for k in range(1,5):    
                    try:
                        if board[i-k][j+k] != "o":
                            break
                        if k == 4 and board[i-k][j+k] == "o":
                            cnt +=1
                            break
                    except Exception as e:
                        break
        if cnt >= 1:
            break 
    if cnt >= 1:
        result = "YES"
    else:
        result = "NO"
    print(f'#{test_case} {result}')
