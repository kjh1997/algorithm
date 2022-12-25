from collections import Counter

def solution(s):
    answer = []
    data = []
    s= s.replace("{{","").replace("}}","")
    for i in s.split("},{"):
        data.extend(i.split(","))
    count = sorted(Counter(data).items(),reverse = True, key = lambda x : x[1])
    for k,v in count:
        answer.append(int(k))
    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))