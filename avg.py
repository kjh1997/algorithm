from unittest import result

from numpy import average, result_type


t = int(input())
for i in range(t):
    data = list(map(int, input().split()))

    max_index = data.index(max(data))
    data.pop(max_index)
    min_index = data.index(min(data))
    
    data.pop(min_index)
    result_value = sum(data)/ len(data)
    print(f"#{i+1} {int(result_value)}")