def solution(order):
    tmp = []
    i = 1
    now = 0
    
    while i != len(order)+1:
        print(i)
        tmp.append(i)
        while tmp[-1] == order[now]:
            now += 1
            tmp.pop()
            if len(tmp) == 0:
                break
        i += 1

    return now

print(solution( [4, 3, 1, 2, 5] ))
# print(solution([5, 4, 3, 2, 1]))