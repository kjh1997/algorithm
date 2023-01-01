
from collections import Counter
def solution(topping):
    ans =0
    counter = Counter(topping)
    print(counter)
    dic = set()
    for i in topping:   
        counter[i] -=1
        dic.add(i)
        if counter[i] ==0: counter.pop(i)
        if len(dic)==len(counter): 
            ans +=1

        
    return ans

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))