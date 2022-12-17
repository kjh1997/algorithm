from collections import deque

def solution(q1, q2):
    answer=0
    q1 = deque(q1)
    q2 = deque(q2)
    q1s = sum(q1)
    q2s = sum(q2)
    tot = q1s+q2s
    limit = 4*len(q1)
    if tot % 2 != 0:
            return -1
    while True:
        
        if q1s< q2s:
            t = q2.popleft()
            q1s += t
            q2s -= t
            q1.append(t)
            answer +=1
        elif q1s > q2s:
            t = q1.popleft()
            q1s -= t
            q2s += t
            q2.append(t)
            answer +=1
        else:
            break
        if limit == answer:
            return -1
    return answer



print(solution([3, 2, 7, 2],[4,6,5,1]))