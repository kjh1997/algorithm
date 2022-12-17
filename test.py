def solution():
    from collections import deque
    from itertools import permutation
    cal = ['+','-']
    data = permutation(cal,5)
    print(data.__iter__)
    for i in data.__iter__: 
        print(i)
    return 0

solution()
