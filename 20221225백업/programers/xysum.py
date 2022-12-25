def solution(n, left, right):
    answer = []
    for i in range(n):
        for j in range(n):
            answer.append(max(i+1, j+1))
    return sum(answer[left:right + 1])


print(solution(4,5,7))