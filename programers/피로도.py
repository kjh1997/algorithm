from itertools import permutations

def solution(k, dungeons):
    answer = -1
    data = permutations(dungeons,len(dungeons))       
    for d in data:
        cur = k
        cnt = 0
        for i in d:
            if cur < i[0] or cur <= i[1]: continue
            cnt +=1
            cur -= i[1]
        if answer < cnt: answer=cnt


    return answer



print(solution(80,[[80,20],[50,40],[30,10]]))