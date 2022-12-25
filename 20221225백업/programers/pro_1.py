def solution(arr1, arr2):
    answer = [[0]*len(arr1[0]) for i in range(len(arr1))]
    for i in range(len(arr1)): # 세로
        for j in range(len(arr2[0])): #가로
            for k in range(len(arr2)): # 세로
                answer[i][j]+=arr1[i][k] *arr2[k][j]
    
    
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))