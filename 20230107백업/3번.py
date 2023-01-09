def solution(arr):
    answer = 10e9

    data = {}
    for i in range(len(arr)):
        if arr[i] not in data:
            data[arr[i]] = i
        else:
            answer = min(answer, abs(data[arr[i]]-i))
            data[arr[i]] = i
    if answer == 10e9:
        return -1

    
    return answer


print(solution([2,1,3,1,4,2,1,3]))