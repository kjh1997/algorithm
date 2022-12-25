def solution(k, m, score):
    answer = 0
    
    score.sort()
    idx= score[::-1].index(k)
    x = len(score)- (len(score)//m)*m 
    score = score[:len(score)-idx]
    score = score[x:]
    for i in range(0,len(score),m):
        answer += score[i] *m
    return answer
    

print(solution(4	,3	,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))