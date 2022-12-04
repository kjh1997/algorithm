# def solution(k, tangerine):
#     answer = 0
#     keys = set(tangerine)
#     data = []
#     for i in keys:
#         data.append(tangerine.count(i))
#     data.sort(reverse=True)
#     for i in data:
#         k -= i
#         answer +=1
#         if k <=0: break
    
    
    
#     return answer
from collections import Counter


def solution(k, tangerine):
    answer = 0
    count = sorted(Counter(tangerine).items(),reverse = True, key = lambda x : x[1])
    for x,v in count  :
        if k <=0: break
        k -= v
        answer +=1
    return answer


print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))