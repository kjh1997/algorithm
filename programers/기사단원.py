def solution(number, limit, power):
    answer = []
    for i in range(1,number+1):
        n = getCount(i) +1
        if  n <= limit:
            answer.append(n)
        else: answer.append(power)

    return sum(answer)

def getCount(num):
    cnt = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i ==0:
            cnt.append(i)
    return len(cnt)


def getCount(n): 
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    print(a)
    return len(set(a))
def solution(number, limit, power):
    return sum([getCount(i) if getCount(i)<=limit else power for i in range(1,number+1)])


print(solution(5,3,2))