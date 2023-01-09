from itertools import combinations

def solution(arr, n):
    s,e = 0,len(arr)-1
    arr.sort()
    while s!=e:
        tmp = arr[s]+arr[e]
        if tmp == n:
            return True
        if tmp < n:
            s+=1
        if tmp > n:
            e -=1
    
    return False

print(solution([5,3,9,13],7))
