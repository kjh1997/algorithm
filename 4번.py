def solution(n):
    tmp = []
    num = 0
    while n > 0:
        tmp.append(n % 2)
        n //= 2
    for i in range(len(tmp)):
        if tmp[i] == 1:
            num += 3**i
    return num
print(solution(11))