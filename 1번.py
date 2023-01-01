def solution(p):
    answer = p+1
    tmp = p+1
    while True:

        if len(list(str(tmp))) == len(set(list(str(tmp)))): 
            answer = tmp
            break
        tmp+=1

 
    return answer


print(solution(1987))